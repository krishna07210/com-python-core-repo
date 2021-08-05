import re


def main():
    f = open('word.txt')
    for line in f:
        if re.search('Hari', line):
            print(line, end='')

    for line in f:
        print(re.sub('(Harikrishna)', 'Likith', line), end='')


if __name__ == "__main__": main()
