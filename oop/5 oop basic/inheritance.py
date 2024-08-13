# Base class, parent class, common attribute + functiionality
# Derived class, child class, uncommon attribute + functionality

# Parent Class
class Gadget:
    def __init__(self, brand, price, color, origin) -> None:
        self.brand = brand
        self.price = price
        self.color = color
        self.origin = origin
        
    def run(self):
        return f"Running laptop : {self.brand}"
    
# Child class        
class Laptop:
    
    def __init__(self,memory,ssd) -> None:
        self.memory = memory
        self.ssd = ssd
        
    def coding(self):
        return f"Learning python and practicing"
    

class Phone(Gadget):
    def __init__(self,brand,price,color,origin,dual_sim) -> None:
        super().__init__(brand,price,color,origin) # calling constructor from parents class
        self.dual_sim = dual_sim
        
        
    def phone_call(self, number, text):
        return f"Sending SMS to : {number, text}"
    
    def __repr__(self) -> str:
        return f"Phone : {self.brand}, {self.price}, {self.color}, {self.origin}, {self.dual_sim}"
    
    
my_phone = Phone("Iphone", 1000000, "Black", "China", True)
print(my_phone)

# 6.3