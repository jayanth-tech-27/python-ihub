

str1="jayanth"
result=""
for i in range (len(str1)):
    if i % 2==0:
        result+=str1[i].lower()
    else:
        result+=str1[i].upper()
print(result)
