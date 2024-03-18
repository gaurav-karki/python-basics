# list box = a listing od selectable text items within its own container
from tkinter import *
from tkinter import messagebox  # submodule of tkinter
# from tkinter import colorchooser


def buy():
    cart = listbox.curselection()
    if cart:
        select_items = [listbox.get(i) for i in cart]
        if messagebox.askokcancel(title="Reminder!!", message="Are you sure to buy it?"):
            print("You have bought: " + str(select_items))
    else:
        messagebox.showinfo(title="No food item selected!!", message="Select at least one food item to buy")


def add():
    listbox.insert(listbox.size(), entry_food.get())
    listbox.config(height=listbox.size())


def delete():
    # listbox.delete(listbox.curselection())
    for i in reversed(listbox.curselection()):
        listbox.delete(i)
    listbox.config(height=listbox.size())


window = Tk()

label = Label(window,
              text="Thela Food",
              font=("Arial Black", 20),
              relief=RAISED,
              pady=20,
              background="white",
              borderwidth=5,
              fg="Green",
              anchor=CENTER)
label.pack(anchor=W)
listbox = Listbox(window,
                  font=("Constantia", 16, "italic"),
                  bg="#f7ffde",
                  fg="green",
                  border=2.5,
                  justify=LEFT,
                  width=30,
                  selectmode=MULTIPLE)
listbox.pack(anchor=W)

listbox.insert(1, "- Chicken Momo")
listbox.insert(2, "- Buff Momo")
listbox.insert(3, "- Sausage")
listbox.insert(4, "- French Fries")
listbox.insert(5, "- Panipuri")
listbox.insert(6, "- Chatpatey")
listbox.insert(7, "- Dahipuri and Chat")
listbox.insert(8, "- Syavale")
listbox.config(height=listbox.size())

# Enter the food items
entry_food = Entry(window, border=2.5, relief=RAISED,
                   font="Constantia",
                   bg="white",
                   fg="green")
entry_food.pack(anchor=W)
# entry_food.place(x=50)

# Button to buy food items
buy_button = Button(window,
                    text="Buy",
                    command=buy)
buy_button.pack(anchor=W)

# add food item to the listbox
add_food_button = Button(window,
                         text="Add food Item",
                         command=add
                         )
add_food_button.pack(anchor=W)

# Delete food items from the listbox
delete_item = Button(window,
                     text="Delete item",
                     command=delete)
delete_item.pack(anchor=W)

window.mainloop()
