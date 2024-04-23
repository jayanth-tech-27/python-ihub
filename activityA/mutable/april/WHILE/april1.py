# a=0
# str1="Jayanth"
# while(a<len(str1)):
#     print(str1[a])
#     a+=1
# print("end of code")

# for x in "Jayanth":
#     print(x)

# for x in range(1,10):
#     print(x)

# i=0
# while(i<10):
#     print(i)
#     i+=1

#1 to 50 even numbers----->100,odd numbers--->75
# even_number=[]
# odd_number=[]
# for x in range(1,51):
#     if x%2==0:
#         x1=x+100
#         even_number.append(x1)
#     else:
#         x1=x+75
#         odd_number.append(x1)
# print(even_number)
# print(odd_number)



even_number=[]
odd_number=[]
i=0
while(i<51):
    if i%2==0:
        i1=i+100
        even_number.append(i1)
    else:
        i1=i+75
        odd_number.append(i1)
    i+=1
print(even_number)
print(odd_number)



