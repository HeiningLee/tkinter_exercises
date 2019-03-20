import tkinter as tk


class GUI:
    def __init__(self, master):

        lb = tk.Label(master, text='Select your favorite language:')
        lb.pack()

        self.var = tk.IntVar()
        frmbuttons = tk.Frame(master, relief='ridge', borderwidth=2)
        for txt, val in [('python', 1), ('C++', 2), ('Ruby', 3)]:
            tk.Radiobutton(frmbuttons, text=txt, value=val, variable=self.var).pack(padx=5, pady=5)
        frmbuttons.pack(pady=5)
        self.var.set(2)
        btn = tk.Button(master, text='OK', command=self.printoption, width=30)
        btn.pack(pady=5)

    def printoption(self):
        print('Your favorite language is ' + str(self.var.get()))


root = tk.Tk()
root.geometry('300x200')
GUI(root)

root.mainloop()
