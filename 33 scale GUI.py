# scale
from tkinter import *


def submit():
    result = scale.get()
    print("Temperature of water : ", result, " degree celsius")


window = Tk()
hot = PhotoImage(file="flame.png")
hot_label = Label(window, image=hot)
hot_label.pack()
scale = Scale(window,
              from_=100,
              to=0,
              length=400,
              tickinterval=10,
              orient=VERTICAL,
              font=("Consolas", 20),
              # resolution=5 # allows to increase by the value you assigned
              # showvalue=False, # True/ False shows or doesn't show the value of scale
              troughcolor="#69EAFF",
              fg="#FF1C00",
              bg="#111111",
              )
# scale.set(((scale['from']-scale['to'])/2)-scale['to'])
scale.pack()
cold = PhotoImage(file="ice.png")
cold_label = Label(window, image=cold)
cold_label.pack()
button = Button(window, text="Submit", command=submit)
button.pack(side=BOTTOM)
# button.place(y=20)


window.mainloop()