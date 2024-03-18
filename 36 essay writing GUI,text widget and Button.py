from tkinter import *
from tkinter import messagebox
from tkinter import filedialog
# def display():
#     if x.get():
#         print("You agreed!!")
#     else:
#         print("You don't agree!!")


def submit():
    text = filedialog.asksaveasfile(defaultextension=".txt",
                                    filetypes=[
                                        ("Text file", ".txt"),# only save as .txt file
                                        ("All files", ".*"),
                                        ("pdf file", ".pdf")
                                    ])
    file_text = textarea.get(1.0, END)
    text.write(file_text)
    text.close()


def backspace():
    textarea.delete("end-2c", "end-1c")


def delete():
    if messagebox.askokcancel(title="Reminder!!!", message="Do you want to delete it all!!"):
        textarea.delete("1.0", END)



window = Tk()
window.geometry("1920x1080")
window.title("Essay writing window")
icon = PhotoImage(file="cover.png")
window.iconphoto(True, icon)
# menubar = Menu(window)
# window.config(menu=menubar)
#
# menubar.add_cascade(label="File", menu=menubar)
# menubar.pack()
# """frame"""
# frame = Frame(window,
#               background="white",
#               bd=5,
#               borderwidth=5,
#               relief="solid")
# """label"""
# label_1 = Label(window, image=icon)
# label_1.pack(side=TOP)
# label_1.place(x=10, y=20)
label = Label(window,
              text="Here you can write your essays, journals and notes",
              font=("Times New Roman", 20, "bold")
              )
label.pack(side=TOP)

textarea = Text(window, width=150,
                height=33,
                padx=10,
                pady=10)
textarea.pack()

# checkbox
# x = BooleanVar()
# check_box = Checkbutton(window,
#                         text="Do you agree on the privacy policy!",
#                         font=("Times New Roman", 20, "italic"),
#                         variable=x,
#                         onvalue=True,
#                         offvalue=False,
#                         command=display,
#                         padx=500,
#                         pady=700,
#                         fg="blue",
#                         background="black",
#                         activeforeground="blue",
#                         activebackground="black",
#                         compound=BOTTOM
#                         )
# check_box.pack(side=BOTTOM)

submit_button = Button(window,
                       text="Save",
                       command=submit)
submit_button.pack()
backspace_button = Button(window,
                          text="<-Backspace",
                          command=backspace)
backspace_button.pack()
delete_button = Button(window,
                       text="Delete",
                       command=delete)
delete_button.pack()
window.mainloop()
