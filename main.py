import tkinter as tk
from tkinter import *
from tkinter.ttk import *
from PIL import ImageTk, Image
from tkinter import filedialog
from tkinter import messagebox

win = tk.Tk()
win.title("Quicket")
win.geometry('1600x720')
win.resizable(height=False, width=False)
p1 = PhotoImage(file='quicket.png')
win.iconphoto(True, p1)

heading = Label(win, text="Quicket", font=('Times New Roman', 50, 'bold'))
heading.grid()
play_mode = Label(win, text='-Choose Game Mode-', font=('Century Gothic', 30, 'underline'))
play_mode.place(relx=0.1,
                rely=0.2,
                anchor='nw')

quicket_image = PhotoImage(file='quicket.png')
quicket_label = Label(win, image=quicket_image)
quicket_label.place(relx=0.1,
                    rely=0,
                    anchor='e')

style1_btn_gamemode = Style()
style1_btn_gamemode.configure('A.TButton', font=('calibri', 50, 'bold', 'underline'), foreground='red')
photo1 = PhotoImage(file='singleplayer.png')
btn1 = Button(win, image=photo1, style='A.TButton', command=None)
btn1.grid(row=2, column=0, pady=2)

style2_btn_gamemode = Style()
style2_btn_gamemode.configure('B.TButton', font=('calibri', 50, 'bold', 'underline'), foreground='orange')
photo2 = PhotoImage(file='multiplayer.png')
btn2 = Button(win, image=photo2, style='B.TButton', command=None)
btn2.grid(row=3, column=0, pady=2)
win.mainloop()
