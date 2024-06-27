class QT:
    def setEid(self,Eid):
        self.Eid=Eid
    def getEid(self):
        return self.Eid
    def setName(self,name):
        self.name=name
    def getName(self):
        return self.name
obj=QT()
obj.setEid(1001)
print(obj.getEid())
obj.setName('jayanth')
print(obj.getName())