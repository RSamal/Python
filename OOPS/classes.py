#!/bin/python

from __future__ import print_function
# Simple class example but the properties does not scale well

class Duck:

    def __init__(self, color='white'):
        self._color = color

    def quak(self):
        print("Quaaak!!!!",self._v)

    def walk(self):
        print("Walk like a duck!!!",self._v)

    def get_color(self):
        return self._color

    def set_color(self,color):
        self._color = color


def main():

    donald = Duck()
    print(donald.get_color())
    donald.set_color('blue')
    print(donald.get_color())
if __name__ == '__main__':
    main()