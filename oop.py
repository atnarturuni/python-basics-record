class Cat():
    _count = 0

    def __init__(self, name, weight, color):
        self.name = name
        self.weight = weight
        self.color = color
        self.fullness = 0
        Cat._count += 1

    def eat(self, fullness=1):
        print(f"{self.name} поел")
        self.fullness += fullness

    def __str__(self):
        return f'Кот {self.name}'

    @staticmethod
    def get_count():
        return Cat._count


vasya = Cat("Вася", 5, "black")
barsik = Cat("Барсик", 8, "ginger")

print(vasya.name, vasya.color)
print(barsik.name, barsik.color, barsik.fullness)
barsik.eat(2)
barsik.eat()
barsik.eat()
print(barsik.fullness)
print(vasya)

print(Cat.get_count())
