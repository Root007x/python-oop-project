class Shopping:
    cart = [] # Class attribute or static attribute
    origin = "china"
    
    def __init__(self, name,location) -> None:
        self.name = "Jomuna"
        self.location = "Future Park"
        
    def purchase(self,item,price,amount):
        rem = amount - price
        print(f"Money left : {rem}")
    
    @staticmethod
    def add(a,b):
        print(a + b)
        
    @classmethod
    def boss(self):
        print("Boss")
        

Shopping.add(2,5) # static method
Shopping.boss() # Classmethod