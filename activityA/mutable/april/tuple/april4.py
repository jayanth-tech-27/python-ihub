import time
T1=(1001,1002,1003,1004,1005)
print("before immuatable operations===")
print(T1)
print()
print(type(T1))
print()
print("after immutable operations")
T1[0]=200
T1[1]=2001
T1[2]=2003
T1[3]=2004
T1[4]=2005
print(T1)
print()
print(type(T1))
print()
time.sleep(2)
print("end of code")



