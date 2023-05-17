from abc import abstractmethod, ABC
import copy


class Prototype(ABC):
    @abstractmethod
    def clone(self):
        pass


class Car(Prototype):
    def __init__(self, brand, model, color, transmission):
        self.brand = brand
        self.model = model
        self.color = color
        self.transmission = transmission

    def __str__(self):
        return f"- Brand: {self.brand}\n- Model: {self.model}\n- Color: {self.color}\n- Transmission: {self.transmission}"

    def clone(self):
        return type(self)(self.brand, self.model, self.color, self.transmission)


if __name__ == '__main__':
    print("Car number 1:")
    car1 = Car("BMW", "X5", "black", "Manual")
    print(car1)

    print("\nCar number 2:")
    car2 = car1.clone()
    car2.transmission = "Automatic"
    car2.color = "white"
    print(car2)
