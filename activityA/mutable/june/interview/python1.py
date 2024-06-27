#The Fibonacci series in python is a mathematical sequence that starts with 0 and 1, with each subsequent number being the sum of the two preceding ones. In Python, generating the Fibonacci series is not only a classic programming exercise but also a great way to explore recursion and iterative solutions.
a=0
b=1
for i in range(1,10):
    c=a+b
    a=b
    b=c
    print(c,end=' ')

    