class Phone:
    manufecture = "China"

    def __init__(self, brand, price, owner) -> None:
        self.brand = brand
        self.price = price
        self.owner = owner

    def send_sms(self, phone, sms):
        text = f"sending to : {phone} {sms}"
        return text


my_phone = Phone("Sumsung", 1000000, "Hasan")

print(my_phone.owner, my_phone.brand, my_phone.price)

her_phone = Phone("Iphone", 10000, "Mallak")

print(her_phone.owner, her_phone.brand, her_phone.price)
