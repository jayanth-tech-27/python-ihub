import re
# p=r"^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$"
# email="user@example.com"
# m=re.match(p,email)
# if m:
#     print("valid email address")
# else:
#     print("invalid email address")


p=r"\d{4}-\d{2}-\d{2}"
t="the event is sheduled at te 2025-22-22."
m=re.search(p,t)
if m:
    print(m)
else:
    print("not found")