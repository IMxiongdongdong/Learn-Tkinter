import tkinter as tk

window = tk.Tk()
window.title('my window')
window.geometry('400x400')

l = tk.Label(window, bg='yellow', width=20, text='')
l.pack()

counter = 0
def do_job():
    global counter
    l.config(text='do'+str(counter))
    counter += 1

menubar = tk.Menu(window)
filemenu = tk.Menu(menubar, tearoff=0)
menubar.add_cascade(label='File', menu=filemenu)
filemenu.add_cascade(label='Open', command=do_job)
filemenu.add_separator()
filemenu.add_cascade(label='Exit', command=window.quit)

window.config(menu=menubar)
window.mainloop()
