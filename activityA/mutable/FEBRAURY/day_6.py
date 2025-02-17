from abc import ABC,abstractmethod
class Defence(ABC):
    @abstractmethod
    def area(self):
        pass
    def weapon(self):
            print("the weapon used in ak47")

class Army(Defence):
    def area(self):
        print("the place when army fights on hand")
class Navy(Defence):
    def area(self):
        print("the place whenthe navy do on the war")
class Airforce(Defence):
    def area(self):
        print("the place when aiforce wars  airr")

obj=Army()
obj.area()
obj.weapon()
Obj1=Navy()
Obj1.area()
Obj1.weapon()
obj2=Airforce()
obj2.area()
obj2.weapon()
