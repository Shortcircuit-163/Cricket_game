import tkinter as tk
from tkinter.ttk import *
from PIL import ImageTk, Image
from tkinter import filedialog
from tkinter import messagebox

win = tk.Tk()
win.title("Quicket")
win.geometry('1366x768')
p1 = tk.PhotoImage(file='quicket.png')
win.iconphoto(True, p1)

win.grid_columnconfigure(0, weight=1)
win.grid_columnconfigure(1, weight=1)
win.grid_columnconfigure(2, weight=1)
win.grid_rowconfigure(0, weight=1)
win.grid_rowconfigure(1, weight=1)
win.grid_rowconfigure(2, weight=1)
win.grid_rowconfigure(3, weight=1)
win.grid_rowconfigure(4, weight=1)


heading = Label(win, text="Quicket", font=('Times New Roman', 50, 'bold'))
heading.grid(row=0, column=1)

quicket_image = tk.PhotoImage(file='quicket.png')
quicket_label = Label(win, image=quicket_image)
quicket_label.grid(row=1, column=1)

play_mode = Label(win, text='-Choose Game Mode-', font=('Century Gothic', 30, 'underline'))
play_mode.grid(row=2, column=1)

style1_btn_gamemode = Style()
style1_btn_gamemode.configure('A.TButton', font=('calibri', 50, 'bold', 'underline'), foreground='red')
photo1 = tk.PhotoImage(file='singleplayer.png')
btn1 = Button(win, image=photo1, style='A.TButton', command=None)
btn1.grid(row=3, column=1)

style2_btn_gamemode = Style()
style2_btn_gamemode.configure('B.TButton', font=('calibri', 50, 'bold', 'underline'), foreground='orange')
photo2 = tk.PhotoImage(file='multiplayer.png')
btn2 = Button(win, image=photo2, style='B.TButton', command=None)
btn2.grid(row=4, column=1)

win.mainloop()