age = int(input("how old are you?: "))
if age >= 100:
    print("you are going to die soon")
elif age >= 18:
    print("you are an adult!")
else:
    print("you are a child")

temp = int(input("what is the temperature outside?\n"))
airquality = bool(input("what is the air quality?\n"))
if airquality <= 30 and temp >= 0:
    print("Temperature and air quality is good")
else:
    print("temperature and air quality is bad")