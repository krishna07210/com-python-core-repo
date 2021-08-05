class Duck:

    def __init__(self, **kwargs):
        self.variables = kwargs

    def quack(self):
        print('Quaaack')

    def walk(self):
        print('walk like a duck')

    def set_variable(self, k, v):
        self.variables[k] = v

    def get_variable(self, k):
        return self.variables.get(k, None)


def main():
    donald = Duck(feet=2)
    print(donald.get_variable('feet'))
    donald.set_variable('color','white')
    print(donald.get_variable('color'))


if __name__ == "__main__": main()
