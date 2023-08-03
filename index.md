---
layout: default
title: Creating a text embedding model with keras
---

# Vector Text Embeddings

##### NOTE:
This post is the first in a series that will outline how to build a search engine for fast similartiy search using vector databases and vector embedding techniques

## Summary

With the recent popularity of vector databases, vector embeddings are being used in a new set of applications that use vectors of numbers to represent many different types of data, from documents to images to time series data.  Using these vector embeddings, similarity searches can then be performed that will find approximate results (see [ANN](https://towardsdatascience.com/comprehensive-guide-to-approximate-nearest-neighbors-algorithms-8b94f057d6b6) for details).

When the data you want to represent is a text document, you need a way to convert your text into a vector of numbers so it can be used for searching.  Vector embeddings of text are an interesting topic, that is outside of the scope of this post, but you can learn more about the nitty gritty details [here](https://www.tensorflow.org/text/tutorials/word2vec).

Tensorflow provides a very easy way to create text embeddings, based on any corpus of text that you want to represent, in a matter of minutes.  Once you create the embedding model, it can be used in your software to create embeddings that will work with popular vector databases like [Milvus](https://milvus.io) abnd [Pinecone](https://www.pinecone.io/). 

## Code

All of the code for this post can be found [here](https://github.com/theonej/theonej.github.io/tree/master/code/text-embeddings-with-keras).

The first thing to do is to get a text corpus (vocabulary) to train your model on.  I used the [booksum](https://www.tensorflow.org/datasets/catalog/booksum) dataset from tensorflow, and just picked a chapter at random.  

The directory structure for the project is:

- data
    - book_summaries
        - chapter_10.txt
- models
     - definitions
     - trained
- repositories
- main.py
- requirements.txt

Once you have the text corpus in the **book_summaries** directory, the next step is to create a repository to fetch and clean the text so it can be used by the vectorization model.  The following code creates a repository in the **repositories** directory that loads the vocabulary data, removes the line endings in text, and remove any entries that consist of only line endings.  The code looks like this:


```
def get_vocabulary(vocabulary_path):
    vocabulary_array = open(vocabulary_path).readlines()

    vocabulary = clean_vocabulary(vocabulary_array)

    return vocabulary

def clean_vocabulary(vocabulary_array):
    vocabulary_array = list(map(lambda text: remove_newlines(text), vocabulary_array))
    vocabulary_array = list(filter(lambda text: text != '', vocabulary_array))

    return vocabulary_array

def remove_newlines(text):
    text = text.replace('\n', '')

    return text
```
Once you have the repository in place, you're ready to create the model that will use the vocabulary to create the embeddings.  In the **models/definitions** directory, create a file named text_vector_model.py.  This model will create a simple Sequential model with a single TextVectorization layer and will use the TextVectorization layer to ingest the vocabulary to create the embeddings.  the code looks like this:

```
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
```

The next step is to pull it all together to load the vocabulary, train the model and save the model so it can be used later.  Create a file in the root of your project called main.py.  This file will load the vocabulary from the data directory, create the model using the vocabulary, and then test the model to create a few vector embeddings of some sample sentences.

The code looks like this:

```
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
```

And that's it.  

If you look in the **models/trained** directory, you'll see the files that represent the trained model (which can later be loaded and used to create vector embeddings, which I will post about in the next installment).

I hope this was helpful.  If I messed anything up or there is a better way to do it, I'd love to hear from you at [j.henry@jhenrycode.com](mailto:j.henry@jhenrycode.com)