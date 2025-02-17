import re
# p=r"\d"
# t="123abc"
# matches=re.findall(p,t)
# print(matches)

# p=r"cat|dog"
# t="i have a cat and dog"
# m=re.findall(p,t)
# print(m)

p=r"(\d{3})-(\d{2})-(\d{4})"
t="my number is 123-46-7890"
m=re.search(p,t)
if m:
    print(m.group(1))
    print(m.group(2))