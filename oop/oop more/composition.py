class Engine:
    def __init__(self) -> None:
        pass
        
    
    def start(self):
        return "Engine Started"
    
# car `has a` engine
class Car:
    def __init__(self) -> None:
        self.engine = Engine()
        
