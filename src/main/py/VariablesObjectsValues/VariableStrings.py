def main():
    s = "This is a\n String"
    print(s)
    s = r"This is a\n String"
    print(s)
    n = 42
    s = "This is a {} String".format(n)  # Python 3
    print(s)
    s = "This is a %s String" % n  # Python 2
    print(s)
    # \ escapes the new line
    s = '''\
    this is sting 
    \
    line after the line
    '''
    print(s)


if __name__ == '__main__': main()
