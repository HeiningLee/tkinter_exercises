import tkinter as tk


root = tk.Tk()


def optionclicked():
    print('option clicked!')


# 基于root（或者toplevel对象）建立菜单栏对象
mbar = tk.Menu(root)
# 基于菜单栏对象，建立一级菜单
menu_1 = tk.Menu(mbar, tearoff=0)
menu_2 = tk.Menu(mbar, tearoff=0)
menu_3 = tk.Menu(mbar, tearoff=0)
# 基于一级菜单，建立次级子菜单，这里准备将子菜单入口安排到第二个菜单的第一项。
menu_2_1 = tk.Menu(menu_2, tearoff=0)

# 开始设置级联关系，第一级菜单是菜单栏的级联，用选项menu设定对应的菜单对象
mbar.add_cascade(label='M1', menu=menu_1)
mbar.add_cascade(label='M2', menu=menu_2)
mbar.add_cascade(label='M3', menu=menu_3)

# 为菜单添加选项，设定命令响应函数
menu_1.add_command(label='option 1-1', command=optionclicked())
menu_1.add_command(label='option 1-2', command=optionclicked())
menu_1.add_command(label='option 1-3', command=optionclicked())
# 为菜单2添加级联项
menu_2.add_cascade(label='option 2-1', menu=menu_2_1)
# 为子菜单添加选项
menu_2_1.add_command(label='option 2-1-1',
                     command=optionclicked())
menu_2_1.add_command(label='option 2-1-2',
                     command=optionclicked())
menu_2_1.add_command(label='option 2-1-2',
                     command=optionclicked())
# 为菜单2添加普通选项
menu_2.add_command(label='option 2-2', command=optionclicked())
menu_2.add_command(label='option 2-3', command=optionclicked())

# 为菜单3添加普通选项
menu_3.add_command(label='option 3-1', command=optionclicked())
menu_3.add_command(label='option 3-2', command=optionclicked())
menu_3.add_command(label='option 3-3', command=optionclicked())
root['menu'] = mbar

root.mainloop()
