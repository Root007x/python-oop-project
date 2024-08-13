class Shopping:
    def __init__(self,name):
        self.name = name
        self.cart = []
        
    def add_to_cart(self,item,price,quantity):
        product = {"item" : item, "price" : price, "quantity" : quantity}
        self.cart.append(product)
        
    def chackout(self, amount):
        total = 0
        for item in self.cart:
            print(item)
            total += item["price"] * item["quantity"]
        print("Total Price : ",total)
        
        if amount < total:
            return f"please provide {total - amount} more"
        else:
            extra = amount - total
            print(f"Here is your item extra money {extra}")
        


shopon = Shopping("Jacob")
shopon.add_to_cart("alu",50,2)
shopon.add_to_cart("dim",25,6)

print(shopon.cart)

shopon.chackout(1000)