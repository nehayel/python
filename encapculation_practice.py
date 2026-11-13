class BankAccount:
    def __init__(self, name, balance):
        self.name = name
        self.__balance = balance

    def get_balance(self):
        print(f"{self.name}'s balance is {self.__balance}")

    def deposit(self, amount):
        if amount > 0:
            self.__balance += amount
            print(f"Deposited: {amount}")
        else:
            print("Invalid amount")
    def withdraw(self, amount):
        if amount > 0 and amount <= self.__balance:
            self.__balance -= amount
            print(f"Withdred: {amount}")
        else:
            print("Prjapto tk nai")
acount = BankAccount("walid", 5000)

acount.get_balance()

acount.deposit(10340)
acount.get_balance()

acount.withdraw(20000)
acount.get_balance()