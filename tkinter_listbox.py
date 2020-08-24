import tkinter as tk

window = tk.Tk()
window.title('翻牌器')
window.geometry('400x400')

var1 = tk.StringVar()
l = tk.Label(window, bg='yellow', width=15, height=2, textvariable=var1)
l.pack()

def print_selection():
    value = lb.get(lb.curselection())
    var1.set(value)

b1 = tk.Button(window, text='点击选择谁侍寝', width=15, height=2, command=print_selection)
b1.pack()

var2 = tk.StringVar()
var2.set(('羊', '汤圆'))

lb = tk.Listbox(window, listvariable=var2)
lb.pack()

window.mainloop()

# import tkinter as tk
#
# window = tk.Tk()
# window.title('My window')
# window.geometry('400x200')
#
# var1 = tk.StringVar()
# l = tk.Label(window, bg='yellow', width=15, height=2, textvariable=var1)
# l.pack()
#
# def print_selection():
#     value = lb.get(lb.curselection())
#     var1.set(value)
#
# b1 = tk.Button(window, text='print selection', width=15, height=2, command=print_selection)
# b1.pack()
#
# var2 = tk.StringVar()
# var2.set((11, 22, 33, 44))
#
# lb = tk.Listbox(window, listvariable=var2)
# list_items = [1, 2, 3, 4]
# for item in list_items:
#     lb.insert('end', item)
# lb.insert(1, 'first')
# lb.insert(2, 'second')
# lb.delete(2)
# lb.pack()
#
# window.mainloop()