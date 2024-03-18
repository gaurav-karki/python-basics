class Car:
    color = None


class Motorcycle:
    color = None


def change_color(vehicle, color):
    vehicle.color = color

car_1 = Car()
car_2 = Car()

bike_1 = Motorcycle()
bike_2 = Motorcycle()

change_color(car_1, "Red")
change_color(car_2, "white")
change_color(bike_1, "blue")
change_color(bike_2, "grey")

print(car_1.color)
print(car_2.color)
print(bike_1.color)
print(bike_2.color)

# duck typing =concept where the class of an object is less important that the methods and attributes
# class type is not checked if minimum method and attributes are present.

class Duck:

    def walk(self):
        print("This duck is walking")

    def talk(self):
        print("This duck is quacking")

class Chicken:
    def walk(self):
        print("This chicken is walking")

    def talk(self):
        print("This chicken is clucking")

class Person:
    def catch_duck(self, duck):
        duck.walk()
        duck.talk()
        print(" you caught the duck")


duck = Duck()
chicken = Chicken()
person = Person()

duck.walk()
duck.talk()
chicken.walk()
chicken.talk()

person.catch_duck(chicken)