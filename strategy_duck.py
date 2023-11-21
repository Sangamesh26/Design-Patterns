from abc import ABC,abstractmethod
class FlyBehaviour(ABC):
    @abstractmethod
    def Fly(self):
        pass
    
class FlyStrategyA(FlyBehaviour):
    def Fly(self):
        print("Fly behaviour A")
        
class FlyStrategyB(FlyBehaviour):
    def Fly(self):
        print("Fly behaviour B")

class FlyStartegyC(FlyBehaviour):
    def Fly(self):
        print("Fly behaviour C")

class EatBehaviour(ABC):
    @abstractmethod
    def Eat(self):
        pass

class EatBehaviourA(EatBehaviour):
    def Eat(self):
        print("Eat behaviour A")

class EatBehaviourB(EatBehaviour):
    def Eat(self):
        print("Eat behavior B")
        
class PersonBehaviour(ABC):
    def FlyBehaviour(self):
        pass
    
    def EatBehaviour(self):
        pass

class PersonSangamesh(PersonBehaviour):
    def FlyBehaviour(self):
        return FlyStrategyB()
    
    def EatBehaviour(self):
        return EatBehaviourA()

class PersonVarun(PersonBehaviour):
    def FlyBehaviour(self):
        return FlyStrategyA()
    def EatBehaviour(self):
        return EatBehaviourA()

if __name__ == "__main__":
    varun = PersonVarun()
    varun.FlyBehaviour().Fly()
    varun.EatBehaviour().Eat()
    
    sangamesh = PersonSangamesh()
    sangamesh.FlyBehaviour().Fly()
    sangamesh.EatBehaviour().Eat()  