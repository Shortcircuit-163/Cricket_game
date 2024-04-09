import tkinter as tk
from tkinter.ttk import *
from PIL import ImageTk, Image
import csv
from Singlelayer_start import start_match_singleplayer as start

def open_singleplayer():
    
    sp = tk.Tk()
    sp.title("Quicket-Singleplayer")
    sp.geometry('800x800')
    # sp.resizable(False, False)
    # sp.configure(background='light grey')
    p1 = tk.PhotoImage(file=r'images\home\quicket.png')
    sp.iconphoto(True, p1)
    
    sp.grid_columnconfigure(0, weight=1)
    sp.grid_columnconfigure(1, weight=1)
    sp.grid_columnconfigure(2, weight=1)

    # sp.grid_rowconfigure(0, weight=1)

    heading = Label(sp, text="Choose an account", background='', font=('Times New Roman', 50, 'bold', 'underline'))
    heading.grid(row=0, column=1)

    name_var=tk.StringVar()
    passw_var=tk.StringVar()
    

    def submit():
 
        name=name_var.get()
        password=passw_var.get()
        
        print("Username input: " + name)
        print("Password input: " + password)

        with open(r'Data\usernames.csv') as passwords:
            pass_reader = csv.reader(passwords, delimiter=',')
            for row in pass_reader:
                if row[0] == name:
                    if row[1] == password:
                        print("correct password")
                        sp.destroy()
                        start(name)
                    else:
                        print("wrong password")
                        tk.messagebox.showerror("Incorrect password", "Please try again")
                        return
                    
    user_pass_frame = Frame(sp)
    user_pass_frame.grid(row=1, column=1, pady =100)


    name_label = tk.Label(user_pass_frame, text = 'Username', font=('calibre',20, 'bold'))
    name_label.grid(row=0, column=0)
    
    names = []
    with open(r'Data\usernames.csv') as users:
        user_reader = csv.DictReader(users, delimiter=',')
        for row in user_reader:
            for username in row.values():
                names.append(username)
                break
    name_dropdown = Combobox(user_pass_frame, textvariable=name_var, values=names, font=('calibre',19,'bold'))
    name_dropdown.grid(row=0, column=1)
    

    passw_label = tk.Label(user_pass_frame, text = 'Password', font = ('calibre',20,'bold'))
    passw_label.grid(row=1, column=0)
    
    passw_entry=tk.Entry(user_pass_frame, textvariable = passw_var, font = ('calibre',20,'normal'), show = '*')
    passw_entry.grid(row=1, column=1)
    

    sub_btn=tk.Button(user_pass_frame,text = 'Submit', command = submit, height=2 , width=10)
    sub_btn.grid(row=2, column=1, pady=10)



    
    sp.mainloop()

