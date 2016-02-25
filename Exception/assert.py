#!/bin/python

# assertion used to do the sanity check

def positve(arg):
    assert (arg > 0) ,"Cant be less than zero"
    return arg

def main():
    print(positve(10))
    try:
        print(positve(-10)) # assert will fail for this call
    except AssertionError as e:
        print(e)

if __name__ == '__main__':
    main()