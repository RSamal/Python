

def main():

    import sys
    print "Python version {}.{}.{}".format(*sys.version_info)
    print sys.platform

    import os
    print os.name
    print os.getenv('PATH')
    print os.getcwd()
    print os.urandom(25)

    import urllib
    page = urllib.urlopen("http://www.google.com")
    for line in page:
        print str(line)

    import random
    print random.randint(1,1000)
    x = range(10)
    print x
    random.shuffle(x)
    print x

    import datetime
    now = datetime.datetime.now()
    print now
    print now.year,now.month, now.day

if __name__ == '__main__':
    main()