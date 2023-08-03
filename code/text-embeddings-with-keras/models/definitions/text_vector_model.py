import tensorflow as tf
from keras.layers import TextVectorization
from keras import Input
from keras.models import Sequential

def create_text_vectorization_model(vocabulary):
    
    vector_layer = TextVectorization(
        output_mode ='int'
    )

    vocab_dataset = tf.data.Dataset.from_tensor_slices(vocabulary)
    vector_layer.adapt(vocab_dataset)

    input = Input(shape=(1,), dtype=tf.string)
    
    model = Sequential()

    model.add(input)
    model.add(vector_layer)

    return model