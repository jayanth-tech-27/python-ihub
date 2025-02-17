import re
p=r"a.*z"
t="123abc"
m=re.match(p,t)
if m:
    print("pattern matches")
else:
    print("patterm not found")