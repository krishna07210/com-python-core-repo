class Duck:
    def quack(self):
        print('Quaack')

    def walk(self):
        print('walk like a duck')


def main():
    donald = Duck()
    print(donald)
    donald.quack()
    donald.walk()


if __name__ == "__main__": main()
