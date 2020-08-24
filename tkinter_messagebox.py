import tkinter as tk
from tkinter import messagebox

window = tk.Tk()
window.title('my window')
window.geometry('400x200')

def hit_me():
    # tk.messagebox.showinfo(title='hi', message='haha')
    # tk.messagebox.showwarning(title='hi', message='nono')
    # tk.messagebox.showerror(title='hi', message='nono')
    # tk.messagebox.askquestion(title='hi', message='haha')
    # tk.messagebox.askyesno(title='hi', message='haha')
    tk.messagebox.askretrycancel(title='hi', message='haha')

b = tk.Button(window, text='hit me', command=hit_me)
b.pack()

window.mainloop()