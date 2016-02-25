#!/bin/python

# generator function returns an iterator in python

def inclusive_range(*args):
    numargs = len(args)

    if numargs < 1:
        raise TypeError('Inclusive_range expect at least one argument recived :{}'.format(numargs))
    elif numargs == 1:
        stop = args[0]
        start = 0
        step = 1
    elif numargs == 2:
        (start,stop) = args
        step =1
    elif numargs == 3:
        (start,stop,step) = args
    else:
        raise TypeError('Inclusive-range function at most accept 3 and recived {}'.format(numargs))
    i = start
    while i <= stop:
        yield i
        i += step

for i in inclusive_range(1,10,2):
    print(i)