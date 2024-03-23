import time 
str1="core Python"
print("===Before Immutable operations===")
print(str1)
print()
print(type(str1))
print()
print("===After immutable operations===")
str1[0]="C"
print(str1)
print()
print(type(str1))
print()
time.sleep(2)
print('End of an application')