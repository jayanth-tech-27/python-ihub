class I_HUB_APP_STORE:
    @classmethod
    def m2(cls):
        print("class_method")
i1=I_HUB_APP_STORE()
i1.m2
I_HUB_APP_STORE.m2()



class I_HUB_APP_STORE:
    @staticmethod
    def m3():
     print("static_method")
i1=I_HUB_APP_STORE()
i1.m3()
I_HUB_APP_STORE.m3()