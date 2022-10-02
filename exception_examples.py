import random
import time

dct = {"a": 1}
try:
    print(dct['b'])
except KeyError as e:
    print("ключа не существует", e)

print("111")
#
# try:
#     number = int(input())
#     number2 = int(input())
#     print(number / number2)
# except (ZeroDivisionError, ValueError) as e:
#     print("введены неправильные данные", e)
# except BaseException as e:
#     print("произошла неизвестная ошибка")
#     print(e)
#     print(type(e))

class AppException(Exception):
    pass


class MyException(AppException):
    def __init__(self, message):
        self.message = message

    def __str__(self):
        return self.message


def my_func():
    if random.random() > 0.5:
        raise MyException("test")

for i in range(10):
    print(i)
    try:
        my_func()
    except MyException:
        print("my exception")  # 1 specific app exception
    except AppException:
        print("app exception")  # 2 other app exceptions
    except BaseException:
        print("base exception")  # 3 python exceptions
