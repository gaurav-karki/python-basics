# radio button = similar to checkbox, but you can only select one from a group.
from tkinter import *

food = ["pizza", "hamburger", "french fries"]
window = Tk()
pizza_image = PhotoImage(file="pizza.png")
hamburger_image = PhotoImage(file="ham burger.png")
french_fries_image = PhotoImage(file="french fries.png")
food_image = [pizza_image, hamburger_image, french_fries_image]
x = IntVar()
for i in range(len(food)):
    radio_button = Radiobutton(window,
                               text=food[i],
                               variable=x,
                               value=i,
                               padx=20,
                               pady=10,
                               font=("Times New Roman", 20, "bold"),
                               image=food_image[i])
    radio_button.pack(anchor=W)
window.mainloop()