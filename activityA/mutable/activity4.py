import time 
L1=['A','B','c']
print("before mutable operations==")
print(L1)
print(type(L1))
print()
print("====after mutable operations ==")
L1[0]="A for apple "
L1[1]="B for ball"
L1[2]="c for cat"
for x1 in L1:
    print(x1)
print(L1)
print()
print(type(L1))
print(" end of code ")