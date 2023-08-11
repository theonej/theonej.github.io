---
layout: default
title: Adding an API layer for the embedding model
---

# Vector Text Embeddings API

##### NOTE:
This post is the second in a series that outlines how to build a search engine for fast similarity search using vector databases and vector embedding techniques

## Summary

In the [previous post](/2023/08/03/text-embeddings-with-keras) I showed how you can create a vector embedding model using [Keras](https://keras.io/).  In this post, I'll build a simple API layer using [FastAPI](https://fastapi.tiangolo.com/), wich is a great framework for high-performance APIs built in python.

## Code

The directory structure for this API builds on the last one, and adds a few new leaves:

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

You should notice that the `main.py` file was renamed to `train_model.py` and that a new `server.py` file was added.  This will act as the entry point to the API.

In `server.py`, a single method is defined using the FastAPI framework that accepts a `DocumentInfo` object (more on that in a bit), calls a command handler to create the embeddings, and then returns the embeddings.

It should be pointed out that this method returns a `201 [created]` status code.  The code for `server.py` looks like this:

```
from fastapi import FastAPI
from type_definitions.document_info import DocumentInfo
from handlers.document_command_handlers import DocumentCommandHandlers

app = FastAPI()

@app.post("/documents", status_code=201)
def index_document(document:DocumentInfo):
    handler = DocumentCommandHandlers()

    embeddings = handler.handle_index_document_command(document)
    print(embeddings)
    
    return {"embeddings":embeddings.tolist()}

```

The `DocumentInfo` class is defined in the `type_definitions/document_info.py` file.  It has three properties (`name`, `text`, and `url`), and three methods (`get_terms`, `clean_text`, and `remove_newlines`).  The url field can be used if you are getting embeddings for a document that has a URI that cen be used to retrieve the full document.  The `get_terms` method returns the document text as an array of text terms.  The code looks like this:

```
from pydantic import BaseModel

class DocumentInfo(BaseModel):

    name : str
    url : str
    text : str
    
    def get_terms(self):
        term_array = self.clean_text(self.text)

        return term_array

    def clean_text(self, text_to_clean):
        term_array = text_to_clean.split(' ')
        
        term_array = list(map(lambda text: self.remove_newlines(text), term_array))
        term_array = list(filter(lambda text: text != '', term_array))

        return term_array

    def remove_newlines(self, text):
        text = text.replace('\n', '')

        return text
```

The next file is the command handler class that accpets the DocumentInfo object and creates the embeddings.  This code is created as a class so that the model, which can be expensive to inistantiate, can be reused without penalty (you could also create the model as a singleton object, but that seems excessive for this toy example).

The `DocumentCommandHandlers` class has a single method: `handle_index_document_command`, wich gets the document terms, uses the trained model to predict the embeddings, and then squeezes the result to reshape it from a matrix with a single column into a flattened array.

The code looks like this:

```
from models.definitions.text_vector_model import get_trained_text_vectorization_model
from type_definitions.document_info import DocumentInfo
import numpy as np

MODEL_PATH = './models/trained/text_vector_model'

class DocumentCommandHandlers:
    def __init__(self):
        self.model = get_trained_text_vectorization_model(MODEL_PATH)

    def handle_index_document_command(self, document:DocumentInfo):
        
        terms = document.get_terms()
        prediction = self.model.predict(terms)

        embedding = np.array(prediction).squeeze()

        return embedding
```

That's all there is to it.  If you run `uvicorn server:app --reload --port 10000` and send a POST command to `0.0.0.0:10000/documents`, with the following json:
```
{
  "name":"test-document",
  "url":"https://blog.jhenrycode.com",
  "text": "this is the contents of a document that I want indexed"
}
```

you should get back a vector of integer embeddings that represent the document text, looking something like this (your values may vary, based on the corpus you chose to train on):

```
{
  "embeddings": [
    18,
    50,
    2,
    1,
    4,
    8,
    1,
    11,
    9,
    1,
    1
  ]
}
```

## Conclusion

FastAPI is a light-weight, performant API framework for python that is very easy to get started with.  In the next post, we will enhance the API with a persistence layer for the embeddings, based on the [Milvus](https://milvus.io) vector database, wich will allow us to then perform a similarity search to find similar documents.

I hope this was helpful.  If I messed anything up or there is a better way to do it, I'd love to hear from you at [j.henry@jhenrycode.com](mailto:j.henry@jhenrycode.com)