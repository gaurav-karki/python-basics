# function = is a block of code which execute only when it is called.
def laptop(company, generation, model):
    print("Device : " + company, "|Generation : ", generation, "|Model : ", model)
    model += 1
    print("you need to change your devices to " + str(model) + " model")
laptop('hp', 11, 2022)

# return statement = function send values/object back to the caller
#                     these values/object are known as function return values

def name(first_name, last_name):
    print(input("Enter your full name: "))

y = name(first_name='', last_name='')
print("Hello", y)

# keyword argument = You can also send arguments with the key = value syntax.
#                    This way the order of the arguments does not matter.
def hello(first_name, middle_name, last_name):
    return ("hello "+ first_name+" "+middle_name+" "+last_name)

x = hello(first_name="Ram", last_name="Parsad",middle_name= "Dhakal")
print(x)

# nested function
def num(num1):
    print(round(abs(float(input("Enter a positive number: ")))))
num(num1='')

# scope = the region that a variable is recognized
#         a variable is only available inside the region it is created
#          a  global and local scope of a variable can be also created.

def display_name():
    name = input("Enter your name: ")
    print("hello " + name.upper() +" Nice to meet you!!")
display_name()
