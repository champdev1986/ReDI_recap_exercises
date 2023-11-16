class BankAccount:
    def __init__(self, account_number, balance):
        self._account_number = account_number
        self._balance = balance

    def _calculate_interest(self, interest):
        return self._balance*interest/100

class Savings(BankAccount):
    def __init__(self, account_number, balance):
        super().__init__(account_number, balance)
        self._INTEREST = 3.5

class Current(BankAccount):
    def __init__(self, account_number, balance):
        super().__init__(account_number, balance)
        self._INTEREST = 1.5

class Customer:
    def __init__(self, name):
        self._name = name
        self._accounts: list(BankAccount) = list()

    def get_name(self):
        return self._name
    
    def get_info(self):
        accounts = ""
        for account in self._accounts:
            accounts += f"{account._account_number}, "
        return f"{self._name}: {accounts}"