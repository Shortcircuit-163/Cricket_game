import tkinter as tk
from tkinter import *
from tkinter.ttk import *
from PIL import ImageTk, Image
import csv
from tkinter import ttk 

def shop(name, username):
    class ScrollBar:
        def __init__(self):
            shp = tk.Tk()
            shp.title("shop")
            shp.geometry('800x600')
            shp.resizable(False, False)
            # shp.configure(background='light grey')
            ph1 = tk.PhotoImage(file=r'images\home\quicket.png')
            shp.iconphoto(True, ph1)

            style = ttk.Style()
            style.configure('TNotebook.Tab', padding=[20, 10])

            tabControl = ttk.Notebook(shp)
        
            tab1 = ttk.Frame(tabControl) 
            tab2 = ttk.Frame(tabControl)
            tab3 = ttk.Frame(tabControl)
            tab4 = ttk.Frame(tabControl) 
            
            tabControl.add(tab1, text ='Batsmen') 
            tabControl.add(tab2, text ='Bowlers') 
            tabControl.add(tab3, text ='All Rounders') 
            tabControl.add(tab4, text ='WK Keepers') 
            tabControl.pack(expand = 1, fill ="both") 
            
            canvas1 = Canvas(tab1)
            canvas1.pack(side=LEFT, fill=BOTH, expand=True)
            
            scrollbar1 = Scrollbar(tab1, orient=VERTICAL, command=canvas1.yview)
            scrollbar1.pack(side=RIGHT, fill=Y)
            
            canvas1.configure(yscrollcommand=scrollbar1.set)
            canvas1.bind('<Configure>', lambda e: canvas1.configure(scrollregion=canvas1.bbox("all")))
            
            # Create a frame inside the canvas to hold the content
            frame = Frame(canvas1)
            canvas1.create_window((0, 0), window=frame, anchor="nw")
            
            # Add content to the frame
            for i in range(50):
                ttk.Label(frame, text=f"Batsman {i+1}").pack(padx=30, pady=5)

            ttk.Label(tab2, text ="Lets dive into the world of computers").grid(column = 0, row = 0,  padx = 30, pady = 30) 

            shp.mainloop()

    scr = ScrollBar()

# Example usage of the shop function
shop('Shop Name', 'Username')
