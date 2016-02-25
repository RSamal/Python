# Preompile regex to save running time of the script

from __future__ import print_function
import re


def main():

    pattern = re.compile('(Len|Neverm)ore',re.IGNORECASE)

    fh = open('sample','r')
    for line in fh:
        match = re.search(pattern,line)
        if match:
            print(match.group())

if __name__ == '__main__':
    main()
