# list1=["my","name","key","ls"]
# list2=["y","s","silly"]
# list3=(zip(list1,list2))
# print(list3)

list1 = ["M", "na", "i", "Ke"] 
list2 = ["y", "me", "s", "lly"]
list3 = [i + j for i, j in zip(list1, list2)]
print(list3)


list1 = ["Hello ", "take "]
list2 = ["Dear", "Sir"]
list3=[i + j for i,j in zip(list1,list2)]
print(list3)