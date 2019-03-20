import tkinter as tk


# 将整个GUI封装为一个类
class GUI:
    # 在初始化函数中就把需要的控件构建好，留出GUI所在的主窗口或toplevel窗口接口
    def __init__(self, master=None):
        # 生成一个None队列，None可以随后被替换为任意实例，这里是frame对象：5层frame。
        frms = [None]*5
        # 构建5层frame，每层frame内部依次排列label和6种relief的按钮。
        for n in range(5):
            # 构建一层frame
            frms[n] = tk.Frame(master)
            # 构建一个标签
            lb = tk.Label(frms[n], text="bd = %d" % n)
            lb.pack(side='left')
            # 构建6个按钮
            for rlf in ['flat', 'raised', 'sunken', 'ridge', 'groove', 'solid']:
                # lambda函数的妙用**
                btn = tk.Button(frms[n], text=rlf, relief=rlf, borderwidth=n,
                                command=lambda r=rlf, b=n: self.showborder(r, b),
                                width=10)
                btn.pack(side='left', padx=10-n, pady=5-n)
            frms[n].pack()

    # 方法：显示浮雕效果和边框宽度
    def showborder(self, rlf, bw):
        print('%s:%d' % (rlf, bw))


# 创建主窗口实例
root = tk.Tk()
# 将GUI应用到主窗口
app = GUI(root)
# 主循环
root.mainloop()
