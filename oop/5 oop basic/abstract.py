from abc import ABC, abstractmethod

class Animal(ABC):
    
    @abstractmethod
    def eat(self):
        print("I need Food") # u have to implement same name method child class or it will not work
    
    @abstractmethod
    def move(self): # must implement in child class or it will not work
        pass
    
    
class Monkey(Animal):
    def __init__(self, name) -> None:
        super().__init__()
        self.name = name
        self.category = "Monkey"
    
    def eat(self):
        print("Hey babe, I am eating mango")
        
    def move(self):
        print("Iam running")
        

rk = Monkey("Pombo")
rk.eat()
rk.move()