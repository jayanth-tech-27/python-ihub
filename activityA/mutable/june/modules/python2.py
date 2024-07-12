import numpy as np
A1=np.array([[[[1001,1002,1003,1004,1005],[2001,2002,2003,2004,2005],[23,3,3,2,2],[6,7,7,8,9]]]])
A2=A1.shape
print(A1)
print(A1.ndim)
print(A2)
A2=A1.reshape(20)
print(A2)
