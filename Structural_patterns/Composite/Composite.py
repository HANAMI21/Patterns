from abc import ABC, abstractmethod


class Components(ABC):
    @abstractmethod
    def get_cost(self) -> int:
        pass

    @abstractmethod
    def get_name(self) -> str:
        pass


class Product(Components):
    def __init__(self, name: str, cost: int):
        self.name = name
        self.cost = cost

    def get_cost(self) -> int:
        return self.cost

    def get_name(self) -> str:
        return self.name


class CompoundProduct(Components):
    def __init__(self, name: str):
        self.name = name
        self.product_list = []

    def get_cost(self):
        cost = 0
        for el in self.product_list:
            cost += el.get_cost()
        return cost

    def get_name(self) -> str:
        return self.name

    def add_product(self, prod: Components):
        self.product_list.append(prod)

    def remove(self, prod: Components):
        self.product_list.remove(prod)

    def clear(self):
        self.product_list = []


class Cake(CompoundProduct):

    def __init__(self, name: str):
        super(Cake, self).__init__(name)

    def get_cost(self):
        cost = 0
        for it in self.product_list:
            cost_it = it.get_cost()
            print(f"Стоимость '{it.get_name()}' = {cost_it} грн")
            cost += cost_it
        print(f"Стоимость пиццы '{self.get_name()}' = {cost} грн")


if __name__ == '__main__':
    layers = CompoundProduct("Коржи")
    layers.add_product(Product("Яйца", 30))
    layers.add_product(Product("Мука", 60))
    layers.add_product(Product("Мед", 25))

    cream = Product("Крем", 90)

    decorations = CompoundProduct("Украшения")
    decorations.add_product(Product("Berries", 50))
    decorations.add_product(Product("Сhocolate", 40))

    cake = Cake("Медовик")
    cake.add_product(layers)
    cake.add_product(cream)
    cake.add_product(decorations)
    cake.get_cost()
