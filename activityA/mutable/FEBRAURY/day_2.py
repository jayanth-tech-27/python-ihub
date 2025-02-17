class Parent:
    def m1(self):
        print("the name is ram ")

class Parent_2:
    def m2(self):
        print("the name of parent 2 is")
class Parent_3:
    def m3(self):
        print("the name of parent 3 is kiram kumar reddy")

class Parent4(Parent,Parent_2,Parent_3):
    def m4(self):
        print("the namee is child is parent")

obj=Parent4()
obj.m1()
obj.m2()
obj.m3()
obj.m4()
