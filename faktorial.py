import tkinter as tk

from functools import reduce

window=tk.Tk()

window.title('First Step')

window.geometry('400x500')

def faktorial():
    eded=int(eded_entry.get())
    cavab=reduce(lambda a, b: a*b, [i for i in range(1, eded+1)])
    print(cavab)
    
eded_label=tk.Label(window, text='Ededi daxil edin: ')
eded_label.grid(row=0, column=0)
eded_entry=tk.Entry(window)
eded_entry.grid(row=0, column=1)

duyme=tk.Button(window, text='Faktorial', command=faktorial)
duyme.grid(row=1, column=2)

window.mainloop()