def main():
    try:
        for line in readfile('line.txt1'): print(line.strip())
    except IOError as e:
        print('Could not find the file: ', e)
    except  ValueError as e:
        print('bad filename: ',e)


def readfile(filename):
    if filename.endswith('.txt'):
        fh = open(filename)
        return fh.readlines()
    else:
        raise ValueError('Filename must end with .txt')


if __name__ == "__main__": main()
