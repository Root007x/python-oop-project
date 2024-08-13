class Vehicle:
    def __init__(self, name, price):
        self.name = name
        self.price = price
        
    def __repr__(self) -> str:
        return f"{self.name} {self.price}"
        
    def move(self):
        pass
    
class Bus(Vehicle):
    def __init__(self,name,price,seat) -> None:
        super().__init__(name = name, price = price)
        self.seat = seat
        
    def __repr__(self) -> str:
        return super().__repr__() + f" {self.seat}"
    
class Truck(Vehicle):
    def __init__(self,name,price,weight) -> None:
        super().__init__(name = name, price = price)
        self.weight = weight
        

class PickupTruck(Truck):
    
    def __init__(self,name, price, weight) -> None:
        super().__init__(name = name,price = price,weight = weight)
        

class ACBus(Bus):
    def __init__(self,name,price,seat,temp):
        super().__init__(name = name, price = price, seat = seat)
        self.temp = temp
        
    def __repr__(self) -> str:
        return super().__repr__() + f" {self.temp}"
        
        
green_line = ACBus("green",500000000,50,25)
print(green_line)
    