#SINGLE INHERTANCE
class parent:
    def __init__(self,surname,place):
        self.surname= surname
        self.place=place
    def m1(self):
        print("the surname is ",self.surname)
        print("the place is ",self.place)
class child(parent):
        def __init__(self,surname,place,hobbies,studies):
            super().__init__(surname,place)
            self.hobbies=hobbies
            self.studies=studies
        def m2(self):
            super().m1()
            print("the hobbies of child",self.hobbies)
            print('the studeues is',self.studies)
class child2(parent):
     def __init__(self, surname, place,hobbies,studies):
          super().__init__(surname, place)
          self.hobbies=hobbies
          self.studdies=studies
     def m3(self):
          super().m1
          print('the hobbies of child',self.hobbies)
          print('the studies is ',self.studdies)
object=parent('abc','hyd')
object1=child('abc','hyd','cricket','sdfgwrg')
object1.m2()
object2 = child2('abc','hyd','cricket','ahyecgf')
object2.m3()