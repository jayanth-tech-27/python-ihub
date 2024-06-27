# multple inheritance
class parent1:
    def m1(self):
        print('the name is')
class parent2:
    def m2(self):
        print('the parent 2')
class parent3:
    def m3(self):
        print('the parent 3')
class child(parent1,parent2,parent3):
    def m4(self):
        print('the name of the child')
obj=child()
obj.m1()
obj.m2()
obj.m3()