# Creating associative lists with dictionaries
def main():
    print("Associative Lists")
    map = {'one': 1, 'two': 2, 'three': 3, 'four': 4}
    print(map)
    for k in map:
        print(k, map[k])
    print("---Sorted ---- ")
    for k in sorted(map.keys()):
        print(k, map[k])

    d = dict(
        one=1, two=2, three=3, four=4, five=5
    )
    d['seven'] = 7
    for k in sorted(d.keys()):
        print(k, d[k])


if __name__ == '__main__': main()
