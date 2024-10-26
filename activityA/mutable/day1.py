# class qt:
#     a = 1
#     _b = 5
#     __c = 7

#     def m1(self):
#         print("The value of a is:", self.a)      # Accessing public attribute
#         print("The value of b is:", self._b)     # Accessing protected attribute
#         print("The value of c is:", self.__c)    # Accessing private attribute

# # Create an instance of the qt class
# obj = qt()

# # Call the m1 method
# obj.m1()

# # Accessing public and protected attributes
# print(obj.a)      # Output: 1
# print(obj._b)     # Output: 5
# print(obj._qt__c)  


# # single inhertance
# class parent:
#     def __init__(self,surname,place):
#         self.surname=surname
#         self.place=place
#     def m1(self):
#         print(self.surname)
#         print(self.place)
# class child(parent):
#     def __init__(self,surname,place,hobbies,studies):
#         super().__init__(surname,place)
#         self.hobbies=hobbies
#         self.studies=studies
#     def m2(self):
#         super().m1()
#         print(self.hobbies)
#         print(self.studies)
# obj=parent("abc","hyd")
# obj=child('abc','hyd','cricket','graduation')
# obj.m2()

# # multiple inhertance
# class parent1:
#     def m1(self):
#         print("the name is parent1 is ram")
# class parent2:
#     def m2(self):
#         print("the name second parennt is jayanth")
# class parent3:
#     def m3(self):
#         print("the name is kanna")
# class child(parent1,parent2,parent3):
#     def m4(self):
#         print("jdjhdj")
# oka=child()
# oka.m1()
# oka.m2()
# oka.m3()
# oka.m4()

# # multilevel
# class grandparent:
#     def m1(self):
#         print("the name surname")
# class parent(grandparent):
#     def m2(self):
#         print('the methjod name ois okay')
# class child(parent):
#     def m3(self):
#         print('the metod name ios okay jhsjdh')
# obj=child()
# obj.m1()
# obj.m2()
# obj.m3()


# abstraction
# from abc import ABC, abstractmethod
# class defence(ABC):
#     @abstractmethod
#     def area(self):
#         pass
#     def weapon(self):
#         print("the weapon used in ak47")
# class army (defence):
#     def area(self):
#         print('okay army')
# class navy(defence):
#     def area(self):
#         print('okay navy')
# obj=army()
# obj.area()
# obj.weapon()
# obj1=navy()
# obj1.area()
# obj1.weapon()


# class qt:
#     def m1(self,*args):
#         if len(args)==1:
#             print("only one passed arraged")
#         elif len(args)==2:
#             print("two values are passed")
#         elif len(args)==3:
#             print("3 valuies are passed")
#         else:
#             print("can be any no of value")
# ob=qt(9,5)
# # ob.m1(8,7,8,97,8,8)
# # ob.m1(5)




# method overloading
# class parent:
#     def m1(self):
#         print('i am parent')
# class child(parent):
#     def m1(self):
#         print('i am child')
# obj=parent()
# obj.m1()
# obj1=child()
# obj1.m1()




class qt:
    def __init__(self):
        print("i am parent class constructor")
class ihub(qt):
    def __init__(self):
        print('i am child class constructor')
obj=qt()
obj1=ihub()