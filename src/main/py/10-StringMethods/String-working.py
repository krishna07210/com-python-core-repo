def main():
    print('This is a string')
    s = 'This is a string'
    print(s.upper())
    print('This is a string'.upper())
    print('This is a string {}'.format(42))
    print('This is a string %d' % 42)
    print(s.find('is'))
    s1 = '   This is a string  '
    print(s1.strip())
    print(s1.rstrip())
    s2 = '   This is a string\n'
    print(s2.rstrip('\n'))
    print(s.isalnum())
    print('thisisasting'.isalnum())

    a,b =1,3
    print('this is {}, that is {}'.format(a,b))
    s = 'this is {}, that is {}'
    print(s.format(5,9))

    print(s.center(80))

    s1 = 'this is %d, that is %d' % (a,b)
    print(s1 )

    a,b =42,35
    print('this is {}, that is {}'.format(b,a))
    print('this is {1}, that is {0}'.format(b,a))
    print('this is {bob}, that is {fred}'.format(bob=a,fred=b))




if __name__ == "__main__": main()
