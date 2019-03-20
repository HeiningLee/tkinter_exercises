import tkinter as tk

# 创建主窗口
root = tk.Tk()
root.title('框架实例')

frm = tk.Frame(root, relief='solid', borderwidth=1, width=300, height=150)

frm1 = tk.Frame(frm, relief='groove', borderwidth=2)
lb1 = tk.Label(frm1, text='You shot him!').pack(pady=10)
btn1 = tk.Button(frm1, text="He's dead!", state='disabled').pack(side='left', padx=5, pady=8)
btn2 = tk.Button(frm1, text="He's completely dead!").pack(side='right', padx=5, pady=8)
frm1.place(anchor='nw', relx=0.05, rely=0.1)

lb2 = tk.Label(frm, text='Self-defence against fruit', bg='blue')
lb2.place(anchor='w', relx=0.1, rely=0.1)
frm.pack()
root.mainloop()
