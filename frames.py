## -*- coding: utf-8 -*-
from tkinter import Tk, Label, Frame
# 使用TK创建root对象，主窗口
root = Tk()

for relief in ['flat', 'raised', 'sunken', 'ridge', 'groove', 'solid']:
    f1 = Frame(root, relief=relief, borderwidth=2)
    label1 = Label(f1, text=relief)
    label1.pack(side='left')
    f1.pack(side='left', padx=5, pady=5)

root.mainloop()
