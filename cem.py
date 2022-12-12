import tkinter as tk

def topla_func():
    eded1=int(eded1_entry.get())
    eded2=int(eded2_entry.get())
    print(eded1+eded2)

window=tk.Tk()
window.title('First Step')
window.geometry('500x600')

eded1_label=tk.Label(window, text='Birinci ededi daxil edin: ')
eded1_label.grid(row=0, column=0)
eded1_entry=tk.Entry(window)
eded1_entry.grid(row=0, column=1)

eded2_label=tk.Label(window, text='Ikinci ededi daxil edin: ')
eded2_label.grid(row=1, column=0)
eded2_entry=tk.Entry(window)
eded2_entry.grid(row=1, column=1)

topla=tk.Button(window, text='Toplamaq', command=topla_func)
topla.grid(row=5, column=1)

window.mainloop()