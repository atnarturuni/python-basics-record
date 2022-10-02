import re

text = (
    "Добрый вечер! Меня зовут Василий, моя электронная "
    "почта va-sya_1990@yandex.ru, моя рабочая почта "
    "Vasya@company-2020.com."
)

result = re.finditer(
    r"[\w\d_-]+@[\w\-_\d]+\.\w+", text, re.MULTILINE
)

for item in result:
    print(item.group(0))



text = "03/29/2022"
print(re.sub(r"([0-3]\d)/(\d{2})/(\d{4})", r"\2/\1/\3", text))

result2 = re.search(r"([0-3]\d)/(\d{2})/(\d{4})", text)
print("month", result2.group(1))
print("day", result2.group(2))
print("year", result2.group(3))
