def login_Required(f1):
    def inner(name,is_login):
        if is_login==False:
            print('kindly login')
            return 
        return f1(name,is_login)
    return inner


@login_Required
def home(name,is_login):
    print('welcome to home page of our website')
@login_Required
def orders(name,is_login):
    print('welcome to orders page of our website')
def about():
    print('welcome to about section of our website')
home('user',True)
orders('user',False)
about()


# exception handling
try:
    x = 5 / 1
    print(x)
except ZeroDivisionError:
    print("You can't divide by zero!")
else:
    print("Yes nice calculation")
finally:
    print("ok")