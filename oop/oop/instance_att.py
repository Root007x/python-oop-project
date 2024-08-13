class Shop:
    shoppint_mall = "Jamuna Feature Park"

    def __init__(self, buyer):
        self.buyer = buyer
        self.cart = [] # Not shared for all object (Instance attribute)

    def add_to_cart(self,item):
        self.cart.append(item)


person_1 = Shop("Sakib")
person_1.add_to_cart("Egg")
person_1.add_to_cart("Potato")

print(person_1.cart)

person_2 = Shop("Nisho")
person_2.add_to_cart("Banana")
person_2.add_to_cart("Milk")

print(person_2.cart)