class Parent:
    def m1(self):
        print("this is the grand parent")
class Parent1(Parent):
    def m2(self):
        print("the name of part is syam")
class Parent2(Parent1):
    def m3(self):
        print("this is vanamala")
class Child(Parent2):
    def m4(self):
        print("grand child")
obj=Child()
obj.m1()
obj.m2()
obj.m3()
obj.m4()