from functools import reduce

lst = [1, 2, 3]

print(lst)
print(lst[0], lst[-1])
print(lst[1:])
print(lst[1:2])
print(lst[:2])

lst2 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
print(lst2[1:8:2])

print(lst2[::-1])
# lst3 = lst2[::]
lst3 = [*lst2]
lst2.remove(8)
print(lst2)
print(lst3)

lst2_2 = [i * 2 for i in lst2 if i < 4]
print(lst2_2)

print([i * 2 for i in range(10)])

eng_rus_dict = {
    "cat": "кот",
    "car": "машина"
}

eng_rus_dict2 = {
    k.upper(): v[0] for k, v in eng_rus_dict.items()
}
print(eng_rus_dict2)


def a(x):
    return x * 2


b = lambda x: x * 2

print(a(2), b(2))

lst4 = filter(lambda x: x < 4, lst2)
lst4 = map(lambda x: x * 2, lst4)
print(list(lst4))
print(list(range(10)))

print(list(reversed(sorted([3, 5, 2, 1]))))

test_dict = {"a": 5, "b": 3, "d": 8, "c": -1}
print(test_dict)
print(dict(sorted(
    test_dict.items(),
    key=lambda x: x[0]
)))

print(dict(sorted(
    test_dict.items(),
    key=lambda x: x[1]
)))

print(reduce(lambda x, y: x + y, lst2))


def my_generator():
    print('старт генератора')
    i = 1
    while True:
        print('интерация генератора', i)
        i += 1
        yield i ** 2


for i in my_generator():
    print('в цикле', i)
    if i > 10:
        break
