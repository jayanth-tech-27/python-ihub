#SINGLE INHERTANCE
class parent:
    def __init__(self,surname,place):
        self.surname= surname
        self.place=place
    def m1(self):
        print("the surname is ",self.surname)
        print("the place is ",self.place)
class child1(parent):
    def __init__(self,surname,place,hobbies,studies):
            
            super().__init__(surname,place)
            self.hobbies=hobbies
            self.studies=studies
    def m2(self):
            super().m1()
            print("the hobbies of child",self.hobbies)
            print('the studeues is',self.studies)
class child2(child1):
    def __init__(self,surname,place,hobbies,studies):
          
          super().__init__(surname, place,hobbies,studies)
          
    def m3(self):
          super().m2()
          print('the hobbies of child',self.hobbies)
          print('the studies is ',self.studies)
class child3(child2):
    def __init__(self, surname, place, hobbies, studies,sports):
          super().__init__(surname, place,hobbies,studies)
          self.sports = sports
          
    def m4(self):
          super().m3()
          print('the hobbies of child',self.hobbies)
          print('the studies is ',self.studies)   
          print('the sports is ',self.sports)   
object=parent('abc','hyd')
object1=child1('abc','hyd','cricket','sdfgwrg')
object1.m2()
print()
print()
object2 = child2('abc2','hyd2','cricket2','ahyecgf2')
object2.m3()
object3=child3('abc1','hyd1','cricket1','ahyecgf1','football')
object3.m4()