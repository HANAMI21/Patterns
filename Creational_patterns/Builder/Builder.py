from abc import ABC, abstractmethod


class Pizza:
    def __init__(self):
        self.dough = None
        self.sauce = None
        self.toppings = []

    def set_dough(self, dough):
        self.dough = dough

    def set_sauce(self, sauce):
        self.sauce = sauce

    def set_toppings(self, topping):
        self.toppings.append(topping)

    def __str__(self):
        return f"Тесто: {self.dough}\nСоус: {self.sauce}\nНачинки: {self.toppings}"


class PizzaCook(ABC):
    @abstractmethod
    def cook_pizza(self):
        pass

    @abstractmethod
    def add_dough(self):
        pass

    @abstractmethod
    def add_sauce(self):
        pass

    @abstractmethod
    def add_toppings(self):
        pass

    @abstractmethod
    def get_pizza(self):
        pass


class PepperoniPizzaCook(PizzaCook):
    def __init__(self):
        self.pizza = None

    def cook_pizza(self):
        self.pizza = Pizza()

    def add_dough(self):
        self.pizza.set_dough('Тонкое')

    def add_sauce(self):
        self.pizza.set_sauce('Томатный')

    def add_toppings(self):
        self.pizza.set_toppings('сыр Моцарелла')
        self.pizza.set_toppings('Пеперони')

    def get_pizza(self):
        return self.pizza


class MargaritaPizzaCook(PizzaCook):
    def __init__(self):
        self.pizza = None

    def cook_pizza(self):
        self.pizza = Pizza()

    def add_dough(self):
        self.pizza.set_dough('Толстое')

    def add_sauce(self):
        self.pizza.set_sauce('Томатный')

    def add_toppings(self):
        self.pizza.set_toppings('сыр Моцарелла')
        self.pizza.set_toppings('Базилик')

    def get_pizza(self):
        return self.pizza


class Director:
    def __init__(self, pizza_cook):
        self.pizza_cook = pizza_cook

    def construct_pizza(self):
        self.pizza_cook.cook_pizza()
        self.pizza_cook.add_dough()
        self.pizza_cook.add_sauce()
        self.pizza_cook.add_toppings()

    def get_result(self):
        return self.pizza_cook.get_pizza()


if __name__ == '__main__':
    margarita_cook = MargaritaPizzaCook()
    pepperoni_cook = PepperoniPizzaCook()

    director = Director(margarita_cook)
    director.construct_pizza()
    pizza = director.get_result()
    print(f'Пицца Маргарита:\n{pizza}')

    print()

    director = Director(pepperoni_cook)
    director.construct_pizza()
    pizza = director.get_result()
    print(f'Пицца Пепперони:\n{pizza}')
