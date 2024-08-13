# Poly -> Many
# Morph -> shape


class Animal:
    def __init__(self,name):
        self.name = name
        
    def make_sound(self): # Default
        print("Animal Making Sound")
        

class Cat(Animal):
    def __init__(self, name):
        super().__init__(name)
        
    def make_sound(self): # same parents method name but different machanism
        print("Mew Mew")
        
class Dog(Animal):
    def __init__(self, name):
        super().__init__(name)
        
    def make_sound(self): # if we don't implement this methiod it will call defalut method
        print("ghew ghew")
        
        
cat = Cat("Mofasa")
cat.make_sound()

don = Dog("Tom")
don.make_sound()