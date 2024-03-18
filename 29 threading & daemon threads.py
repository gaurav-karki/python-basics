# thread = a flow of execution. like a separate order of instruction. however each threads take a turn running
#              to achieve the concurrency.
#   GIL = Global Interpreter lock allow only one thread to hold the python interpreter at any one time.

# cpu bound = program/task spending most of the time waiting for internal event(CPU intensive)
#       uses multiprocessing

# I/O bound = program/ task spending most of the time for external events such as user input, web scraping)
#           use multithreading
import threading
import time


def eat_breakfast():
    time.sleep(3)
    print("you have finished your breakfast")


def drink_tea():
    time.sleep(4)
    print("you are drinking your tea")


def run():
    time.sleep(5)
    print("Now start running")


x = threading.Thread(target=eat_breakfast, args=())
x.start()

y = threading.Thread(target=drink_tea, args=())
y.start()

z = threading.Thread(target=run, args=())
z.start()

eat_breakfast()
drink_tea()
run()

x.join()
y.join()
z.join()

print(threading.active_count())
print(threading.enumerate())

# daemon threads = a thread that runs in the background and not important for a program to run
#           your program will not wait for daemon thread to finish before exiting
#           non-daemon threads can not normally be killed, stays alive until the task is complete.

#           example: back groundtask, garbage collection,waiting  user input
def timer():
    count = 0
    while True:
        time.sleep(1)
        count += 1
        print("Logged in for ", count, " secs")


a = threading.Thread(target=timer(), daemon=True)
a.start()



user = input("do you want to exit(yes/no) : ")
