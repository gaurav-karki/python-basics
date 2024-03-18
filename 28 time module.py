import time

print(time.ctime(1000))# convert a time expressed since epoch to a readable string.
                    # epoch = when the computer thinks the time began.

print(time.time())# return the amount of second since epoch.

print(time.time_ns())# Return the current time in nanoseconds since the Epoch

print(time.thread_time())# Thread time for profiling: sum of the kernel and user-space CPU time

# for i in range(10, 0, -1):
#     print(i, end=" ")
#     time.sleep(1)
#
# print("\nHappy new year 2024")

# to get the current time using time module
print(time.ctime(time.time()))

time_object = time.localtime()
local_time = time.strftime("%B %d %Y| %I:%M:%S", time_object)
print(local_time)