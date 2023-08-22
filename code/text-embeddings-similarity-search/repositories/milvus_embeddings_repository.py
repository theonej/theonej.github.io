from type_definitions.document_info import DocumentInfo
import numpy as np

from pymilvus import(
    connections,
    db,
    Collection,
    utility,
    FieldSchema,
    DataType,
    CollectionSchema
)

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

def get_connection():
    conn = connections.connect(
        alias='default',
        host='localhost',
        port=19530
    )

    return conn

def ensure_document_db():
    conn = get_connection()

    db_name = 'documents'
    existing_dbs = db.list_database()

    if db_name not in existing_dbs:
        database = db.create_database(db_name)

    db.using_database(db_name)

def ensure_collection(recreate_index=False):
    ensure_document_db()

    schema = get_schema()

    collection_name ="document_collection"

    if recreate_index:
        utility.drop_collection(collection_name)

    collection = Collection(name=collection_name, schema=schema)

    return collection


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

