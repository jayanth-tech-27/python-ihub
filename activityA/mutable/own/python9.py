# def sum(a,b):
#     c=a+b
#     print(c)
# x=10
# y=15
# sum(x,y)


# def sub(x,y):
#     print(x-y)
# sub(10,20)

def add(*args):
    sum1=0
    for x in args:
        sum1+=x
        print(sum1)