# Read file
# try:
#     with open("gaurav.txt") as file:
#         print(file.read())
# except FileNotFoundError as e:
#     print(e)
#     print(" sorry,we can not locate that file. :(")

# write file
# text = "gaurav: hey it's great, I am fine. I am learning python.\n what about you?"
# with open("gk.txt", 'a') as file:
#     print(file.write(text))

# copy a file
# copyfile() = copies content of a file
# copy() = copyfile() + permission mode + destination can be directory
# copy2() = copy() + copy metadata ( file creation and modification times

# import shutil
# shutil.copyfile("gaurav.txt", "copyfile.txt")# source , destination
# shutil.copy("gaurav.txt", "copy().txt")
# shutil.copy2("gk.txt", "copy().txt")

# move a file
# import os
# source = "move.txt"
# destination = "C:\\Users\\HP\\Desktop\\move.txt"
#
# try:
#     if os.path.exists(destination):
#         print("There is already a file named " + source)
#     else:
#         os.replace(source, destination)
#         print(source + " was moved")
#
# except FileNotFoundError as f:
#     print(f)
#     print(source + " was not found")

# delete a file.
# import os
# import shutil
# file = "test.txt"
# try:
#     # shutil.rmtree(file) #remove a folder with files
#     if os.remove(file): # remove a file
#     # if os.rmdir(file): # remove a empty folder
#         print(file + " deleted sucessfully")
# except FileNotFoundError as e:
#     print(e)
#     print("File no longer exists!!")
# except PermissionError as e:
#     print(e)
#     print("you can not delete a folder using remove function")
# except OSError as e:
#     print(e)
#     print(" you can not remove a folder with files using rmdir function")
# else:
#     print(file + " was deleted")

