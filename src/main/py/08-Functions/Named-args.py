def main():
    func1(1, 2, 3, 4, 5, 6, 7, 8, one=1, two=2, three=3)
    print(add(1, 2))
    print('\n')
    for i in getRange(5):print(i,end=' ')

def func1(x, y, z, *args, **kwargs):
    print(x, y, z, args)
    print(kwargs['one'], kwargs['two'], kwargs['three'])
    print('\n')
    for k in kwargs: print(k, kwargs[k])


def add(a, b):
    return a + b


def getRange(x):
    return range(x)


if __name__ == "__main__": main()
