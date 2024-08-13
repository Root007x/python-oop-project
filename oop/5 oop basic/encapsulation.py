# Encapsulation -> Hide details
# Access Modifier -> private, protected, public

class Bank:
    def __init__(self,holder_name, initial_deposit) -> None:
        # Public
        self.holder_name = holder_name
        self.initial_deposit = initial_deposit # i can modify initial deposit so it is riskey
        # Private
        self.__initial_deposit = initial_deposit
        # Protected
        self._branch = "Dhaka" # it is only convension
        
    def deposit(self, amount):
        self.__initial_deposit += amount
        
    def get_balance(self):
        return self.__initial_deposit
        
        
rafsan = Bank("Choto Vhai", 100000)

print(rafsan.holder_name)
# print(rafsan.__initial_deposit)

rafsan.deposit(5000)
print(rafsan.get_balance()) 

print(rafsan._Bank__initial_deposit) # forcefully access