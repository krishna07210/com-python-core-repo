class Duck:

    def __init__(self, **kwargs):
        self._color = kwargs.get('color', 'white')

    def quack(self):
        print('Quaaack', self._color)

    def walk(self):
        print('walk like a duck', self._color)

    def set_color(self, color):
        self._color = color

    def get_color(self):
        return self._color


def main():
    donald = Duck(color='blue')
    print(donald.get_color())
    donald = Duck()
    print(donald.get_color())


if __name__ == "__main__": main()
