#!/bin/python
# Class example with scalable properties

from __future__ import print_function

class Duck:
    def __init__(self,**kwargs):
        self._properties = kwargs

    def set_properties(self,k,v):
        self._properties[k] = v

    def get_properties(self,k):
        return self._properties.get(k,None)

def main():
    donald = Duck(color='blue')
   
if __name__ == '__main__':
    main()