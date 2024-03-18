class human:
    living = True

    def eat(self):
        print("Eats to stay alive")

    def breath(self):
        print("Breaths to stay alive")

class male(human):
    man = "Sperm"

    def leads(self):
        print("Male leads the society")

class female(human):
    women = "Ovary with Ovum"

    def follows(self):
        print("Female used to follow male but nowadays they are independent")

male = male()
female = female()
print("MALE")
print("living : ", male.living)
male.eat()
male.breath()
print("Male has {} for reproduction".format(male.man))
male.leads()
print("--------------------------------------")
print("Female")
print("Living : ", female.living)
female.eat()
female.breath()
print("Female has {} for reproduction ".format(female.women))
female.follows()