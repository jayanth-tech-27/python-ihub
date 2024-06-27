class QT:
    def m1(self,*args):
        if len(args)==1:
            print("only one variable has arranged")
        elif len(args)==2:
            print("two values passed")
        elif len(args)==10:
            print("10 values args passed ")
        else:
            print("canbe any num of value")
obj=QT(1)
obj=QT(3,4)