class Animal():
    _count = 0

    def __init__(self, name, weight, color):
        self.__name = name
        self.weight = weight
        self.color = color
        self.fullness = 0
        Animal._count += 1

    def eat(self, fullness=1):
        print(f"{self.__name} поел")
        self.fullness += fullness

    def __str__(self):
        return f'Животное {self.__name}'

    def get_name(self):
        return self.__name

    def set_name(self, name):
        self.__name = name

    def say(self):
        print(f'{self.__name} говорит!')

    @staticmethod
    def get_count():
        return Cat._count


class Cat(Animal):
    def __str__(self):
        return f'Кот {self.get_name()}'

    def say(self):
        print(f'{self.get_name()}: мяу!')

    def mur(self):
        print(f'{self.get_name()}: мур!')


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
vasya.say()
vasya.mur()

print(Cat.get_count())

parrot = Animal("Кеша", 3, "red")
print(parrot)
parrot.say()


class Device():
    def __init__(self, name):
        self.name = name

    def __str__(self):
        return self.name


class Phone(Device):
    def make_a_call(self, phone_number):
        print(f"Звоним на {phone_number}")

    def take_a_photo(self):
        print(f"{self.name}: фотография!")


class PhotoCamera(Device):
    def take_video(self):
        print('записывает видео')

    def take_a_photo(self):
        print(f"{self.name}: фотография!")


objs = [Phone("samsung"), PhotoCamera("canon")]
for obj in objs:
    obj.take_a_photo()
