---
layout: default
title: Saving Vector Embeddings to a Milvus Database
---

# Saving Vector Embeddings to a Milvus Database

##### NOTE:
This post is the third in a series that outlines how to build a search engine for fast similarity search using vector databases and vector embedding techniques

## Summary

In the [previous post](/2023/08/06/similarity-search-api) I added a simple API layer using [FastAPI](https://fastapi.tiangolo.com/).  In this post, I want to now use that API layer to save the vector embeddings for words to a vector database ([Milvus](https://milvus.io) in this case) so they can later be used to search for similar word embeddings.

## Code

The directory structure for this section remains the same as the previous section:
- data
- handlers
- models
     - definitions
     - trained
- repositories
- type_definitions
- train_model.py
- server.py
- requirements.txt

The first step is to get Milvus running on your machine as a docker container.  This is actually quite easy using a simple bash script:

run_milvus.sh

```
wget https://github.com/milvus-io/milvus/releases/download/v2.2.13/milvus-standalone-docker-compose.yml -O docker-compose.yml

docker-compose up -d
```

This should start the milvus database on your machine, and make it available via port 19530 (the default).

If you execute a `docker ps` command, you should see something like this:

```
f8e6464cbce3   milvusdb/milvus:v2.2.13                    "/tini -- milvus run…"   2 days ago   Up 3 seconds                      0.0.0.0:9091->9091/tcp, 0.0.0.0:19530->19530/tcp   milvus-standalone
4a3e4de426a2   minio/minio:RELEASE.2023-03-20T20-16-18Z   "/usr/bin/docker-ent…"   2 days ago   Up 3 seconds (health: starting)   9000/tcp                                           milvus-minio
2f46b39981e0   quay.io/coreos/etcd:v3.5.5                 "etcd -advertise-cli…"   2 days ago   Up 3 seconds                      2379-2380/tcp                                      milvus-etcd
```

The next step is to create the mivlus repository in our API code so we can save data to it.  Create a file named `milvus_embeddings_repository.py` in the respositories directory, and import the required components from pymilvus (
pymilvus==2.2.13 should be added to the requirements.txt file):

```
from pymilvus import(
    connections,
    db,
    Collection,
    utility,
    FieldSchema,
    DataType,
    CollectionSchema
)
```

In addition, we will be using numpy for some array manipulations, and our DocumentInfo class to pass data into the repository, so add the following imports to your repository module:

```
from type_definitions.document_info import DocumentInfo
import numpy as np
```

As part of saving the document embeddings, we also want to save the document meta data, so that when we find a match later, we can get the information about the matching data that we need.  We'll use the DocumentInfo class to pass this metadata, so create a function with the following signature:

```
def save_document_embeddings(document: DocumentInfo, embeddings):
```

This will be the main entry point to our repository.  

Milvus uses a hierarchy of abstractions to represent data, so we need to set up those abstractions in our code to ensure we can properly write to Milvus.  The hierarchy is as follows:

- connection
  - database
    - collection
      - schema 

the first thing we'll do is tell pymilvus how to connect to our instance of Milvus running on our local machine.  To do this, create a function to set up the connection:

```
def get_connection():
    conn = connections.connect(
        alias='default',
        host='localhost',
        port=19530
    )

    return conn
```

This function uses the default connection parameters for the locally running of Milvus (NOTE: this connection is not secured in any way).  

Once we have the connection, we need to ensure there is a database that is set up to save data to.  We do this by first ensuring the connection, then checking to see if the connection already contains a database with the name we want (`documents`.  very creative).

```
def ensure_document_db():
    conn = get_connection()

    db_name = 'documents'
    existing_dbs = db.list_database()

    if db_name not in existing_dbs:
        database = db.create_database(db_name)

    db.using_database(db_name)
```

Once we have ensured that the database exists, we want to ensure that we have a collection for the data.  Before we can create the collection though, we need to set up the data schema we want to use to save the embeddings and the metadata.  In this case, we want to save the document name, url, and text, along with an auto generated primary key.  We also will set up a vector field to hold the embeddings.  The schema will look like this:

```
def get_schema():
    document_pk = FieldSchema(
        name="document_pk",
        dtype=DataType.INT64,
        is_primary=True,
        auto_id=True,
        max_length=200,
    )

    document_name = FieldSchema(
        name="document_name",
        dtype=DataType.VARCHAR,
        is_primary=False,
        auto_id=False,
        max_length=200,
    )

    document_url = FieldSchema(
        name="document_url",
        dtype=DataType.VARCHAR,
        is_primary=False,
        auto_id=False,
        max_length=1000,
    )

    document_text = FieldSchema(
        name="document_text",
        dtype=DataType.VARCHAR,
        is_primary=False,
        auto_id=False,
        max_length=65535,
    )

    embeddings = FieldSchema(name="embeddings", dtype=DataType.FLOAT_VECTOR, dim=10000)

    schema = CollectionSchema(
        fields=[document_pk, document_name, document_url, document_text, embeddings],
        description="document info embeddings",
        enable_dynamic_field=False,
    )

    return schema
```

Notice the five fields we added, and their associated data types.  Now that the schema has been defined, creating the collection looks like this:

```
def ensure_collection(recreate_index=False):
    ensure_document_db()

    schema = get_schema()

    collection_name ="document_collection"

    if recreate_index:
        utility.drop_collection(collection_name)

    collection = Collection(name=collection_name, schema=schema)

    return collection
```

The recreate_index parameter allows us to drop and recreate the collection, in the case that we want to make a change to the schema.  If no changes are needed, this function will check for the collection and create it if it does not exist.

Now that all of the housekeeping for data persistence is done, the `save_document_embeddings` function can be filled out:

```
def save_document_embeddings(document: DocumentInfo, embeddings):
    document_collection = ensure_collection()

    padded_embeddings = np.pad(embeddings, (0, 10000-len(embeddings)), mode='constant', constant_values=(0))
    print(padded_embeddings)

    data = {
        "document_name":document.name,
        "document_url":document.url,
        "document_text":document.text,
        "embeddings":padded_embeddings
    }

    result = document_collection.insert(data)
    
    return result
```

Here we simply ensure the collection (which in turn ensures the database and conneciton), and format the data.  Notice the `padded_embeddings` line.  Milvus expects the vector embeddings to be of a known size (no ragged arrays), so we use numpy to pad out the embeddings to the maximum length with zeros.

That is all that's required for the milvus repository.

To actually save the document metadata and embeddings, we import the repository into the `document_command_handler` module like this:
```
from repositories.milvus_embeddings_repository import  save_document_embeddings
```

and modify the `handle_index_document_command` function to use the repository:
```
def handle_index_document_command(self, document:DocumentInfo):
        
        terms = document.get_terms()
        prediction = self.model.predict(terms)

        embedding = np.array(prediction).squeeze()

        save_document_embeddings(document, embedding)
        
        return embedding
```

Now, when you call the API by posting data to it, you'll get the same response from the API as you previously did, but your vector embeddings and document metadata will be saved to milvus so we can look across documents to find similar embeddings, and find related documents.

## Conclusion

Milvus is a simple to set up, simple to use vector embedding database, and in the next post we'll use the vectors we save to Milvus to perform similarity searches for related document, based on their text embeddings.


I hope this was helpful.  If I messed anything up or there is a better way to do it, I'd love to hear from you at [j.henry@jhenrycode.com](mailto:j.henry@jhenrycode.com)