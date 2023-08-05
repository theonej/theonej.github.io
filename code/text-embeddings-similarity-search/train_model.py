from repositories.vocabulary_repository import get_vocabulary
from models.definitions.text_vector_model import create_text_vectorization_model

def train_vector_embeddings_model():
    vocabulary = get_vocabulary(vocabulary_path='./data/book_summaries/chapter_10.txt')

    model = create_text_vectorization_model(vocabulary=vocabulary)
    model.save('./models/trained/text_vector_model', save_format='tf')

    text_input = [
        ['please vectorize this sentence'],
        ['this is another sentence that I would like to vectorize.  it is much longer']
    ]

    embeddings = model.predict(text_input)
    print(embeddings)

train_vector_embeddings_model()