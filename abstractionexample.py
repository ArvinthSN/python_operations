from abc import ABC ,abstractmethod
from collections.abc import async_generator


class AbstractClass(ABC):
    @abstractmethod
    def animalname(self):
        pass
    @abstractmethod
    def animalsound(self):
        pass

class Child_class(AbstractClass):
    def __init__(self,name,sound)->None:
        self.name = name
        self.sound = sound
    def animalname(self)->str:
        return self.name
    def animalsound(self)->str:
        return self.sound

obj = Child_class("cat","MEOW!!")
print(f"{obj.animalname()} sounds as {obj.animalsound()} {obj.animalsound()}")
obj = Child_class("leopard","MEOWwww!!")
print(f"{obj.animalname()} sounds as {obj.animalsound()} {obj.animalsound()}")
obj = Child_class("Goat","BAAAAAAAHh!!!")
print(f"{obj.animalname()} sounds as {obj.animalsound()} {obj.animalsound()}")
obj = Child_class("pig","OINNNNNKk!!")
print(f"{obj.animalname()} sounds as {obj.animalsound()} {obj.animalsound()}")