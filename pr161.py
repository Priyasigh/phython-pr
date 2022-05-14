from os import name
from tkinter import *
import tkinter
import tkinter.messagebox as tm
import csv

win=tkinter.Tk()

def click():
    username = entry_username.get()
    password = entry_password.get()

    with open('data.csv') as csvfile:
        reader = csv.DictReader(csvfile)
        database = []
        for row in reader:
            database.append(dict(username=row['username'], password=row['password']))

    for row in database:
        username_file = row['username']
        name=username_file.split('@')
        password_file = row['password']

        if username == username_file and password == password_file:
             tm.showinfo("Login info", f"Welcome {name[0]}")
             break
    else:
         tm.showerror("Login error", "Incorrect username or password")

label_username = Label(win, text="Username")
label_password = Label(win, text="Password")

entry_username = Entry(win)
entry_password = Entry(win, show="*")

label_username.grid(row=0, sticky=E)
label_password.grid(row=1, sticky=E)
entry_username.grid(row=0, column=1)
entry_password.grid(row=1, column=1)
logbtn = Button(win, text="Login",command=click)
logbtn.grid(columnspan=2)

win.mainloop()