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

i=0
e=[]
o=[]
while(i<51):
    if i%2==0:
        i1=i+100
        e.append(i1)
    else:
        i1=i+75
        o.append(i1)
    i+=1
print(e)
print(o)

L1=[3001,3002,3003,3004,3005,3001,3002]
L2=[]
a=0
while(a<len(L1)):
    if(L1[a] not in L2):
        L2.append(L1[a])
    a+=1
    print("before :",L1)
    print("after operator ",L2)
