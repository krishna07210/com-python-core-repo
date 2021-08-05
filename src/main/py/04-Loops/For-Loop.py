#!/usr/bin/python3
def main():
    fh = open('lines.txt')
    for line in fh.readlines():
        print(line, end='')

    print('\n')
    for line in [1, 2, 3, 4, 5, 6]:
        print(line, end='')

    print('\n')
    for line in 'string':
        print(line)


if __name__ == "__main__": main()
