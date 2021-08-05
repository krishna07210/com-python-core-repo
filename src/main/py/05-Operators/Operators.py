#!/usr/bin/python3
def main():
    print('Add -', 5 + 5)
    print('Multi -', 5 * 5)
    print('Sub -', 5 - 3)
    print(5 / 3)
    print(5 // 3)
    print(5 % 3)
    print(divmod(5, 3))
    num = 5
    num += 1
    print(num)

    x, y = 4, 5
    print(id(x), id(y))
    print(x is y)
    print(x is not y)
    x = 5
    print(id(x), id(y))
    print(x is y)

    print('Booleans')
    print(True and False)
    print(True and True)
    print(True or False)
    print(False and False)
    print(False or False)

    print('----')
    a, b = 0, 1
    x, y = 'zero', 'one'
    print(x < y)
    if a < b and x < y:
        print('yes')
    else:
        print('no')


if __name__ == "__main__": main()
