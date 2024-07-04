i=65
n=int(input('enter the no of rows:'))
for x in range(1,n):
    for y in range(x):
        print(chr(i),end=' ')
        i+=1
    print()
    i=65