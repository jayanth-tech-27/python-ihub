def test_case1(*obj1):
    s2=0
    for x1 in obj1:
        s2=s2+x1
    print("sum of any no of arguments:",s2)
test_case1()
test_case1(10)
test_case1(10,20)
test_case1(10,20,30)
test_case1(10,20,30,40)
test_case1(10,20,30,40,50)
