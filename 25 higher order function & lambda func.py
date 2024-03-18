# higher order function = a function that either:
#                   1. accepts the function as the argument
#                       or
#                   2. return the function
#                   (in python, function are also treated as an object)

def loud(text):
    return text.upper()


def quiet(text):
    return text.lower()


def hello(function):
    text = function("Gaurav")
    print(text)


# so as we can see in hello function we can pass loud and quiet function as an argument.
hello(loud)
hello(quiet)


# so as you can see it returns the dividend function.
def divisor(x):
    def dividend(y):
        return y / x

    return dividend


divide = divisor(5)
print(divide(10))


# lambda function = function written in 1 line using lambda keyword
#               accepts any number of arguments but has only one expression.
# normal functon
def gaurav(x):
    return x * 2


gk = gaurav(10)
print(gk)

# lambda function : expression

double = lambda x: x * 2
print(double(225))

multiply = lambda x, y, z: x * y * z
print(multiply(8, 9, 7))

add = lambda a, b, c, d: a+b+c+d
print(add(25, 26, 27, 28))

age_check = lambda age: True if age >= 18 else False
print(age_check(18))