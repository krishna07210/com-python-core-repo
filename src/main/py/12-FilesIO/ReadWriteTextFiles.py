def main():
    f = open('lines.txt', 'r')
    for line in f:
        print(line, end=' ')

    # readlines()'
    # for line in f.readlines():
    #     print(line, end=' ')

    infile = open('lines.txt', 'r')
    outfile = open('new.txt', 'w')
    for line in infile:
        print(line, file=outfile, end=' ')
    print('Done..!')

    # Large files
    largeFileprocess()

def largeFileprocess():
    buffersize = 50000
    inbigfile = open('bigfile.txt', 'r')
    outbigfile = open('new.txt', 'w')
    buffer = inbigfile.read(buffersize)
    while len(buffer):
        outbigfile.write(buffer)
        print('.', end=' ')
        buffer = inbigfile.read(buffersize)
    print()
    print('Large File process Done..!')


if __name__ == "__main__": main()
