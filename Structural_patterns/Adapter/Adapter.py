from abc import ABC, abstractmethod


class UsdMoney(ABC):
    rate_usd = 37.11

    @abstractmethod
    def get_amount(self) -> int:
        pass

    @abstractmethod
    def set_amount(self, am: int) -> None:
        pass


class UahMoney(ABC):

    @abstractmethod
    def get_uah_amount(self) -> float:
        pass


class Worker(UsdMoney):
    def __init__(self, am: int) -> None:
        self.amount = am

    def set_amount(self, am: int) -> None:
        self.amount = am

    def get_amount(self) -> int:
        return self.amount


class AdapterMoney(UahMoney):
    def __init__(self, original_amount: UsdMoney):
        self.original_amount = original_amount
        self.amount = self.convert_amount()

    def convert_amount(self) -> float:
        return self.original_amount.get_amount() * UsdMoney.rate_usd

    def get_uah_amount(self) -> float:
        return self.amount


if __name__ == '__main__':
    worker_money = Worker(1500)
    uah_money = AdapterMoney(worker_money)
    print("Зарплата работника в USD: " + str(worker_money.get_amount()))

    print("Зарплата работника в UAH: " + str(uah_money.get_uah_amount()))
    print()
