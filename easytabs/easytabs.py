__author__ = "Mehmet Eren Inanir"
__email__ = "mail@easytabs.com"
__status__ = "planning"

from doctest import master
import os
from tkinter import *

class easytabs:
    def newtab():
        master = Tk()
        master.mainloop()
    def tabsize(tabheight=False, tabwidth=False):
        canvas = Canvas(master, height=tabheight, width=tabwidth)
        canvas.pack()
    def tabframe(tabrelx=False, tabrely=False, tabrelheight=False, tabrelwidth=False, bgcolor=False):
        frame = Frame(master, bg=bgcolor)
        frame.place(relx=tabrelx, rely=tabrely, relheight=tabrelheight, relwidth=tabrelwidth)


