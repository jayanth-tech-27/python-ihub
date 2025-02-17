class Qt:
    def setEid(self,Eid):
        self.Eid=Eid
    def getEid(self):
        return self.Eid
    def setEnum(self,Enum):
        self.Enum=Enum
    def getEnum(self):
        return self.Enum
obj=Qt()
obj.setEid("vanamala")
print(obj.getEid())
obj.setEnum("9948640337")
print(obj.getEnum())