def main():
    # touple
    t = 1,2,3,4,5
    print(type(t))
    print(t)
    print(t[0] , t[4],t[-1],t[-2],len(t))
    print(min(t),max(t))
    t =(1,2,3,4)
    print(t)
    print(type(t))

    #List

    l = [1,2,3,4,5]
    print(l)
    print(type(l))
    print(l[0] , l[4],l[-1],l[-2],len(l))

    t1 = tuple(range(10))
    print(t1)
    l1 = list(range(10))
    print(l1)
    l1[5] =42
    print(l1)
    l1.extend(range(20))
    print(l1)
    l1.insert(0,22)
    print(l1)
    l1.remove(0)
    print(l1)
    del l1[12]
    print(l1)
    print(l1.pop())
    print(l1)
    print(l1.pop(2))
    print(l1)
if __name__ == "__main__": main()
