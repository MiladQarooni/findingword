from tkinter import *
from tkinter import ttk
from tkinter import filedialog
from tkinter import messagebox as msg
import re


# Create the main application window
app = Tk()
app.title("File Picker App")
app.geometry('500x100')
right = int(app.winfo_screenwidth() / 2 - 400 / 2)
down = int(app.winfo_screenheight() / 2 - 200 / 2)
app.geometry('+{}+{}'.format(right, down))
app.resizable(0, 0)
app.iconbitmap('images/login.ico')

def open_file():
    file_path = filedialog.askopenfilename()
    if file_path:
        label.config(text="Selected File: " + file_path)
        global selected_file_path
        selected_file_path = file_path
def countword():
    try:
        file=open(selected_file_path,'r',encoding='utf-8')
        content = file.read()
        c = content.count('را')
        msg.showinfo("Character Count", f"Character count: {c}")
        file.close()
    except FileNotFoundError:
        msg.showerror("Error", "No file selected")

# Create a label to display the selected file path
label = Label(app, text="Selected File: ")
label.grid(row=0, column=0, padx=10, pady=10)

# Create a button to open the file dialog
button = Button(app, text="Open File", command=open_file)
button.grid(row=0, column=1, padx=10, pady=10)

labelchar = Label(app, text="character count: ")
labelchar.grid(row=1, column=0, padx=10, pady=10)

# Create a button to open the file dialog
buttonchar = ttk.Button(app, text="how many word", command=countword)
buttonchar.grid(row=1, column=1, padx=10, pady=10)

# Run the application
app.mainloop()






