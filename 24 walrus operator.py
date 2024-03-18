# walrus operator(:=)
# lets create a tuple
# foods = list()
# while True:
#     food = input("Enter the foods you want to eat: ")
#     if food.lower() == "quit":
#         break
#     foods.append(food)
# print("Enjoy your meal: ", foods)

foods = list()
while (food := input("Enter the food you want to eat: ").lower()) != "quit":
    foods.append(food)
print("Enjoy your meal: ")
print(foods)

def hello():
    print("Hello there")

hi = hello
hi()
print(hello)
print(hi)

name = print
name("hello, my name is gaurav karki")