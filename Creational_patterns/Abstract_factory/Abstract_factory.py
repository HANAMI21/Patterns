from __future__ import annotations
from abc import ABC, abstractmethod


class CarFactory(ABC):

    @abstractmethod
    def create_body(self) -> Body:
        pass

    @abstractmethod
    def create_engine(self) -> Engine:
        pass


class BMWFactory(CarFactory):
    def create_body(self) -> Body:
        return BMWBody()

    def create_engine(self) -> Engine:
        return BMWEngine()


class MercedesFactory(CarFactory):
    def create_body(self) -> Body:
        return MercedesBody()

    def create_engine(self) -> Engine:
        return MercedesEngine()


class Body(ABC):
    def __init__(self, brand: str):
        self.brand = brand

    @abstractmethod
    def check_body(self):
        pass


"""
Конкретные продукты создаются соответствующими Конкретными Фабриками.
"""


class BMWBody(Body):
    def __init__(self):
        super().__init__("BMW")

    def check_body(self):
        print(f"- Создан кузов для {self.brand}")


class MercedesBody(Body):
    def __init__(self):
        super().__init__("Mercedes")

    def check_body(self):
        print(f"- Создан кузов для {self.brand}")


class Engine(ABC):
    def __init__(self, brand: str):
        self.brand = brand

    @abstractmethod
    def check_engine(self) -> str:
        pass


"""
Конкретные Продукты создаются соответствующими Конкретными Фабриками.
"""


class BMWEngine(Engine):
    def __init__(self):
        super().__init__("BMW")

    def check_engine(self):
        print(f"- Создан двигатель для {self.brand}")


class MercedesEngine(Engine):
    def __init__(self):
        super().__init__("Mercedes")

    def check_engine(self):
        print(f"- Создан двигатель для {self.brand}")


def client_code(factory: CarFactory) -> None:
    body = factory.create_body()
    engine = factory.create_engine()
    body.check_body()
    engine.check_engine()


if __name__ == "__main__":
    """
    Клиентский код может работать с любым конкретным классом фабрики.
    """
    print("Клиентский код работает с фабрикой БМВ:")
    client_code(BMWFactory())

    print()

    print("Клиентский код работает с фабрикой Мерседес:")
    client_code(MercedesFactory())
