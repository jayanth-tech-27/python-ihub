class Qt:
    def __init__(self,a):
        self.a=a
    def __add__(self,b): 
        return self.a+b.a
    def __sub__(self,c):
        self.c=c
    def __mul__(self,d):
        return self.a*d.a
obj=Qt(10)
obj1=Qt(20)
print(obj+obj1)
print(obj-obj1)
print(obj*obj1)