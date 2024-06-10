# Базовый класс Animal
class Animal:
    def __init__(self, name, species):
        self.name = name
        self.species = species

    def make_sound(self):
        return "Some generic sound"

    def get_info(self):
        return f"{self.name} is a {self.species}"

# Производный класс Dog, наследующий от Animal
class Dog(Animal):
    def __init__(self, name, breed):
        super().__init__(name, "Dog")
        self.breed = breed

    def make_sound(self):
        return "Bark"

    def get_info(self):
        return f"{self.name} is a {self.breed} breed of dog"

# Тестовая программа для демонстрации работы методов базового и производного классов
def test_program():
    # Создание экземпляра базового класса
    generic_animal = Animal("Generic Animal", "Unknown Species")
    print(generic_animal.get_info())
    print(generic_animal.make_sound())

    # Создание экземпляра производного класса
    my_dog = Dog("Rex", "German Shepherd")
    print(my_dog.get_info())
    print(my_dog.make_sound())

if __name__ == "__main__":
    test_program()
