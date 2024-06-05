t1=(11,22)
t2=(99,55)
t1,t2=t2,t1
print(t1)
print(t2)

t1=(11,22,33,55,77,99)
print(t1.count(55))

def check(t):
    return all(t1 == t[0] for i in t)
t1=(45,45,45,45,45)
print(check(t1))

