import math

x = 20.221
a = 20.321
b = 20.123
c = 20.120
print(round(x))
print(math.ceil(x))
print(math.floor(x))
print(math.log10(x))
print(math.pi)
print(math.e)
print(math.log(x, 8))
print(math.degrees(x))
print(math.sqrt(x))
print(abs(x))
print(pow(x, 2))
print(max(a, b, c))
print(min(a, b, c))

# slicing and indexing

word = "Gaurav"
print(word[::3])

print(word[::-1])

website1 = "http://pornhub.com"
website2 = "http://nepalexaminationboard.edu.np.com"
Slice = slice(7, -4)
print(website1[Slice])
print(website2[Slice])

word = "GAURAV"
for i in word:
    print(i)

number = None
while not number:
    number = input("your phone number:")
    if not len(number) != 10:
        print("Invalid number")
    else:
        print("call me baby: ", number)
    break

