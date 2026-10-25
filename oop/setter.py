class BankAccount:
    def __init__(self, balance):
        self._balance = balance

    def withdraw(self, amount):
        if amount <= 0:
            return "Invalid amount"
        elif amount <= self._balance:
            self._balance -= amount
            return "Amount Withdrawed"
        else:
            return "Insufficient balance"
    def deposit(self,amount):
        if amount <= 0:
            return "Invalid amount"
        else :
            self._balance += amount
            return "Money has been credited to the account"
    @property
    def balance(self):
        return self._balance

    @balance.setter
    def balance(self,new_balance):
        if new_balance < 0:
            raise ValueError("Balance cannot be negative")
        self._balance = new_balance 

acc1 = BankAccount(1000)
print(acc1.withdraw(500))
print(acc1.deposit(3000))
print(acc1.balance)
try:
    acc1.balance = -50
except ValueError as error:
    print(error)
try:
    acc1.balance = 50
except ValueError as error:
    print(error)
print(acc1.balance)