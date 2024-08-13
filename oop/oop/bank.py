class Bank:
    def __init__(self, balance):
        self.balance = balance
        self.min_withdraw = 100
        self.max_withdraw = 100000

    def get_balance(self):
        return self.balance
    
    def deposit(self, amount):
        if amount > 0:
            self.balance += amount

    def withdraw(self, amount):
        if amount < self.min_withdraw:
            return f"You can withdraw below {self.min_withdraw}"
        elif amount > self.max_withdraw:
            return f"You can not withdraw more than {self.max_withdraw}"
        else:
            self.balance -= amount
            return f"Here is your money {amount}"

brac = Bank(15000)
print(brac.get_balance())
print(brac.withdraw(5000))
print(brac.get_balance())

# 5.6
