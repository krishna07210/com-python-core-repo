# 0505 Aggregating values with lists and tuples
def main():
    x = (1,2,3,4)
    print(type(x),x)

    y = [1,2,3,4,5,6]
    print(type(y),y)
    y.append(7)
    print(type(y),y)
    y.insert(0,0)
    y.insert(4,3.1)
    print(type(y),y)

    s = 'string'
    print(s[0] , s[2:4])

    a = (1,2,3,4)
    for i in a:
        print(i)

    a = 'string'
    for i in a:
        print(i)
if __name__ == '__main__': main()
