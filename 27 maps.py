# maps() = applies a function to each item in iterable such as ( list, tuple etc.)
# maps( function , iterable)
print("------------------maps()---------------")
store = [("shirt", 1500),
         ("pant", 2500),
         ("hoodie", 3000),
         ("jacket", 5000),
         ("tanktop", 200)]

to_inr = lambda data: (data[0], data[1] / 1.6)

store_inr = list(map(to_inr, store))
for i in store_inr:
    print(i)

# filter = creates a collection from an iterable for which a function returns true.

# filter( function, iterable)
print("-----------------filter-----------------")
name = [("gaurav", 20),
        ("ram", 21),
        ("hari", 18),
        ("gopal", 13),
        ("suprem", 23),
        ("alish", 12)]

age = lambda data: data[1] >= 18
age_above18 = list(filter(age, name))
for i in age_above18:
    print(i)

# reduce =apply a function to an iterable and reduce it to a single cumulative value.
#           perform function on first 2 elements and repeats process until 1 value remains.
# reduce( function , iterable)
print("-------------------------reduce---------------------------")
import functools

name = ["G", "A", "U", "R", "A", "V"]
word = functools.reduce(lambda x, y: x + y, name)
print(word)

factorial = [10, 9, 8, 7, 6, 5, 4, 3, 2, 1]
number = functools.reduce(lambda x, y: x * y, factorial)
print(number)

# list comprehension = a way to create a new list with less syntax can mimic certain lambda function
#                   easier to read.
# list = [expression for item in iterable]
print("--------------------list comprehension--------------------------")
square = [i * i for i in range(1, 11)]
print(square)
# to mimic lambda function list = [ expression for item in iterable if conditional]
students = [100, 90, 80, 60, 70, 40, 45, 55, 61, 59, 23, 47, 0, 10]
# passed_student = [i for i in students if i >= 50]
passed_student = [i if i >= 50 else "failed" for i in students]

print("passed_students: ", passed_student)

# dictionary comprehension = way to create dictionaries using an expression.
#                   can replace a loop and certain lambda functions.
# dictionary = {key: expression for (key, value) in iterables}
print("---------------------- dictionary comprehension------------------------")
country_temp_f = {'USA': 29,
                  'NEPAL': 42,
                  'INDIA': 48,
                  'GERMANY': 25}
country_temp_c = {key: round((value - 32) * (5 / 9)) for (key, value) in country_temp_f.items()}
print(country_temp_c, "degree celcius")

# [ expression for item in iterable if conditional]

name_gender = {'gaurav': 'male',
               'sita': 'female',
               'geeta': 'female',
               'ram': 'male',
               'gopal': 'male',
               'hari': 'male',
               'laxmi': 'female'}
gender_male = {key: value for (key, value) in name_gender.items() if value == 'male'}
print(gender_male)


# dict  comprehension using function
# {key: function(value) for (key value) in iterable.items }
def check_temp(value):
    if value >= 70:
        return "hot"
    elif 69 >= value >= 40:
        return "mild"
    else:
        return "cold"


country_temp = {'USA': 29,
                'NEPAL': 42,
                'INDIA': 48,
                'GERMANY': 25,
                'MALYASIA': 78,
                'PHILIPPINE': 71,
                'AUSTRALIA': 85,
                'CHINA': 51,
                'TAIWAN': 54,
                'MALDIVES': 76,
                'CANADA': 18,
                'RUSSIA': 7,
                'SOUTH KOREA': 59,
                'JAPAN': 42}
country_temp_description = {key: check_temp(value) for (key, value) in country_temp.items()}
print(country_temp_description)

# same dict using if else condition
# {key: if/else for (key, value) in iterables.items)
climate = {key: "warm" if value >= 40 else "cold" for (key, value) in country_temp.items()}
print(climate)

# zip (*iterables) = aggregate element from two or more iterables(list, tuple, set etc.)
#       creates a zip object of paired elements stored in tuple for each element
print("-----------------------zip--------------------------------")
student_name = ["gaurav", "suprem", "alish", "pradip", "samir", "ajay", "yabesh"]
student_id = ("0362124", "0362123", "0362454", "0362145", "0362678", "0362324", "0362756")

room = dict(zip(student_name, student_id))
for key, value in room.items():
    print(key + " : " + value)
