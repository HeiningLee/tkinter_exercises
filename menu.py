# 菜单
import tkinter as tk


class GUI:
    def __init__(self, master):
        self.mbar = tk.Frame(master)
        cmdbutton = self.makeCommandButton(self.mbar)
        casbutton = self.makeCascadeButton(self.mbar)




    def makeCommandButton(self, master):
        cmdbtn = tk.Menubutton(master, text='Button Command',underline=0)
        cmdbtn.pack(side='left',padx=5)
        cmdbtn.menu = tk.Menu(cmdbtn)
        cmdbtn.menu.add_command(label='menulist1', )



    def makeCascadeButton(self):