# single inhertance 
class Parent:
    def __init__(self,surname,land) :
        self.surname=surname
        self.land=land
    def m1(self):
        print("the surname is vanamala",self.surname)
        print("the place was inherited",self.land)
class Child(Parent):
    def __init__(self, surname, land,cash,gold):
        super().__init__(surname,land)
        self.cash=cash
        self.gold=gold
    def m2(self):
        super().m1()
        print("thecahs was also inherited ",self.cash)
        print("the gold was inherted ",self.cash)
obj=Parent("vanamala","palmoil ")
Obj1=Child("vanamala","palmoil","12211","12grams")
Obj1.m2()
      

