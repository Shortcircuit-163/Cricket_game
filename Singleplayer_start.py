import tkinter as tk
from tkinter.ttk import *
from PIL import ImageTk, Image
import csv


def start_match_singleplayer(user):
    
    sm = tk.Tk()
    sm.title("Quicket-Start Match")
    sm.geometry('800x800')
    # sm.resizable(False, False)
    # sm.configure(background='light grey')
    p1 = tk.PhotoImage(file=r'images\home\quicket.png')
    sm.iconphoto(True, p1)
    

    sm.grid_columnconfigure(0, weight=1)
    sm.grid_columnconfigure(1, weight=1)
    sm.grid_columnconfigure(2, weight=1)

    greeting = "Hello " + user + "!"
    heading = Label(sm, text=greeting, background='', font=('Times New Roman', 50, 'bold'))
    heading.grid(row=0, column=1)
