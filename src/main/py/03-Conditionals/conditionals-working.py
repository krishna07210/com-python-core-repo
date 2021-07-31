#!/usr/bin/python3

def main():
    a, b = 0, 1
    if False:
        print('this is true')
    else:
        print('it is not true')

    v = 'one'
    if v == 'one':
        print('v is one')
    elif v == 'two':
        print('v is two')
    elif v == 'three':
        print('v is three')
    else:
        print('v is some other thing')


if __name__ == "__main__": main()
