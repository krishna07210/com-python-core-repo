def main():
    a = 10
    print(id(a))
    print(type(a))
    print(a)
    a = 20
    print(id(a))
    print(a)
    a = 10
    print(id(a))
    print(a)
    a, b = 0, 1
    print(a == b)
    print(a < b)
    b = True
    print(type(b))
    print(id(b))


if __name__ == '__main__': main()
