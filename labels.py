import tkinter as tk

root = tk.Tk()

lb1 = tk.Label(root, text="I mean, it's a little confusing for me "
                          "when you say 'dog kennel' if you want a mattress. "
                          "why not just say 'mattress'?",
               wraplength=300, justify='left').pack(pady=10)
frm1 = tk.Frame(root)
lb2 = tk.Label(frm1, text="It's not working, we need more!", relief='raised')
lb2.pack(side='left', padx=5, pady=5)
lb3 = tk.Label(frm1, text="I'm not coming out!", relief='sunken')
lb3.pack(side='right', padx=5, pady=5)
frm1.pack(pady=10)

# 给出文件名和浮雕样式的数组
images = [('image1', 'raised'), ('image2', 'sunken')]
frm2 = tk.Frame(root)

# 从文件新建PhotoImage对象，并将其运用到Label中，共2幅图。
img1 = tk.PhotoImage(file='images/%s.png' % images[0][0])
tk.Label(frm2, image=img1, relief='%s' % images[0][1]).pack(side='left', padx=5)
img2 = tk.PhotoImage(file='images/%s.png' % images[1][0])
tk.Label(frm2, image=img2, relief='%s' % images[1][1]).pack(side='right', padx=5)
frm2.pack()



root.mainloop()