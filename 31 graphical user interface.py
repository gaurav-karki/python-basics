from tkinter import *


def click():
    username = entry.get()
    print("Hello", username)


def delete():
    entry.delete(0, END)


def backspace():
    entry.delete(len(entry.get()) - 1, END)


window = Tk()  # instantiate an instance of a window
window.geometry("420x420")
window.title("Graphical User Interface")
icon = PhotoImage(file='ori-1.png')
window.iconphoto(True, icon)
# photo = PhotoImage(file="ori-1.png")
# label = an area widget that holds text and image within a window
label = Label(window,
              text="Hello",
              font=("calibre", 20, "bold"),
              fg="white",
              background="black",
              relief=SUNKEN,
              bd=10)
label.pack(side=TOP)
label.place(x=0, y=0)
# entry widget = text box that accepts a single line of user input
entry = Entry(window,
              font=("Times new roman", 20, "normal"),
              )
entry.pack(side=LEFT)
entry.place(x=10, y=60)

# buttons= it's button it is what it is, you click it
submit_button = Button(window,
                       text="Click me",
                       command=click,
                       font=("Times new roman", 20, "bold"),
                       relief=RAISED,
                       bd=5,
                       padx=10,
                       pady=10
                       )
submit_button.pack(side=BOTTOM)
delete_button = Button(window, text="Delete", command=delete)
delete_button.pack(side=BOTTOM)
backspace_button = Button(window, text="Backspace", command=backspace)
backspace_button.pack(side=BOTTOM)
window.mainloop()  # place window on the computer screen
