from oopcar import Car

car_1 = Car("Nissan", "GTR", 2024, "Blue")


print(car_1.make, car_1.model, car_1.year, car_1.color)

car_1.drive()
car_1.stop()


class Person:
    eats = 3, "times a day"# class variable
    def __init__(self, name, age, gender, status):
        self.name = name # instance variable
        self.age = age # instance variable
        self.gender = gender # instance variable
        self.status = status # instance variable

    def isworking(self):
        print("He is learning python")


person_1 = Person("Gaurav", 20, "Male", "Unmarried")
print("------------------------------------")
print("Name : "+person_1.name)
print("Age : " + str(person_1.age))
print("Gender : "+person_1.gender)
print("Status : "+person_1.status)
for i in Person.eats:
    print(i, end=" ")
    

person_1.isworking()