import tkinter as tk


root = tk.Tk()
root.title('A simple entry')
root.geometry('300x100+50+50')

lb = tk.Label(root, text='Enter:')
lb.pack(side='left', padx=10)

e = tk.StringVar()  # 创建StringVar字符串变量
ety = tk.Entry(root, width=30, textvariable=e)
ety.pack(side='left', padx=10)
e.set('This is an entry!')

root.mainloop()
