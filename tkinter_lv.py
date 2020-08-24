import tkinter as tk

window = tk.Tk()
window.title('预言家')
window.geometry('400x200')

var = tk.StringVar()
l = tk.Label(window, textvariable=var, bg='green', font=('Arial',12), width=15, height=4)
l.pack()

on_hit = False
def hit_me():
    global on_hit
    if on_hit == False:
        on_hit = True
        var.set('郑建道')
    else:
        on_hit = False
        var.set('')
b = tk.Button(window, text='点击查看谁会被绿', width=15, height=4, command=hit_me)
b.pack()

window.mainloop()