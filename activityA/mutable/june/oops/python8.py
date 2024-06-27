# #single inheritance
# class parent:
#     def __init__(self,surname,place):
#         self.surname=surname
#         self.place=place
#     def m1(self):
#         print("'the name is",self.surname)
#         print('the palce is',self.place)
# class child(parent):
#     def __init__(self, surname, place,hobbies,studies):
#         super().__init__(surname, place)
#         self.hobbies=hobbies
#         self.studies=studies
#     def m2(self):
#         super().m1()
#         print('the hobbies',self.hobbies)
#         print('the studies',self.studies)
# obj=parent('abc','hyd')
# obj1=child('abc','hyd','cricket','tenth')
# obj1.m2()


#multilevel inhertance
# class parent:
#     def __init__(self,surname,place):
#         self.surname=surname
#         self.place=place
#     def m1(self):
#         print("the name is ",self.surname)
#         print('the place is ',self.place)
# class child1(parent):
#     def __init__(self, surname, place,studies):
#         super().__init__(surname, place)
#         self.studies=studies
#     def m2(self):
#         super().m1()
#         print('studies',self.studies)
# class child2(child1):
#     def __init__(self, surname, place, studies):
#         super().__init__(surname, place, studies)
#     def m3(self):
#         super().m2()
# obj=parent('abc','hyd')
# obj1=child1('abc','hyd','cricket')
# obj2=child2('abc','hyd','cricket')
# obj1.m2()
# obj1.m1()


class QT:
    location = 'Ameerpet'
    def __init__(self,fees):
        self.fees = fees
    def m1(self):
        print("The value of a is: ",self.fees)
        print("The location of QT is :",self.location)
        print("The location of QT is(with class inside) :",QT.location)
obj = QT(1234)
obj.m1()
print("The location of QT is (with obj) :",obj.location)
print("The location of QT is (with class name):",QT.location)