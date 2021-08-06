def main():
    infile = open('olives.jpg', 'rb')
    outfile = open('new.jpg','wb')
    buffersize = 50000
    buffer = infile.read(buffersize)
    while len(buffer):
        outfile.write(buffer)
        print('.',end=' ')
        buffer = infile.read(buffersize)
    print()
    print('Binar File Read Done ..')

if __name__ == "__main__": main()
