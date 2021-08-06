def main():
    # dictionaries
    d = {'one' : 1 , 'two' :2 , 'three' :3}
    print(d , type(d))
    d1 = dict(one=1,two=2,three=3)
    print(d1 , type(d1))

    x = dict(four=4,five=5,six=6)
    d = dict(one=1,two=2,three=3,**x)
    print(d , type(d))

    #methods
    print('four' in d)
    for k in d: print(k,end=' ')
    for k, v in d.items(): print(k,v )

    print(d['three'])
    # print(x['three']) KeyError: 'three'
    print(x.get('three'))
    print(x.get('three','not found'))
    del x['four']
    print(x)
    x.pop('five')
    print(x)

if __name__ == "__main__": main()
