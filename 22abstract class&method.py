# prevent user from creating an object of that class
# compels user to override the method to its child class
# abstract class = class that contains one or more abstract method.
# abstract method = a method which have declaration but doesn't have implementation.

from abc import ABC, abstractmethod


class Vehicle(ABC):
    @abstractmethod
    def go(self):
        pass

    @abstractmethod
    def stop(self):
        pass


class Car(Vehicle):
    def go(self):
        print("You drive a car")

    def stop(self):
        print("The  car is stopped")


class Motorcycle(Vehicle):
    def go(self):
        print("you ride a motorcycle")

    def stop(self):
        print("The motorcycle is stopped")


# abstract class does not  allow to create an object of its class so without object there is no method call
# so though the method are declared, but we can not implement it
# vehicle = Vehicle()
car = Car()
motorcycle = Motorcycle()

car.go()
motorcycle.go()
