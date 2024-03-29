import sys

def main():
    print('Python version {}.{}.{}'.format(*sys.version_info))
    print(sys.platform)

    import os
    print(os.name)
    print(os.getenv('PATH'))
    print(os.getcwd())
    print(os.urandom(25))

    import urllib.request
    page = urllib.request.urlopen('http://bw.org/')
    print(page)
    # for line in page: print(str(line,encodings='utf_8'),end= ' ')

    import random
    x = list(range(25))
    print(x)
    random.shuffle(x)
    print(x)

    import datetime
    now = datetime.datetime.now()
    print(now)
    print(now.year,now.month,now.day,now.hour,now.minute,now.second,now.microsecond)

if __name__ == "__main__": main()
