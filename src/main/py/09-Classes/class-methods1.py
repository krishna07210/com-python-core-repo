class Duck:

    def __init__(self, color='white'):
        self._color = color

    def quack(self):
        print('Quaaack', self._color)

    def walk(self):
        print('walk like a duck', self._color)

    def set_color(self, color):
        self._color = color

    def get_color(self):
        return self._color


def main():
    donald = Duck('blue')
    donald.walk()
    donald.set_color('green')
    print(donald.get_color())


if __name__ == "__main__": main()
