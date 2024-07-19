n=int(input('enter the number:'))
a,b=0,1
for x in range(n):
    a=b
    b=a+b
    print(a,end=' ')

