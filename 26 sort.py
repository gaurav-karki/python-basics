# sort() method = used with list
# sort() function = used with iterables

students = ("Gaurav", "Anil", "Suprem", "Sagun", "Bob", "Diwas")

# students.sort(reverse=True)
# students =tuple which has not the attribute sort but with sorted we can sort a tuple
sorted_students = sorted(students)
for i in sorted_students:
    print(i)

person = [("gaurav", 20, "A"),
          ("ram", 50, "D"),
          ("shyam", 30, "B"),
          ("hari", 34, "C")]

age = lambda years: years[1]
person.sort(key=age, reverse=True)
for i in person:
    print(i)
