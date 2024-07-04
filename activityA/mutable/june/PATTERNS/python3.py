# reverse hill printing
n=int(input('enter the input:'))
for x in range(n):
    print(x*' ',(n-x)*' *')

# # left triangle
n=int(input('enter the input:'))
for x in range(n,0,-1):
    print((n-x)*' ',(x)*'*')


