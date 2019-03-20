import tkinter as tk


class GUI:
    def __init__(self, master):

        lb = tk.Label(master, text='Select your favorite language:')
        lb.pack()

        self.svar = tk.StringVar()
        for txt, val in [('python', 'python'), ('C++', 'C++'), ('Ruby', 'Ruby')]:
            rb = tk.Radiobutton(master, text=txt, value=val, variable=self.svar, anchor='w')
            rb['indicatoron'] = 0
            rb.pack(padx=5, pady=5)
        self.svar.set('C++')
        btn = tk.Button(master, text='OK', command=self.printoption)
        btn.pack(pady=5)

    def printoption(self):
        print('Your favorite language is ' + self.svar.get())


root = tk.Tk()
root.geometry('300x200')
GUI(root)

root.mainloop()
