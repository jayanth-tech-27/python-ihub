# import numpy as np
# A1=np.array([100,2332,3323,232,32,2323,2,987])
# print(A1)
# A2=A1.reshape(4,2)
# print("dimenshions",A2)


# import numpy as np

# A1 = np.array([1, 2, 3, 4, 5, 6, 7])
# A2 = A1.reshape(1, 7)
# print(A2)

class megastar:
    def __init__(self,surname,place):
        self.surname=surname
        self.place=place
    def m1(self):
        print('the surname is ',self.surname)
        print('the place is ',self.place)
class ramcharan(megastar):
    def __init__(self,surname,place,fans,fame):
        super().__init__(surname,place)
        self.fame=fame
        self.fans=fans
    def m2(self):
        super().m1()
        print('the fame was',self.fame)
        print('the fans are',self.fans)
obj=megastar('konidela','hyd')
obj1=ramcharan('konidela','hyd','extractordinary','unmatchable')
obj.m1()
obj1.m2()