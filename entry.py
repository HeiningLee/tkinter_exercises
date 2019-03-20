import tkinter as tk


class GUI:

    def __init__(self, master=None):
        self.sv = tk.StringVar()
        self.sv.set('Hello World!')
        self.sv.trace('w', self.varchanged)
        self.ety = tk.Entry(master, textvariable=self.sv, width=30)
        self.ety.pack(padx=10, pady=10)

        self.btn = tk.Button(master, text='print entry', command=self.prt)
        self.btn.pack(pady=10)


    def prt(self):
        print(self.sv.get())

    def varchanged(self):
        print('Value Changed')


root = tk.Tk()
root.title('An Entry')
root.geometry('300x200')

GUI(root)
root.mainloop()
