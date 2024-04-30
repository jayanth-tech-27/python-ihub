# variable length arguments
def test_case1(*obj1):
    for x1 in obj1:
      print(x1,end='    ')
test_case1()
test_case1(10)
test_case1(10,20)
test_case1(10,20,30)
test_case1(10,20,30,40)
test_case1(10,20,30,40,50)