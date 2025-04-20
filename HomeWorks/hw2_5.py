class Animal:
    def __init__(self, name, age):
        self.__name = name
        self.__age = age

    def info(self):
        return print(f'{self.__name} is {self.__age} years old. Birth year: {2025 - self.__age}')

some_animal = Animal('Anim', 2)
print(some_animal.info())