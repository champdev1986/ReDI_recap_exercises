class BankAccount:
    def __init__(self, balance = 0):
        self.balance = balance

    def deposit(self, amount):
        temporar_balance = self.balance 
        try:
            temporar_balance += amount
        except TypeError as error:
            print("Only numbers can be added to balance")   
        else:                    
            if amount < 0:
                print("Only positive amounts could be deposited")
            else:
                self.balance = temporar_balance
                print("Current balance is: " + str(self.balance))

    def withdraw(self, amount):
        temporar_balance = self.balance
        try:
            temporar_balance -= amount
        except TypeError as error:
            print("Only numbers can be added to balance")   
        else: 
            if temporar_balance < 0:
                print("The balance could not be negative")
            else:
                self.balance -= amount
                print("Current balance is: " + str(self.balance))

my_account = BankAccount(balance=100)
your_account = BankAccount(balance=199)
number = 3

if isinstance(my_account, BankAccount):
    print("my_account is instance of BankAccount") 

if isinstance(your_account, BankAccount):
    print("your_account is instance of BankAccount") 

if isinstance(number, BankAccount):
    print("your_account is instance of BankAccount")

my_account.deposit(100)
my_account.withdraw(50)