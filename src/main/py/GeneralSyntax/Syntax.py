def main():
    print("This is Main Function")
    egg()
    fun(1)
    fun1()


def egg():
    print("egg")
    condition()
    fun(3)


def condition():
    print("Hello")
    a, b = 2, 3
    if a > b:
        print("a > b")
    elif a < b:
        print("a < b")
    else:
        print("a = b")
    s = "less than" if a < b else "not less than"
    print(s)


def fun1(a=0):
    for i in range(a, 10):
        print(i, end=' ')
    print()


def fun(a):
    for i in range(a, 10):
        print(i, end=' ')
    print()


if __name__ == '__main__': main()
