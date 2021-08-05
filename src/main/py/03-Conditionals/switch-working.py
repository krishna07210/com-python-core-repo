#!/usr/bin/python3
def main():
    choices = dict(
        one='first',
        two='second',
        three='third'
    )
    v = 'seven'
    print(choices.get(v, 'other'))

    a, b = 0, 1
    v1 = 'this is true' if a < b else 'this is not true'
    print(v1)

if __name__ == "__main__": main()
