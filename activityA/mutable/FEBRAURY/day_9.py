# import re
# pattern=r"^hello"
# text="hello ,world!"
# match=re.match(pattern,text)
# if match:
#     print("pattern found  at the beginiing")
# else:
#     print("pattern not fount ")

# import re
# p=r"world"
# t="hello,world!"
# match=re.search(p, t)
# if match:
#     print("pattern found")
# else:
#     print("pattern not found")

import re 
p=r"is"
t="this is a simple example .is this clear??"
matches=re.findall(p,t)
print(F"Found{len(matches)} occurences:{matches}")