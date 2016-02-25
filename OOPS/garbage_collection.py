#!/bin/python

"""
Python deletes unneeded objects (built-in types or class instances) automatically to free the memory space.
The process by which Python periodically reclaims blocks of memory that no longer are in use is termed Garbage Collection.

Python's garbage collector runs during program execution and is triggered when an object's reference count reaches zero.
An object's reference count changes as the number of aliases that point to it changes.

An object's reference count increases when it is assigned a new name or placed in a container (list, tuple, or dictionary).
The object's reference count decreases when it's deleted with del, its reference is reassigned, or its reference goes out of scope.
When an object's reference count reaches zero, Python collects it automatically.

We can see the garbage collection implementing the __del__ method in a class
"""

class Point:
    def __init__(self,x=0,y=0):
        self._x = x
        self._y = y

    def __del__(self):
        className = self.__class__.__name__
        print(className, " : Destoryed")


def main():

    ##### Simple Example #####
    a = 40 # create an object <40>
    b = a  # increase the reference count of <40>
    c = [b]  # increase the reference count of <40>

    del a   # decrease the reference count of <40>
    b = 100 # decrease the reference count of <40>
    c[0] = -1 # decrease the reference count of <40> and at this point the object will be garbage collected

    ### Example using custom defined object ####

    pt1 = Point()
    pt2 = pt1
    pt3 = pt2

    print(id(pt1),id(pt2),id(pt3))
    del pt1
    del pt2
    del pt3

if __name__ == "__main__":
    main()