class Prey:
    def flee(self):
        print("this animal flees")

# method overriding = rabbit eagles and fish implement their specific method
#             instead of implementing the method that it inherits from the parent class.
class Predator:
    def hunt(self):
        print("This animal hunts the flees")


class Rabbit(Prey):
    def flee(self):
        print("rabbit gets hunted by Eagles")


class Eagle(Predator):
    def hunt(self):
        print("Eagles hunt down rabbit")


class Fish(Prey, Predator):
    def flee(self):
        print("small fish are hunted by big fish")

    def hunt(self):
        print("Big fish are hunted by sharks and whales")


rabbit = Rabbit()
eagle = Eagle()
fish = Fish()

rabbit.flee()
eagle.hunt()
fish.flee()
fish.hunt()