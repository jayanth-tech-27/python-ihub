import time
D2=dict(Pid=1001,Pname="mobile_1",Price=27100,Company="samsung")
print(D2)
print()
print(type(D2))
print()
print("before operations:",D2)
D3=D2.get("Pid")
print()
print("after operations:",D3)
print()
time.sleep(2)
print("end of code")