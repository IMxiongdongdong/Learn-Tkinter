import tkinter as tk

window = tk.Tk()
window.title('my window')
window.geometry('400x400')

def print_selection():
    l.config(text='you have selected '+var.get())#Label的所有参数都可改变

var = tk.StringVar()
l = tk.Label(window, bg='yellow', width=20, text='empty')
l.pack()

r1 = tk.Radiobutton(window, text='option A', variable=var, value='A', command=print_selection)
r1.pack()
r2 = tk.Radiobutton(window, text='option B', variable=var, value='B', command=print_selection)
r2.pack()

window.mainloop()