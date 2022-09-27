def get_translation(word, dictionary):
    if word in dictionary:
        return dictionary[word]
    else:
        return None


def prepare_word(word):
    return word.lower().strip()
