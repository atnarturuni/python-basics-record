from translator import (
    get_parameters,
    print_translation,
    DICT,
    REVERSED_DICT,
    prepare_word,
    get_translation
)

while True:
    word, direction = get_parameters()
    word = prepare_word(word)

    if direction == 1:
        translation = get_translation(word, DICT)
    else:
        translation = get_translation(word, REVERSED_DICT)
    print_translation(word, translation)
