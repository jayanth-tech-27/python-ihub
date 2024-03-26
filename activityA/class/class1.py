import time
L1=[1001,1002,1003,1004]
L2=[1002,2002,2003,2004]
print("before the operation")
print()
L1.append("1001")
print("after the operation:",L1)
print()
L1.extend(L2)
print()
print("after the operation:",L1)
time.sleep(2)
print("end of code")
