import tkinter as tk
from tkinter.ttk import *
from PIL import ImageTk, Image
import csv

def signup_window():
    sgnp = tk.Tk()
    sgnp.title("Quicket-Signup")
    sgnp.geometry('800x800')
    # sgnp.resizable(False, False)
    # sgnp.configure(background='light grey')
    ph1 = tk.PhotoImage(file=r'images\home\quicket.png')
    sgnp.iconphoto(True, ph1)

    sgnp.grid_columnconfigure(0, weight=1)
    sgnp.grid_columnconfigure(2, weight=1)

    heading = Label(sgnp, text="Create quicket account", font=('Times New Roman', 50, 'bold', 'underline'))
    heading.grid(row=0, column=1, pady = 50)

    signup_frame = tk.Frame(sgnp)
    signup_frame.grid(row=1, column=1, pady = 100)

    name_var=tk.StringVar()
    username_var=tk.StringVar()
    passw_var=tk.StringVar()

    def signup_append():
        name = name_var.get()
        username = username_var.get()
        password = passw_var.get()

        new_player_credentials = [username, password]

        def check_username_taken():
            with open(r'Data\usernames.csv', 'a+') as add_user:
                add_user.seek(0)
                user_reader = csv.reader(add_user, delimiter=',')
                for row in user_reader:
                    if row[0] == username:
                        print("Username already taken")
                        tk.messagebox.showerror("Username taken", "Please try again")
                        return True
                
                return False
        
        if check_username_taken() == False:
            with open(r'Data\usernames.csv', 'a+', newline='') as add_user:
                writer = csv.writer(add_user)
                writer.writerow(new_player_credentials)


            path1 = r'Data\users\data_' + username + '.csv'

            with open(path1, 'w', newline='') as player_data:
                datawriter = csv.writer(player_data)
                datawriter.writerow(['Name', 'Batsmen owned', 'Bowlers owned','wicket keepers owned', 'all rounders owned', 'Wickets', 'Runs', 'Economy', 'Innings', 'Batting Average', 'Bowling Average', 'Batting Overs', 'Bowling Overs', 'Total Overs'])
            with open(path1, 'a', newline='') as append_player_data:
                datawriter = csv.writer(append_player_data)
                datawriter.writerow([name, 4, 3, 1, 3, 0, 0, 0, 0, 0, 0, 0, 0, 0])

            path2 = r'Data\users\player_data_' + username + '.csv'
            with open(path2, 'w+', newline='') as players:
                player_data_writer = csv.writer(players)
                player_data_writer.writerow(['batsmen names', 'bowler names', 'all rounder names', 'wicket keeper names'])
                # ADD STARTERPACK HERE

    name_entry_label = tk.Label(signup_frame, text = 'Enter your name:', font = ('calibre',20,'bold'))
    name_entry_label.grid(row=0, column=0)
    
    name_entry = tk.Entry(signup_frame, textvariable = name_var, font = ('calibre',20,'normal'))
    name_entry.grid(row=0, column=1)

    username_label = tk.Label(signup_frame, text = 'Enter username:', font = ('calibre',20,'bold'))
    username_label.grid(row=1, column=0)

    username_entry = tk.Entry(signup_frame, textvariable = username_var, font = ('calibre',20,'normal'))
    username_entry.grid(row=1, column=1)

    passw_label = tk.Label(signup_frame, text = 'Enter password:', font = ('calibre',20,'bold'))
    passw_label.grid(row=2, column=0)

    passw_entry=tk.Entry(signup_frame, textvariable = passw_var, font = ('calibre',20,'normal'), show = '*')
    passw_entry.grid(row=2, column=1)

    signup = tk.PhotoImage(file=r'images\singleplayer\signup.png')
    signup_btn = signup.subsample(2, 2)
    signup_button=tk.Button(signup_frame,image=signup_btn, command = signup_append, borderwidth=0)
    signup_button.grid(row=3, column=1, pady=30)    


    sgnp.mainloop()