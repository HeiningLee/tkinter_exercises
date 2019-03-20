import tkinter as tk


root = tk.Tk()
root.title("一个最简单的窗口")

# locate the window
win_width = 300
win_height = 200
screen_width = root.winfo_screenwidth()
screen_height = root.winfo_screenheight()
print("Screen Width: " + str(screen_width))
print("Screen Height: " + str(screen_height))
win_x = screen_width/2 - win_width/2
win_y = screen_height/3 - win_height/3
root.geometry('%dx%d+%d+%d' % (win_width, win_height, win_x, win_y))

txtvar = tk.StringVar()


label = tk.Label(textvar=txtvar, bg='blue', width=30, height=10)
label.pack()

button_on = False


def hit_btn():
    global button_on
    if button_on is False:
        button_on = True
        txtvar.set('Hello World!')
    elif button_on is True:
        button_on = False
        txtvar.set('')
    # print(button_on)


btn = tk.Button(text='Wake me up', width=30, height=10, command=hit_btn)
btn.pack()


root.mainloop()