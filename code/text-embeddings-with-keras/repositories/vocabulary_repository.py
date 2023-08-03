
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