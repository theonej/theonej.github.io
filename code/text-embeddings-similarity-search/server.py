from fastapi import FastAPI
from type_definitions.document_info import DocumentInfo
from handlers.document_command_handlers import DocumentCommandHandlers
import json

app = FastAPI()

@app.post("/documents", status_code=201)
def index_document(document:DocumentInfo):
    handler = DocumentCommandHandlers()

    print(document)
    
    embeddings = handler.handle_index_document_command(document)
    print(embeddings)
    
    return {"embeddings":embeddings.tolist()}

@app.get("/health-check")
def health_check():
    return True