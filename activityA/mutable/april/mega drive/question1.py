# 25.Consider both the lists and write the code for expected output:

# l1=["a","b","c","d"]
# l2=[1,2,3,4]

# Expected output:{"a":1,"b":2,"c":3,"d":4}

l1 = [1,23,23231,232]
l2 = [1, 2, 3, 4]

result = dict(zip(l1, l2))
print(result)