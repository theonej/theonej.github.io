from models.definitions.text_vector_model import get_trained_text_vectorization_model
from type_definitions.document_info import DocumentInfo
from repositories.milvus_embeddings_repository import  save_document_embeddings

import numpy as np

MODEL_PATH = './models/trained/text_vector_model'

class DocumentCommandHandlers:
    def __init__(self):
        self.model = get_trained_text_vectorization_model(MODEL_PATH)

    def handle_index_document_command(self, document:DocumentInfo):
        
        terms = document.get_terms()
        prediction = self.model.predict(terms)

        embedding = np.array(prediction).squeeze()

        save_document_embeddings(document, embedding)
        
        return embedding