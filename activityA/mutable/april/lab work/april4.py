# # def sum_even(numbers):

# #   sum = 0

# #   for number in numbers:

# #     if number % 2 == 0:

# #       sum += number

# #   return sum


# # print(sum_even([1, 2, 3, 4, 5, 6, 7, 8, 9, 10]))

# # def sum_even(numbers):
# #     sum=0
# #     for number in numbers:
# #         if number % 2==0:
# #             sum+=number
# #     return sum
# # print(sum_even([1,2,3,4,5,6,7,8,9,10]))

# def divisible_by_3_or_5(numbers):

#   divisible_numbers = []

#   for number in numbers:

#     if number % 3 == 0 or number % 5 == 0:

#       divisible_numbers.append(number)

#   return divisible_numbers


# print(divisible_by_3_or_5([1, 2, 3, 4, 5, 6, 7, 8, 9, 10]))
def divisible_by_3_or_5(numbers):

  divisible_numbers = []

  for number in numbers:

    if number % 3 == 0 or number % 5 == 0:

      divisible_numbers.append(number)

  return divisible_numbers


print(divisible_by_3_or_5([1, 2, 3, 4, 5, 6, 7, 8, 9, 10]))