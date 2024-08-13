class Person:
    
    def __init__(self,name,age,height,weight) -> None:
        self.name = name
        self.age = age
        self.height = height
        self.weight = weight
    
    def eat(self):
        print("I love to eat")
        
    def exercise(self):
        raise NotImplementedError
        

class Cricket(Person):
    def __init__(self,name,age,height,weight,team):
        super().__init__(name,age,height,weight)
        self.team = team
    #Overriding
    def eat(self):
        print("I love chicken Curry")
        
    def exercise(self):
        print("Running")
        
    #overloading
    def __add__(self,other):
        return self.age + other.age
    
    def __mul__(self,other):
        return self.height * other.height
        
player = Cricket("sakib",30,5.5,70,"bd")
player.eat()
player.exercise()

player_2 = Cricket("Musfiq",30,5.6,60,"bd")

print(player + player_2)
print(player * player_2)