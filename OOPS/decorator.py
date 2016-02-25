#!/bin/

from __future__ import print_function

# Decorator example

class Duck:
    def __init__(self,**kwargs):
        self._properties = kwargs

    def get_properties(self,k):
        return self._properties.get(k,None)
    def set_properties(self,k,v):
        self._properties[k] = v

    # Using decorator
    @property
    def color(self):
        return self._properties.get('color',None)

    @color.setter
    def color(self,c):
         self._properties['color'] = c

    @color.deleter
    def color(self):
        del self._properties['color']
def main():

    donald = Duck()

    print(donald.color)
    donald.color = 'blue'
    print(donald.color)


if __name__ == '__main__':
    main()