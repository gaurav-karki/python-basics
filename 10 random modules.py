import random
x = random.randint(1, 10)
y = random.randrange(1, 1000, 2)
z = random.triangular(1, 10)
print(x)
print(y)
print(z)

mylist = ['gaurav', 'hari', 'ram', 'sita']
a = random.choices(mylist)
print(a)
cards = [2, 3, 4, 5, 6, 7, 8, 9, 10, 'J', 'Q', 'K', 'A']
random.shuffle(cards)
print(cards)