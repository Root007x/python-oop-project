class Shop:
    cart = [] # shared for all object (Class attribute)
    def __init__(self, buyer) -> None:
        self.buyer = buyer

    def add_to_cart(self, item) -> None:
        self.cart.append(item)


person_1 = Shop("Sakib")
person_1.add_to_cart("Egg")
person_1.add_to_cart("Potato")

print(person_1.cart)

person_2 = Shop("Nisho")
person_2.add_to_cart("Banana")
person_2.add_to_cart("Milk")

print(person_2.cart)