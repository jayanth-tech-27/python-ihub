class parent:
    def m1(self):
        print('i aam parent')
class child(parent):
    def m1(self):
        print("i am child")
obj=child()
obj.m1()
obj1=parent()
obj1.m1()