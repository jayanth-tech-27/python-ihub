#encapsulation
class QT:
    a=10    #public
    _b=20    #protected
    __c=30   #private
    def m1(self):
        print("the value of a is:",self.a)
        print("the value of b",self._b)
        print("the value of c",self.__c)
obj=QT()
obj.m1()
print(obj.a)
print(obj._b)
print(obj.__c)
print(obj._QT__c)#name mangliy 