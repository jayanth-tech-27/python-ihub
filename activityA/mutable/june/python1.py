# if(__name__=="__main__"):
#  s1=lambda x:x*x
# print("square of + number is :",s1(6))
# print("square of - number is:",s1(-7))
# print("square of number is ",s1(12.32))


# Example of using lambda with map
# numbers = [1, 2, 3, 4]
# squared = list(map(lambda x: x**2, numbers))
# print(squared) 

# num=[1,2,3,4,5]
# squared=list(map(lambda x: x*x,num))
# print(squared)

# from functools import reduce

# # Example of using lambda with reduce
# numbers = [1, 2, 3, 4]
# sum_result = reduce(lambda x1, x2: x1 + x2, numbers)
# print(sum_result) 

from functools import reduce
numbers=[1,2,3,4]
sum_result=reduce(lambda x1,x2: x1+x2, numbers)
print(sum_result)