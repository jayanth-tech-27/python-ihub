# l1="121"
# l2=""
# for x in l1:
#     l2=x+l2
# if(l1==l2):
#     print("it is palindrome")
# else:
#     print("it is not a palindrome")



# jayanth = "GeekforGeeks!"
# vowels = "aeiouAEIOU"
 
# count = sum(jayanth.count(vowel) for vowel in vowels)
# print(count)

str2 = str2.lower()

# check if length is same
if(len(str1) == len(str2)):

    # sort the strings
    sorted_str1 = sorted(str1)
    sorted_str2 = sorted(str2)

    # if sorted char arrays are same
    if(sorted_str1 == sorted_str2):
        print(str1 + " and " + str2 + " are anagram.")
    else:
        print(str1 + " and " + str2 + " are not anagram.")