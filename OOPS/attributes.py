#!/bin/python
# Accessing attribute of object in python
# This is an example of the python object which scales well with the predfined python function , just like the **kwargs properties in other
#example

#Functions are
# hasattr(object,property)
# getattr(object,property)
# setattr(object,property,value)
# delattr(object,property)

class Employee:
    def __init__(self):
        pass

def main():
    emp = Employee()
    print(hasattr(emp,'age'))

    setattr(emp,'age',20)
    setattr(emp,'name','Rinku')
    print(hasattr(emp,'age'))
    print(getattr(emp,'age'))
    print(getattr(emp,'name'))

    delattr(emp,'age')
    print(hasattr(emp,'age'))
    print(getattr(emp,'name'))


    # Every pyton class has the following built in attributes
    # __dict__: Dictionary containing the class's namespace.
    # __doc__: Class documentation string or none, if undefined.
    # __name__: Class name.
    # __module__: Module name in which the class is defined. This attribute is "__main__" in interactive mode.
    # __bases__: A possibly empty tuple containing the base classes, in the order of their occurrence in the base class list.

    print("Employee.__dict__ :", Employee.__dict__)
    print("Employee.__doc__ :", Employee.__doc__)
    print("Employee.__name__ :",Employee.__name__)
    print("Employee.__module__ :",Employee.__module__)
    print("Employee.__bases__ :", Employee.__bases__)

if __name__ =='__main__':
    main()