# n=int(input())
# for x in range(n):
#     # print((n-x)*' ', x*'*')
#     print((x+1)*'*' , x*' ')


n=int(input("Enter thee number: "))
# for x in range(n):
#     print((n-x)*'*', x*' ')

for x in range(n):
    print((n-x)*" ",x*" *")

for x in range(n):
    print(x*" ",(n-x)*' *')