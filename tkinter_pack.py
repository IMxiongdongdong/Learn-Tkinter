import tkinter as tk

window = tk.Tk()
window.title('My Window')
window.geometry('400x200')

# tk.Label(window, text=1).pack(side='top')
# tk.Label(window, text=1).pack(side='bottom')
# tk.Label(window, text=1).pack(side='left')
# tk.Label(window, text=1).pack(side='right')

# for i in range(4):
#     for j in range(3):
#         tk.Label(window, text=1).grid(row=i, column=j,
#                                       padx=10, pady=10)
#pad代表距离扩展
tk.Label(window, text=1).place(x=10, y=100, anchor='nw')

window.mainloop()