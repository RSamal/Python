#!/bin/python
from __future__ import print_function

# Generator example for inclusive range . __iter__ function makes an object as an iterator

class inclusive_range:

    def __init__(self,*args):
        numargs = len(args)
        if numargs < 1:
            raise TypeError('Require at least one argument and recived {}'.format(numargs))
        elif numargs == 1:
            self._stop = args[0]
            self._start = 0
            self._step = 1
        elif numargs == 2:
            (self._start, self._stop) = args
            self._step = 1
        elif numargs == 3:
            (self._start,self._stop,self._step) = args
        else:
            raise TypeError("requires at most 3 argument but recieved {}".format(numargs))
    def __iter__(self):
        i = self._start
        while i <= self._stop:
            yield i
            i += self._step
def main():
    o = inclusive_range(1,10,2)
    for i in o:print(i,end=' ')


if __name__ == '__main__':
    main()