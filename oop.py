class Cat():
    _count = 0

    def __init__(self, name, weight, color):
        self.__name = name
        self.weight = weight
        self.color = color
        self.fullness = 0
        Cat._count += 1

    def eat(self, fullness=1):
        print(f"{self.__name} поел")
        self.fullness += fullness

    def __str__(self):
        return f'Кот {self.__name}'

    def get_name(self):
        return self.__name

    def set_name(self, name):
        self.__name = name

    @staticmethod
    def get_count():
        return Cat._count


vasya = Cat("Вася", 5, "black")
barsik = Cat("Барсик", 8, "ginger")

# print(vasya.name, vasya.color)
# print(barsik.name, barsik.color, barsik.fullness)
barsik.eat(2)
barsik.eat()
barsik.eat()
print(barsik.fullness)
print(vasya)
vasya.set_name("Вася великолепный")
print(vasya.get_name())

print(Cat.get_count())
