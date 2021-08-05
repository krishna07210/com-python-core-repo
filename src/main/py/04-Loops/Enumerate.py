#!/usr/bin/python3
def main():
    fh = open('lines.txt')
    for index, line in enumerate(fh.readlines()):
        print(index, line, end='')

    print('\n')
    for i, c in enumerate('this is a string'):
        if c == 's': print('index:{} is an s'.format(i))


if __name__ == "__main__": main()
