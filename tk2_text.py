import tkinter as tk


root = tk.Tk()
root.title("插入字符")

# locate the window
win_width = 800
win_height = 200
screen_width = root.winfo_screenwidth()
screen_height = root.winfo_screenheight()
print("Screen Width: " + str(screen_width))
print("Screen Height: " + str(screen_height))
win_x = screen_width/2 - win_width/2
win_y = screen_height/3 - win_height/3
root.geometry('%dx%d+%d+%d' % (win_width, win_height, win_x, win_y))

txt = tk.Text()
txt.pack(side="left", fill='y')
txt.tag_add('tag1', 1.0, 2.0)
txt.tag_config('tag1', foreground='red', background='blue', font=('monospace', 25, 'italic', 'bold'))
txt.mark_set('mk1', 1.0)
txt.mark_set('mk2', 3.2)
txt.insert('mk1', 'This is a Text box.', 'tag1')
txt.insert('mk2', 'This is a Text box.', 'tag1')
txt.see('end')

scr = tk.Scrollbar()
scr.pack(side="left", fill='y')

scr["command"] = txt.yview
txt["yscrollcommand"] = scr.set




root.mainloop()