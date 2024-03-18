class Car:

    def __init__(self, make, model, year, color):
        self.make = make
        self.model = model
        self.year = year
        self.color = color


    def drive(self):
        print("she is driving a {} {} ".format(self.make, self.model))


    def stop(self):
        print("There is a {} stopped in {} color".format(self.model, self.color))

