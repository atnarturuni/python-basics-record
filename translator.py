DICT = {
    "mother": "мама",
    "father": "папа",
    "sun": "солнце",
    "son": "сын",
    "cat": "кот",
    "dog": "собака",
    "car": "машиниа",
    "door": "дверь",
    "note": "заметка",
}

REVERSED_DICT = {}
for key, value in DICT.items():
    REVERSED_DICT[value] = key

while True:
    word = input("Введите слово для перевода: ")

    print("Выберите направление перевода")
    print("1. с английского на русский (по умолчанию)")
    print("2. с русского на английский")
    direction = input()
    if not direction:
        direction = 1
    direction = int(direction)

    if direction == 1:
        if word in DICT:
            translation = DICT[word]
            print(f"Перевод слова {word} - {translation}")
        else:
            print(f"Нет перевода для слова {word}")
    else:
        if word in REVERSED_DICT:
            translation = REVERSED_DICT[word]
            print(f"Перевод слова {word} - {translation}")
        else:
            print(f"Нет перевода для слова {word}")
