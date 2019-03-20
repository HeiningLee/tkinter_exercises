# 用 Checkbutton 实现对所选的内容的打印
import tkinter as tk


class GUI:
    def __init__(self, master):
        # 两个Checkbutton，各有自己的Var对象，这里用一个list存两个Var。
        self.sv = []
        self.sv.append(tk.StringVar())
        self.sv.append(tk.StringVar())

        # 分别设置两个Checkbutton的on值和off值，并且与Var对象做关联
        cb1 = tk.Checkbutton(master, text='checkbutton1',
                             onvalue='cb1 on',
                             offvalue='cb1 off',
                             variable=self.sv[0])
        cb1.pack()
        cb2 = tk.Checkbutton(master, text='checkbutton2',
                             onvalue='cb2 on',
                             offvalue='cb2 off',
                             variable=self.sv[1])
        cb2.pack()
        # 初始化Var对象
        self.sv[0].set('cb1 start')
        self.sv[1].set('cb2 start')
        # 搞一个按钮来输出Var对象的值
        btn = tk.Button(master, text='ok',
                        width=30,
                        command=self.sitrep)
        btn.pack()

    def sitrep(self):
        for i in self.sv:
            print(i.get())
        print('\n')


root = tk.Tk()
GUI(root)
root.mainloop()