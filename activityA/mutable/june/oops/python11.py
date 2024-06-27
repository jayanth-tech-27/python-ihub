#abstraction
from abc import ABC, abstractmethod
class defence(ABC):
    @abstractmethod
    def area(self):
        pass
    def weapon(self):
        print("the weapon used in war is ak47")
        pass
    def model(self):
        print('mpdel is')
class army(defence):
    def area(self):
        print("the place when army fights on hand")
class navy(defence):
    def area(self):
        print("the place whejn navy")
class airforce(defence):
    def area(self):
        print("the plaace of airforce")

obj=army()
obj.area()
obj.weapon()
obj.model()
obj1=navy()
obj1.area()
obj1.weapon()
obj1.model()
obj2=airforce()
obj2.area()
obj2.weapon()
obj2.model()