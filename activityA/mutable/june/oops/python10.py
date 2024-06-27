#encapsulation one error
class QT:
    a=10 
    _b=20    #protected
    __c=30   #private
def m1(self):
    print('the vale of ',self.a)
    print('the value of',self._b)
    print('the value of ',self.__c)
obj=QT()
obj.m1()
print(obj.a)
print(obj._b)
print(obj.__c)
print(obj._QT__c)#name mangily with name mangily we can access the private variable outside the class

#another method
class QT:
    def setEid(self,Eid):
        set.Eid= Eid
    def getEid(self):
        return self.Eid