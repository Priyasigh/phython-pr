# import the module tkinter for gui
# from multiprocessing.sharedctypes import Value
import tkinter as tk 
import tkinter.messagebox as mb


from numpy import place
# make instance of TK
root = tk.Tk()
# create window
canvas1 = tk.Canvas(root, width=400, height=300,  relief='raised')
canvas1.pack()
# create the  input label

label1 = tk.Label(root, text='Login page')
label1.config(font=('helvetica', 14))

# create canvas of label1
canvas1.create_window(200, 20, window=label1)


label3 = tk.Label(root, text='Enter Your Username:')
label3.config(font=('helvetica', 10))
label2 = tk.Label(root, text='Enter your Password:')
label2.config(font=('helvetica', 10))

canvas1.create_window(200, 50, window=label3)
canvas1.create_window(200, 100, window=label2)
usernameEntry=tk.Entry(root)
canvas1.create_window(200,75,window=usernameEntry)
entry1 = tk.Entry(root,show='*')
canvas1.create_window(200, 125, window=entry1)


def getSquareRoot():
    u1=usernameEntry.get()
    x1 = entry1.get()
    with open('data.csv', 'r')as f:
        data = f.readlines()
        for i,value in enumerate(data):
            username=value.split(',')[0].split('@')[0]
            password=value.split(',')[1]
            if i == 0:
                continue
            if x1 == password and u1==username:
                 mb.showinfo("Login info", f"Welcome {username}")
                 break

        else: mb.showerror("Login error", f"incorrect username and password")
button1 = tk.Button(text='Login', command=getSquareRoot,
                    bg='lightblue', fg='white', font=('helvetica', 10, 'bold'))
canvas1.create_window(200, 170, window=button1)

root.mainloop()