class QT:
    def __init__(self):
        print("i am parent class comnstructor")
class IHUB(QT):
    def __init__(self):
        print("i am child class constructor")
obj=IHUB()  
obj1=QT()