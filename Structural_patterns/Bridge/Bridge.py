from abc import ABC, abstractmethod


class Pet(ABC):
    def __init__(self, pet_name):
        self.pet_name = pet_name

    @abstractmethod
    def sound(self):
        pass


class Dog(Pet):
    def sound(self):
        return "Гав-гав"


class PetOwner(ABC):
    def __init__(self, pet: Pet):
        self.pet = pet

    @abstractmethod
    def interact(self):
        pass


class DogOwner(PetOwner):
    def interact(self):
        print(f"Я хозяин собаки по кличке {self.pet.pet_name}\nДай голос: - {self.pet.sound()}!")


dog = Dog("Шарик")

dog_owner = DogOwner(dog)

dog_owner.interact()
