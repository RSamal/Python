#!/bin/python
from __future__ import print_function

#No argument function
def noarg():
    print("You called no argument function")

# One Argument function
def oneArg(x):
    print("you called one arg function with value {}".format(x))


# Two Argument Function
def twoArg(x,y):
    print("you called two argument function with value {} and {}".format(x,y))

# Function with default value, None is a special value in python same as null in othet programing language
def defaultValue(x,y=None,z=20):
    print("You called deafult value function with value {}, {} and {}".format(x,y,z))

# Keyword arguments
def keyargs(name,age):
    print(name,age)

#varable arguments. Variable argument is a touple so in python code we can treat this as a tuple

def varFunction(this,that,other,*args):
    print(this,that,other,args, end='')
    for i in args: print(i, end='')

#NamedFunction or dict function vary common known as **kwargs
def namedFunc(**kwargs):
    for k in kwargs:print(k,kwargs[k],end='')

# All together
def all(x,y,z,*args,**kwargs):
    print(x,y,z,args,kwargs)


def main():
    #Called the no argument function
    noarg()

    # Called one argument function
    oneArg(12)

    #called two argument function
    twoArg(10,20)

    #calling keyword function
    keyargs(age=25,name='Rama')

    #Called default argument function
    defaultValue(100)
    defaultValue(100,200)
    defaultValue(100,200,300)

    # Called the variabelargument Function
    varFunction(1,2,3,10,20)
    varFunction(1,2,3,10,20,30,49)

    # calling the named function
    namedFunc(one=1,two=2,three=3)

    all(1,2,3,4,5,6,7,one = 1, two =2 , three =3)

    # Anonymous function or lambada in python
    double = lambda x:  x+x
    print(double(10))



if __name__ =="__main__":
    main()