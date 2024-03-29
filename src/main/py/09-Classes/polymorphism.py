class Duck:
    def quack(self): print('Quaaack')
    def walk(self): print('Walks like a duck')
    def bark(self): print('The duck cannot bark')
    def fur(self): print('The duck has feathers')

class Dog:
    def bark(self): print('woof!')
    def fur(self): print('The dog has brown and white fur')
    def walk(self): print('Walks like a dog')
    def quack(self): print('The dog cannot quack')

def main():
    donald = Duck()
    fido = Dog()
    in_the_forest(donald)
    in_the_pond(fido)

def in_the_forest(dog):
    dog.bark()
    dog.fur()

def in_the_pond(duck):
    duck.quack()
    duck.walk()

    # for o in (donald,fido):
    #     o.quack()
    #     o.walk()
    #     o.bark()
    #     o.fur()


if __name__ == "__main__": main()
