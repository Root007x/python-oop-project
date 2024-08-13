

def print_name(first,**karg): # karg act dictionary
    for key,value in karg.items():
        print(f"{key} : {value}")

print_name("Mahadi",last="Hasan",age="24")





