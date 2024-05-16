import tkinter as tk
from tkinter.ttk import *
from PIL import ImageTk, Image
import csv


def start_match_singleplayer(name):
    
    sm = tk.Tk()
    sm.title("Quicket-Start Match")
    sm.geometry('900x800')
    # sm.resizable(False, False)
    # sm.configure(background='light grey')
    p1 = tk.PhotoImage(file=r'images\home\quicket.png')
    sm.iconphoto(True, p1)
    

    sm.grid_columnconfigure(0, weight=1)
    sm.grid_columnconfigure(1, weight=1)
    sm.grid_columnconfigure(2, weight=1)

    greeting = "Hello " + name + "!"
    heading = Label(sm, text=greeting, background='', font=('Times New Roman', 50, 'bold'))
    heading.grid(row=0, column=1)

    player_info = tk.Frame(sm)
    player_info.grid(row=1, column=1, pady = 100)

    def return_playerdata():
        data_path = r'Data\user_data.csv'
        with open(data_path) as player_data:
            user_reader = csv.reader(player_data, delimiter=',')
            for row in user_reader:
                if row[0] == name:
                    batsmen_owned = row[3]
                    bowlers_owned = row[4]
                    wicket_keepers_owned = row[5]
                    all_rounders_owned = row[6]
                    wickets = row[7]               
                    runs = row[8]              
                    economy = row[9]              
                    innings = row[10]               
                    batting_average = row[11]               
                    bowling_average = row[12]              
                    batting_overs = row[13]               
                    bowling_overs = row[14]              
                    total_overs = row[15]
                    all_data = [batsmen_owned, bowlers_owned, wicket_keepers_owned, all_rounders_owned, wickets, runs, economy, innings, batting_average, bowling_average, batting_overs, bowling_overs, total_overs]
                    return all_data

    batsmen_owned, bowlers_owned, wicket_keepers_owned, all_rounders_owned, wickets, runs, economy, innings, batting_average, bowling_average, batting_overs, bowling_overs, total_overs = return_playerdata()[0], return_playerdata()[1], return_playerdata()[2], return_playerdata()[3], return_playerdata()[4], return_playerdata()[5], return_playerdata()[6], return_playerdata()[7], return_playerdata()[8], return_playerdata()[9], return_playerdata()[10], return_playerdata()[11], return_playerdata()[12]

    batsmen = Label(player_info, text='Batsmen', background='', font=('Times New Roman', 20, 'bold'))
    batsmen.grid(row=0, column=0)
    batsmen_value = Label(player_info, text=batsmen_owned, font=('Times New Roman', 30, 'bold'))
    batsmen_value.grid(row=1, column=0)

    bowlers = Label(player_info, text='Bowlers', background='', font=('Times New Roman', 20, 'bold'))
    bowlers.grid(row=0, column=1)
    bowlers_value = Label(player_info, text=bowlers_owned, font=('Times New Roman', 30, 'bold'))
    bowlers_value.grid(row=1, column=1)

    wicket_keepers = Label(player_info, text='Wicket Keepers', background='', font=('Times New Roman', 20, 'bold'))
    wicket_keepers.grid(row=0, column=2)
    wicket_keepers_value = Label(player_info, text=wicket_keepers_owned, font=('Times New Roman', 30, 'bold'))
    wicket_keepers_value.grid(row=1, column=2)

    all_rounders = Label(player_info, text='All Rounders', background='', font=('Times New Roman', 20, 'bold'))
    all_rounders.grid(row=0, column=3)
    all_rounders_value = Label(player_info, text=all_rounders_owned, font=('Times New Roman', 30, 'bold'))
    all_rounders_value.grid(row=1, column=3)

    wickets_label = Label(player_info, text='wickets', background='', font=('Times New Roman', 20, 'bold'))
    wickets_label.grid(row=0, column=4)
    wickets_value = Label(player_info, text=wickets, font=('Times New Roman', 30, 'bold'))
    wickets_value.grid(row=1, column=4)

    runs_label = Label(player_info, text='runs', background='', font=('Times New Roman', 20, 'bold'))
    runs_label.grid(row=2, column=0)
    runs_value = Label(player_info, text=runs, font=('Times New Roman', 30, 'bold'))
    runs_value.grid(row=3, column=0)

    economy_label = Label(player_info, text='economy', background='', font=('Times New Roman', 20, 'bold'))
    economy_label.grid(row=2, column=1)
    economy_value = Label(player_info, text=economy, font=('Times New Roman', 30, 'bold'))
    economy_value.grid(row=3, column=1)

    innings_label = Label(player_info, text='innings', background='', font=('Times New Roman', 20, 'bold'))
    innings_label.grid(row=2, column=2)
    innings_value = Label(player_info, text=innings, font=('Times New Roman', 30, 'bold'))
    innings_value.grid(row=3, column=2)

    batting_avg = Label(player_info, text='batting average', background='', font=('Times New Roman', 20, 'bold'))
    batting_avg.grid(row=2, column=3)
    batting_avg_value = Label(player_info, text=batting_average, font=('Times New Roman', 30, 'bold'))
    batting_avg_value.grid(row=3, column=3)

    bowling_avg = Label(player_info, text='bowling average', background='', font=('Times New Roman', 20, 'bold'))
    bowling_avg.grid(row=2, column=4)
    bowling_avg_value = Label(player_info, text=bowling_average, font=('Times New Roman', 30, 'bold'))
    bowling_avg_value.grid(row=3, column=4)

    batting_overs_label = Label(player_info, text='batting overs', background='', font=('Times New Roman', 20, 'bold'))
    batting_overs_label.grid(row=4, column=1)
    batting_overs_value = Label(player_info, text=batting_overs, font=('Times New Roman', 30, 'bold'))
    batting_overs_value.grid(row=5, column=1)

    bowling_overs_label = Label(player_info, text='bowling overs', background='', font=('Times New Roman', 20, 'bold'))
    bowling_overs_label.grid(row=4, column=2)
    bowling_overs_value = Label(player_info, text=bowling_overs, font=('Times New Roman', 30, 'bold'))
    bowling_overs_value.grid(row=5, column=2)

    total_overs_label = Label(player_info, text='total overs', background='', font=('Times New Roman', 20, 'bold'))
    total_overs_label.grid(row=4, column=3)
    total_overs_value = Label(player_info, text=total_overs, font=('Times New Roman', 30, 'bold'))
    total_overs_value.grid(row=5, column=3)

    sm.mainloop()

# Batsmen owned,Bowlers owned,wicket keepers owned,all rounders owned,Wickets,Runs,Economy,Innings,
# Batting Average,Bowling Average,Batting Overs,Bowling Overs,Total Overs
