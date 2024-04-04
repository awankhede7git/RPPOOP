from tkinter import *

def submit_form():
  name = name_entry.get()
  age = int(age_entry.get())
  data_array.append({"name": name, "age": age})
  # Clear form after submission (optional)
  name_entry.delete(0, END)
  age_entry.delete(0, END)

window = Tk()
window.title("Data Collection Form")

name_label = Label(window, text="Name:")
name_label.pack()

name_entry = Entry(window)
name_entry.pack()

age_label = Label(window, text="Age:")
age_label.pack()

age_entry = Entry(window)
age_entry.pack()

submit_button = Button(window, text="Submit", command=submit_form)
submit_button.pack()

data_array = []

window.mainloop()
