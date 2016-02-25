#!/bin/python

# Example of Polymorphism. Note: To use polymorphism all the class should have same interface. Python is loosely typed hence polymorphism is natural


class Duck():
    def quack(self):
        print("Quacking!!!!")
    def walk(self):
        print("Walk like a duck")
    def bark(self):
        print("Duck cant bark!!!")
    def cloths(self):
        print("Duck has feather")
class Dog():
    def bark(self):
        print("Barking!!!!")
    def cloths(self):
        print("Dog has feather")
    def quack(self):
        print("Dog cant quack")
    def walk(self):
        print("walk like a dog")

def in_the_forest(animal):
    animal.bark()

def in_the_pond(animal):
    animal.quack()

def main():

    donald = Duck()
    frank = Dog()

    in_the_forest(donald)
    in_the_pond(frank)


if __name__ == '__main__':
    main()