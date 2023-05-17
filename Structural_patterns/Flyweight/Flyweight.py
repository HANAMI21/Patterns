class CarFlyweight:
    def __init__(self, brand, model, color):
        self._brand = brand
        self._model = model
        self._color = color

    def __str__(self):
        return f"Марка: {self._brand}\nМодель: {self._model}\nЦвет: {self._color}"


class CarFactory:
    def __init__(self):
        self.cars = {}

    def get_car(self, brand, model, color):
        if (brand, model, color) not in self.cars:
            self.cars[(brand, model, color)] = CarFlyweight(brand, model, color)
        return self.cars[(brand, model, color)]


if __name__ == '__main__':
    factory = CarFactory()

    car1 = factory.get_car("BMW", "X6", "Белая")
    car2 = factory.get_car("BMW", "X6", "Белая")
    print("Машина №1:" + str(car1))
    print("Айди обьекта:" + str(id(car1)))

    print()

    print("Машина №2:" + str(car2))
    print("Айди обьекта:" + str(id(car2)))

    print()
    print(factory.cars)
