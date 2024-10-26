num=11
if num>1:
   for  i in range(2,(num//2)+1):
    if(num%i)==0:
        print(num,'it is not a prime')
    else:
        print(num,'it is prime')
