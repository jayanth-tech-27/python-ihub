import time
S1={1001,1002,1003,1004,1005,1006,1007,1008,1009,1010}
print("==before mutable operations===")
print(S1)
print()
print(type(S1))
print("==after mutable operations===")
S1[0]=2001
S1[1]=2002
print(S1)
print()
print(type(S1))
print()
time.sleep(2)
