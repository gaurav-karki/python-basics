# args(*) = parameter that will pack all the arguments into a tuple.
#           useful so that a function can accept a varying amount of arguments.

def add(*args):
    sum = 0
    args = list(args)
    args[5] = 0
    for i in args:
        sum += i
    return sum
print(add(1,2,3,4,5,789))

# kwargs(**) = keyword arguments are the parameter that will pack all arguments
#               into a dictionary.
mydict = {'male': 'gaurav',
          'sita': 'female',
          'hari': 'unidentified'}
def name(**mydict):
    print("Hello ", end='')
    for key, value in mydict.items():
        print(value, end='')
        return


# str.format() = optional method that gives users more control
#           while displaying output.

item1 = "sun"
item2 = "moon"
""":normal method"""
print(item1+" goes down, " + item2+" comes up.")
""":format method"""
print("{} goes down, {} comes up.".format(item1, item2))
""":positional argument"""
print("{1} goes down ,{0} come up.".format(item1, item2))
""":keyword argument"""
print("{item1} goes down, {item2} comes up.".format(item1=1, item2=2))
""":add padding to the argument"""
name = input("Enter your name:")

print("hello {} . Nice to meet you!!!".format(name))
# add padding or space
print("hello {name:10} . Nice to meet you!!!".format(name=input("Enter your name:")))
print("hello {name:<10} . Nice to meet you!!!".format(name=input("Enter your name:")))
print("hello {name:>10} . Nice to meet you!!!".format(name=input("Enter your name:")))
print("hello {name:^10} . Nice to meet you!!!".format(name=input("Enter your name:")))
""":keyword argument"""
print("hello {name2} . ohh hi {name1}".format(name1=input("Enter your name:"), name2=input("Enter your friend name:")))
""":positional argument"""
print("{1} goes down, {0} comes up.".format(item1, item2))
""":str format for numbers"""
number = 3.14596
number1 = 3240
print("the number pi is : {}".format(number))
print("the number pi is : {:.3f}".format(number))

print("where is my {}".format("Amount : ", number1))
print("where is my {:,}".format(number1))
print("the number pi is : {}".format(number1))
print("the number in binary is : {:b}".format(number1))
print("the number in octal is : {:o}".format(number1))
print("the number in hexadecimal  is : {:X}".format(number1))
print("the number in scientific notation is : {:E}".format(number1))



