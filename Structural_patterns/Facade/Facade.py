class Authenticator:
    def authenticate_account(self, account_number, pin_code):
        print(f"Вход в личный кабинет по номеру карты {account_number}...")
        return True


class BalanceChecker:
    def check_balance(self, account_number):
        print(f"Проверка баланса по карте {account_number}...")
        return 300


class WithdrawingMoney:
    def withdraw_money(self, amount):
        print(f"Происходит снятие {amount}$")


class ATMFacade:
    def __init__(self):
        self.authenticator = Authenticator()
        self.balance_checker = BalanceChecker()
        self.withdrawing = WithdrawingMoney()

    def interact(self, account_number, pin, amount):
        if self.authenticator.authenticate_account(account_number, pin):
            balance_account = self.balance_checker.check_balance(account_number)
            if balance_account >= amount:
                self.withdrawing.withdraw_money(amount)
                print("Снятие прошло успешно! Поздравляю!")
            else:
                print("К сожалению, у вас недостаточно средств!(")
        else:
            print("Не удалось зайти в личный кабинет(")


atm = ATMFacade()
atm.interact("234532525245", "1111", 200)
