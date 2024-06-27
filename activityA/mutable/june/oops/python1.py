class QT:
    def __init__(self,a):
        self.a=a
    def __add__(self,b):
        return self.a+b.a
    def __sub__(self,c):
        return self.a-c.a
    def __mul__(self,d):
        return self.a*d.a
    def __truediv__(self,e):
        return self.a/e.a
obj=QT(10)
obj1=QT(20)
print(obj/obj1)


