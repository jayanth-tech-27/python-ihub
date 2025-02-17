# def my_decaroator(func):
#     def wrapper():
#         print("something before the functions runs")
#         func()
#         print("something after the function runs")
#     return wrapper
# @my_decaroator
# def say_hello():
#     print("hello world")
# say_hello()

def login_required(f1):
    def inner(name,is_login):
        if is_login==False:
            print("kindly login")
            return
        return f1(name,is_login)
    return inner
@login_required
def home(name,is_login):
    print("welcome to home of our website")

@login_required
def login(name,is_login):
    print("welcone to oders  page of  our website ")

home('user',True) 
login('user',False)