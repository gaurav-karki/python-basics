# menubar
from tkinter import *
from tkinter import filedialog
from tkinter import messagebox
import clipboard



# function for file menu
def openfile():
    open_file = filedialog.askopenfile(defaultextension=".txt",
                                       filetypes=[("Text file", ".txt"),
                                                  ("All files", ".*"),
                                                  ("pdf file", ".pdf"),
                                                  ("MS Word file", ".docx")
                                                  ])
    if open_file:
        try:
            # Open the file for reading
            with open(open_file.name, 'r') as file:

                # Read the content of the file
                file_content = file.read()
            text_area.insert('1.0', file_content)

        except FileNotFoundError as e:
            error_label.config(print(e))
        except Exception as e:
            error_label.config(print(e))
    else:
        print("No file selected")


def savefile():
    save_file = filedialog.asksaveasfile(defaultextension=".txt",
                                         filetypes=[
                                             ("Text file", ".txt"),  # only save as .txt file
                                             ("All files", ".*"),
                                             ("pdf file", ".pdf"),
                                             ("MS Word file", ".docx")
                                         ])
    file_text = text_area.get(1.0, END)
    save_file.write(file_text)
    save_file.close()


def closefile():
    if messagebox.askokcancel(title="Close the window", message="Do you want to exit?"):
        window.destroy()


# function for edit menu
def copy_to_clipboard():
    # Get the currently selected text
    selected_text = text_area.get("sel.first", "sel.last")

    if selected_text:
        # Copy the selected text to the clipboard
        clipboard.copy(selected_text)
    else:
        messagebox.showinfo("Info", "No text selected to copy.")


def paste():
    # paste_text = copy_to_clipboard
    pass

window = Tk()
menubar = Menu(window)
window.config(menu=menubar)


filemenu = Menu(menubar, tearoff=0)
menubar.add_cascade(label="File", menu=filemenu)
filemenu.add_command(label="Open", command=openfile)
filemenu.add_command(label="Save", command=savefile)
filemenu.add_separator()
filemenu.add_command(label="Close", command=closefile)
menubar.add_separator()
editmenu = Menu(menubar, tearoff=0)
menubar.add_cascade(label="Edit", menu=editmenu)
editmenu.add_command(label="Copy", command=copy_to_clipboard)
editmenu.add_command(label="Paste", command=paste)
text_area = Text(window,
                 font=("Times New Roman", 14),
                 width=100,
                 height=40,
                 padx=10,
                 pady=10)
text_area.pack()

error_label = Label(window)
error_label.pack()
window.mainloop()
