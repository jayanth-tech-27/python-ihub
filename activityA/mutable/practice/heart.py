# import time 
# L1=eval(input("enter the list values:",))
# print()
# for k1 in L1:
#     print(k1)
# time.sleep(2)
# print("end of code ")

def heart_shape_print():
    for i in range(6):
        for j in range(7):
            if(
                (i==0 and j % 3 !=0)
                or (i ==1 and j % 3 ==0)
                or (i - j == 2)
                or (i + j ==8)
            ):
                print("*",end=" ")
            else:
                print(" ",end=" ")
        print()
if __name__=="__main__":
    heart_shape_print()