a = [1, 2, 2, 2, 1, 2, 2, 3, 3, 3]
b = []
for x in a:
    if x not in b:
        b.append(x) 
print(b)