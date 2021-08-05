#!/usr/bin/python3
def main():
    list = []
    list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    print(list[0])
    print(list[9])
    print(list[0:5])
    for i in range(0, 10):
        print(i, end=' ')
    print('\n')
    print(list)
    list[:] = range(100)
    print(list[22:42])
    print(list[22:42:2])

    list[27:43:3] = (99, 99, 99, 99, 99, 99)
    print(list)


if __name__ == "__main__": main()
