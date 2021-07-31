class Demo:
    def __init__(self, kind="Hari"):
        self.kind = kind

    def whatKind(self):
        return self.kind


def main():
    friend = Demo()
    print(friend.kind)
    scrambled = Demo("Likith")
    print(scrambled.kind)


if __name__ == '__main__': main()

