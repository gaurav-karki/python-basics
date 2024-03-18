# list = used to store multiple items in a single variable.
student = ["Gaurav", "Ram", "Hari", "Shyam", "Gopal"]
student[4] = "Anil"
student.append("krishna")
student.count("")
student.extend("Madan")
student.remove("Hari")
student.pop()
print(student)
for i in student:
    print(i)
student.clear()

# 2D Lists = a list of lists
student_name = ["Gaurav", "Ram", "Hari", "Shyam", "Gopal"]
student_marks = [90, 80, 60, 72, 30]
status = ["pass", "Fail"]

marksheet = [student_name, student_marks, status]
for i in marksheet:
    print(i)
print(marksheet[0][1], marksheet[1][1], marksheet[2][0])
print(marksheet[0][4], marksheet[1][3], marksheet[2][0])

# tuples = similar to list but written within a parentheses which is ordered
#          sequence of values.
student1 = ("Gaurav", 20, "male")
student2 = ("Sita", 21, "female")
print("---------------------------")
student_total = (student1, student2)
print(student1.count("male"))
print(student1.index("Gaurav"))
print("---------------------------")
print(student2.index(21))
print(student2.index("female"))
print("---------------------------")
for x in student_total:
    print(x)
if "Gaurav" in student1:
    print("i am present!!")

# Set = a collection which is unordered , non-indexed and doesn't
#         print duplicate values.
print("_______________________________________")
class1 = {"gaurav", "ram", "hari", "sita "}
class2 = {"hari", "gopal", "krishna", "madan"}

class1.add("ganga")
class2.remove("madan")
class2.update(class1)
print(class2)
school = class1.union(class2)
print(school)
print(class2.difference(class1))
class1.clear()
class2.clear()

# dictionary = used to store a data value of key:value pair
#              dictionary is a collection which is ordered, changeable and
#              does not allow duplicate values
print("____________________________________")
country_capital = {'USA': 'washington DC',
                   'Nepal': 'Kathmandu',
                   'India': 'New delhi',
                   'China': 'beijing',
                   'Russia': 'Moscow'}
print(country_capital)
country_capital.update({'Germany': 'Berlin'})
print(country_capital)
country_capital.update({'India': 'Kathmandu'})
print(country_capital)
country_capital.pop('USA')
country_capital.fromkeys(country_capital)
country_capital.popitem()
print(country_capital.setdefault('Spain'))
for key, values in country_capital.items():
    print(key, values)
print(country_capital['Nepal'])
print(country_capital.get('Germany'))
print(country_capital.values())
print(country_capital.keys())
print(country_capital.items())


# index operator : [] gives access to a sequence's element ( str, lists, tuple)
print("____________________________________")

name = input("Enter your name:")
if (name [0]. islower()):
    print(name.capitalize())
print(name)
name_person = ['gaurav', 'ram', 'hari']
age_person = ["KARKI", 40, 50]
detail = [name_person, age_person]
print(detail[0][1].upper(), detail[1][0].capitalize())
detail = name_person[0], age_person[0].format(name_person, age_person)
print(detail)

