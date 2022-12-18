import tkinter as tk

reg_win=tk.Tk()

reg_win.title('Registration')
reg_win.geometry('400x500')

#username

username_l=tk.Label(reg_win, text='Username')
username_l.grid(row=0, column=0)

username_e=tk.Entry(reg_win)
username_e.grid(row=0, column=1)

#password

password_l=tk.Label(reg_win, text='Password')
password_l.grid(row=1, column=0)

password_e=tk.Entry(reg_win)
password_e.grid(row=1, column=1)

reg_win.mainloop()