#!/bin/python
# Example of the inheritance

class Animal:
    def talk(self):
        print("I have something to say")

    def walk(self):
        print("hey i am walking")

    def cloths(self):
        print("I have nice cloths")

class Duck(Animal):

    def walk(self):
        print("Walk like a duck!!!")

class Dog(Animal):

    def cloths(self):
        print("I have brown and white fur")

def main():

    donald = Duck()
    donald.walk()

    fido = Dog()
    fido.walk()
    fido.cloths()
if __name__ == '__main__':
    main()