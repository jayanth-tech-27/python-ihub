# # T1=(1001,1002,1003,1004,1005)
# # print(T1)
# # print(max(T1))
# # print(len(T1))


# # for x in range(10):
# #     print("software employee")
# L1=input("enter the list_data",)
# L2=input("enter the list_data",)
# print(L1)
# x1=L1==L2
# x2=L1!=L2
# print(x1)
class QT:
    def m1(self, *args):
        if len(args) == 1:
            print("only one variable")
        elif len(args) == 2:
            print("two")
        elif len(args) == 10:
            print("10 ten values")
        else:
            print("can be any number of values")
obj = QT()
obj.m1(2)  
obj.m1(3,4)  
obj.m1(10) 
obj.m1(10, 20, 30, 40, 50, 60, 70, 80,9,0)  
obj.m1(6, 7, 8, 9)  
