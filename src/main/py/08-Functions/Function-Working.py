def main():
    fun1()
    fun2()
    testfunc(10, 3)
    testfunc(10)
    testfunc1(1,2,3,4,5,6,7,8)


def fun1():
    print("Hello")


def fun2():  # IndentationError: expected an indented block without body
    pass


def testfunc(x, y=None, z=75):
    if y is None : y =112
    print('This is a test function x y z ', x, y, z)

def testfunc1(x, y=None, z=75, *args):
    if y is None : y =112
    print('This is a test function x y z ', x, y, z,args)
    for i in args: print(i,end=' ')


if __name__ == "__main__": main()
