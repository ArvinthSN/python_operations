from abc import ABC , abstractmethod
class animal(ABC) :
    def __init__(self,animal) :
        self.animal = animal
    @abstractmethod
    def sound(self):
       pass
class leopard(animal):
    def __init__(self,animal,soun):
        self.soun = soun
        super().__init__(animal)
    def sound(self):
        print(f"{self.animal} sounds like {self.soun}")
        
        
class dog(animal):
    def __init__(self,animal,soun):
        self.soun = soun
        super().__init__(animal)
        
    def sound(self):
        print(f"{self.animal} sounds like {self.soun}")
        
        



dogobj = dog("dog","bark")
print(dogobj.sound())