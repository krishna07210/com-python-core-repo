def main():
    try:
        fh = open('line.txt')
        for line in fh: print(line.strip())
    except IOError as e:
        print('Could not find the file - ', e)
    except:
        print('Could not find the file.')
    else:
        print('Default ')


if __name__ == "__main__": main()
