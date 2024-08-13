class User:
    def __init__(self,name,age,money):
        self._name = name
        self._age = age
        self.__money = money
    
    # Getter
    @property 
    def age(self): # it become attribute
        return self._age
    
    # getter
    @property
    def salery(self):
        return self.__money
    
    # setter
    @salery.setter # without getter it will not work
    def salery(self,value):
        self.__money += value

samsu = User("Kopa",22,2553535)
#print(samsu.__money)
print(samsu.age)

kasher = User("Halul",24,6666)
kasher.salery = 555

print(kasher.salery)

