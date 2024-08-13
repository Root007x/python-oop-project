class Phone:
    price = 1000
    color = "blue"
    brand = "sumsung"
    feature = ["camera", "speaker", "hammer"]


    def call(self):
        print("Calling one person")

    def send_sms(self, phone : int, sms : str):
        text = f"sending SMS to: {phone} and message : {sms}"
        return text


my_phone = Phone()

print(my_phone.feature)
print(my_phone.call())
print(my_phone.send_sms(414,"i miss you"))

