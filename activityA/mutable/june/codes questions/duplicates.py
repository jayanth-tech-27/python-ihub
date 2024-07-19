l1=[1,2,1,2,1,4,5,43,8,3,4,3,3,3]
l2=[]
for x in l1:
    if x not in l2:
        l2.append(x)
print(l2)
