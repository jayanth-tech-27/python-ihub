#reverse of a string and checkout whether the given string is palindrom or not
str1=input("enter the number:")
str2=""
for x1 in str1:
    str2=x1+str2
print(str2)
if (str1==str2):
   print("palindrom")
else:
  print("not palindrom")
