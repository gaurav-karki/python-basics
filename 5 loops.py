import time
# while loop= a statement that will execute its block of code unlimited
#               amount of time.
# while loop example:
name = None
while not name:
    name = input("Enter your name:")

print("hello " + name)

name = ''
while len(name) == 0:
    name = input("Enter your full name: \n")
print("Hello " + name.upper() + " ! Nice to meet you.")

# for loop = a statement that will execute its block of code limited
#               amount of time.
# for loop example:
word = input("Give me a word: ")
for i in word:
    print(i)

number = input("Enter a number:")
for i in range(10):
    print(i + 1)

for index in range(0, 10, 1):
    print(index + 1)

for i in range(10, 0, -1):
    print(i, end="")
    time.sleep(1)
print("Merry christmas!!!")

# nested loop = the 'inner loop' will finish all of it's iteration before
#               finishing the one iteration of outerloop.
rows = int(input("How many rows?:"))
columns = int(input("How many columns?:"))
symbol = "|__|"
for i in range(rows):
    for j in range(columns):
        print(symbol, end="")
        time.sleep(1)
    print(i)

# loop control statement : change  a loop execution from its normal sequence.
# break = used to terminate the loop entirely.
# continue = skips to the next iteration of loop.
# pass = does nothing , act like a placeholder.
while True:
    name = input("Enter your name:")
    if name != "":
        pass
        print("Hello " + name + ", Nice to meet you!!")
        break

name1 = "Gau@rav@ ka@r@ki"
for i in name1:
    if i == "@":
        continue
    print(i, end="")


for i in range(3, 0, -1):
    if i == 0:
        pass
    else:
        print(i, " ", end="")
        time.sleep(1)
print("\nHello gaurav!!")
