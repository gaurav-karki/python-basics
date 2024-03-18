class Animal:

    def eat(self):
        print("This animal is eating")


class Rabbit(Animal):

    def eat(self):
        print("This rabbit is eating a carrot")

rabbit = Rabbit()
rabbit.eat()

# method chaining = calling multiple method sequentially
#                   each method call perform an action on the same object and return self.

class Bottle:

    def getbottle(self):
        print("Get the water bottle")
        return self

    def openbottle(self):
        print("open the nozzle of bottle")
        return self

    def drinkwater(self):
        print("Drink the water from the bottle")
        return self

    def closebottle(self):
        print("Close the nozzle of the bottle and put it back")
        return self


bottle = Bottle()
# method chaining
bottle.getbottle()\
    .openbottle()\
    .drinkwater()\
    .closebottle()