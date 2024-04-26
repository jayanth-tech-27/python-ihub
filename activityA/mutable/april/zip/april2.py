L1=["pid","Pname","price","company"]
L2=[1001,"mobile_1",25000,"apple"]
print(L1)
print(L2)
res1=dict(zip(L1,L2))
print(res1)
for x1,x2 in res1.items():
    print(x1,"--",x2)