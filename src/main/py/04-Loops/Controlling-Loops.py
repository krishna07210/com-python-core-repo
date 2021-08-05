#!/usr/bin/python3
def main():
    s = 'this is a string'

    for i in s:
        if i == 's': continue
        print(i, end='')

    print('\n')
    for i in s:
        if i == 's': break
        print(i, end='')

    print('\n')
    for c in s:
        print(c, end='')
    else:
        print('loop completed')

    print('\n')
    i = 0
    while (i < len(s)):
        print(s[i], end='')
        i += 1
    else:
        print(" -condition false")


if __name__ == "__main__": main()
