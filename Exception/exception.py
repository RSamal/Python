#!/bin/python

# Exception example

from __future__ import print_function
def main():
    try:
        fh = open("sample",'r')
        for line in fh : print(line.strip())
    except IOError as e:
        print("Could not open the file :",e)
    finally:
        print("close out the resources")
if __name__ == '__main__':
    main()