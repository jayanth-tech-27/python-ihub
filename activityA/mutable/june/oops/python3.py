class QT:
    def __init__(self,*args):
        if len(args)==3:
            print('value 3')
        elif len(args)==6:
            print("six value")
        elif len(args)==1:
            print("one of bvalue")
        else:
            print('may be aany bvakleiu')
obj1=QT(7,3)