# str1=input("enter the string_object:")
# c2=0
# for x1 in range (len(str1)):
#     if(str1[x1]in ("AEIOUaeiou")):
#         c2+=1
#         print("vowela are :",str1[x1])
# print("no of vowels are :",c2)

# c1=0
# for x1 in "software engineering":
#     if(x1 not in ("AEIOUaeiou")):
#         c1+=1
       
# print(c1)

# str1=input("enter the string object:")
# str2=""
# for x1 in str1:
#     str2=x1+str1
# if(str1==str2):
#     print(str1,str2,":given string object is palindrom")
# else:
#     print(str1,str2,":given string object is not a palindrom")

str1=input("enter the string :")
str2=""
for x1 in range(len(str1)):
    str2=str1[x1]+str2
    if(str1==str2):
        print(str1,str2,":given object is palindrom object")
    else:
        print(str1,str2,":given object is not a palindrom object")
