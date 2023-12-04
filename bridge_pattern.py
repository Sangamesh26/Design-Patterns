'''
Bride pattern uml in words be like :
    We have an Interface for abstraction and concrete implementation for this abstraction
    The abstraction interface has another interface that has some concrete classes
    This pattern builds the bridge between two parties let say.
'''
from abc import ABC,abstractmethod

class Car(ABC):
    def __init__(self,name,engine):
        self.name = name
        self.engine = engine
    
    @abstractmethod
    def get_car_details(self):
        pass

class Engine(ABC):
    @abstractmethod
    def details(self):
        pass

class EngineOne(Engine):
    def details(self):
        return "Engine 1"

class EngineTwo(Engine):
    def details(self):
        return "Engine 2"

class Benz(Car):
    def __init__(self,name,engine):
        super().__init__(name,engine)
        
    def get_car_details(self):
        print(f"I am {self.name} with engine {self.engine.details()}")

class Bmw(Car):
    def __init__(self,name,engine):
        super().__init__(name,engine)
    
    def get_car_details(self):
        print(f"I am {self.name} with engine {self.engine.details()}")

class Tata(Car):
    def __init__(self,name,engine):
        super().__init__(name,engine)
    
    def get_car_details(self):
        print(f"I am {self.name} with engine {self.engine.details()}")

if __name__ == "__main__":
    benz = Benz("benz123",EngineOne())
    tata  =Tata("tata098",EngineOne())
    bmw = Bmw("bmw456",EngineTwo())
    
    benz.get_car_details()
    tata.get_car_details()
    bmw.get_car_details()