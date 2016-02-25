#!/bin/python

# User defined exception

from __future__ import print_function

def main():

    try:
        for line in readFile("lines.txt"):
            print(line.strip())
    except IOError as e:
        print("Unable to read the file :", e)
    except ValueError as e:
        print("unable to read the file :", e)

def readFile(file_name):

    if file_name.endswith('.txt'):
        fh = open(file_name,'r')
        return fh.readlines()
    else:
        raise ValueError('filename must end with .txt')

if __name__ ==  '__main__':
    main()