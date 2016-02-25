# This is  string substitute example using regex
from __future__ import print_function
import re

def main():
    fh = open('sample','r')

    #using re.sub() function

    for line in fh:
        print(re.sub('(Len|Neverm)ore','####',line),end='')

    print('====================')

    # The aove statement will print everyline of the file . To avoid this

    fh2 = open('sample','r')
    for line in fh2:
        match = re.search('(Len|Neverm)ore',line)
        if match:
            print(line.replace(match.group(),'#####'),end='')

if __name__ == '__main__':
    main()