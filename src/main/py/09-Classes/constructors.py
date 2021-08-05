class Duck:

    def __init__(self, value):
        print('Constructor')
        self._v = value

    def quack(self):
        print('Quaack', self._v)

    def walk(self):
        print('walk like a duck', self._v)


def main():
    donald = Duck(30)
    print(donald)
    donald.quack()
    donald.walk()
    print(donald._v)


if __name__ == "__main__": main()
