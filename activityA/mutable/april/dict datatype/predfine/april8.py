# # import time


# # a=5
# # b=20
# # # res=a+b
# # a=25
# # res=a+b
# # print(res)


# str1="bananaz"
# count=0
# for x in str1:
#     if x in "a":
#         count=count+1
# print(count)

# str1 = "cricket"

# # Create a new string to store the result
# result = ""

# # Iterate over the characters in the string
# for i in range(len(str1)):
#     # If the index is even, convert the character to uppercase
#     if i % 2 == 0:
#         result += str1[i].lower()  # Convert to lowercase since the first character should be lowercase
#     # If the index is odd, convert the character to lowercase
#     else:
#         result += str1[i].upper()

# # Print the result
# print(result)
len(str1)  #8
str1="vanamala"
result=""
for i in range(len(str1)):
    if i % 2 == 0:
        result +=str1[i].lower()
    else:
        result+= str1[i].upper()
print(result)