# exception : event detected during the execution that interrupt the flow of
#               program
try:
    numerator = float(int(input("Enter a number that you want to divide: ")))
    denominator = float(int(input("Enter a number that you want to divide by: ")))
    division = numerator/denominator
except ZeroDivisionError as e:
    print(e)
    print("you can not divide a number by zero. *idiot!!")
except ValueError as e:
    print(e)
    print("Enter only numbers:")
except Exception as e:
    print(e)
    print("Oops!! something went wrong. please try again.")
else:
    print("Result = {} divide by {} is: ".format(numerator, denominator), division)
finally:
    print("This will always execute without interruption")

# file detection

import os

path = "C:\\Users\\HP\\Desktop\\x"
if os.path.exists(path):
    print("That file exists")
    if os.path.isfile(path):
        print("that is a file.")
    elif os.path.isdir(path):
        print("that is a folder")
else:
    print("That file doesn't exist.")