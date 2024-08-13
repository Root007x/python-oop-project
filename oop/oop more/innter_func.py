def foo():
    print("Foo1")
    
    def inner_foo():
        print("Innter Foo") 
    
    return inner_foo

foo()()

# pass function as parameter

def eat(func):
    print("Iam eating mango")
    func()
    
    
def coding():
    print("I love coding")
    
eat(coding)

# 7.5