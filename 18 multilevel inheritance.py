class Organism:
    alive = True


class Animal(Organism):
    def __init__(self, eat, reproduce, death):
        self.eat = eat
        self.reproduce = reproduce
        self.death = death


class Dog(Animal):
    def bark(self):
        print("is barking")


class Labrador(Dog):
    def cute(self):
        print("this dog is so cute")


dog_1 = Labrador("Meat", True, True)
print("Eats : " + dog_1.eat)
print("Does it reproduce : " + str(dog_1.reproduce))
print("Every organism death is certain : " + str(dog_1.death))
print("is this dog alive: " + str(dog_1.alive))
dog_1.bark()
dog_1.cute()

