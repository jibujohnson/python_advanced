from abc import ABC,abstractmethod

class Animal(ABC):          #Parent class
    @abstractmethod
    def sound(self):        #Abstract method
        pass                #Do nothing

# Every class that inherits from Animal must provide its own implementation of sound() method.

class Cat(Animal):          #Child class of Animal,it also implements sound() method.
    def sound(self):
        print("Cat meows.")
class Dog(Animal):
    def sound(self):
        print("Dog barks.")

#obj=Animal()               #Cannot create an object for animal class directly.

obj1=Cat()
obj1.sound()

obj2=Dog()
obj2.sound()