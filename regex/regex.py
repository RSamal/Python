#
# use of re.search() which returns a match object , and we can use the match object as matching lines
#
from __future__ import print_function
import re


def main():
    fh = open("sample","r")

    # Using the re.search() function
    #for line in fh:
    #    if re.search('(Len|Neverm)ore',line):
    #        print(line,end='')

    print("===========")
    #using match Object

    for line in fh:
        match = re.search('(Len|Neverm)ore',line)
        if match:
            print(match.group())

if __name__ == '__main__':
    main()