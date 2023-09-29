#Libaries
import cflib.crtp
from cflib.crazyflie import Crazyflie
from cflib.crazyflie.log import LogConfig
import PySimpleGUI as sg
from colorama import Back, Fore, init
import os
#font farben fürs terminal
init(autoreset=True)

#variable für gescannte drohnen
drohne = ""
os.system("clear")
os.system("cls")

with open('Images_Pfad.txt', "r") as f:
    path = f.readline()
    print(path)
    

col1 = [
    [sg.Text("      Statistiken und Infortmation:")],
]
#layout for GUI
layout = [
    [sg.Column(col1,justification='center')],
    [sg.Text("Starte die Drohne\n\n")],
    [sg.Button("Scan",button_color = "yellow"),sg.Listbox(values=(f'{drohne}'), size=(10, 5), key='_LISTBOX_'),],
    [sg.Button("Connect",button_color = "green")],
    [sg.Button("Start",button_color = "green")],
    [sg.Button("Stop",button_color = "red")],
    [sg.Text("\n")],
    [sg.Button("movement_key_1",button_color = "grey",image_filename=path+'\\Pfeil_Oben.png', pad=((65,65),3), key="w")],
    [sg.Button("movement_key_2",button_color = "white",image_filename=path+'\\Pfeil_Links.png', pad=((10,10),3),key="a"),
     sg.Button("movement_key_4",button_color = "white",image_filename=path+'\\drohne_fliegen.png',pad=((0,0),3),key="space"),
     sg.Button("movement_key_5",button_color = "white",image_filename=path+'\\Pfeil_Rechts.png', pad=((10,10),3),key="d")],
    [sg.Button("movement_key_3",button_color = "white",image_filename=path+'\\Pfeil_Unten.png', pad=((65,65),3),key="s")],
    [sg.Button("Exit",button_color="red",pad=((000,000),3)),sg.Button("Clear terminal logs",button_color = "red")]
]
#Creating GUI and layout
window = sg.Window("Drohnen Steuerungs GUI", layout,size=(680,680),use_default_focus=False,finalize=True)
#commands to bind keys to actions
movement_key_1, movement_key_2, movement_key_3, movement_key_4, movement_key_5 = window['w'], window['a'], window['s'], window['d'], window['space'] 

window.bind("<w>","w")
window.bind("<a>","a")
window.bind("<s>","s")
window.bind("<d>","d")
window.bind("<space>","space")
#################################

#All events
while True:
    event, values = window.read()
    print(values)
    if event == sg.WINDOW_CLOSED:
        break
    elif event == "Scan": #Event to scan avaible drones
        print(f"{fy}Scanning devices...{Fore.RESET}")
        available_devices = cflib.crtp.scan_interfaces()
        uri_to_connect = available_devices
        uri_to_connect
        drohne = uri_to_connect
        window['_LISTBOX_'].update(values=drohne)
        print(f"{Fore.GREEN}Showing scanned devices")
    elif event in ("movement_key_1", "w"): #Key Event für W
         print(f'{Fore.GREEN}"W" Key Pressed') 
    elif event in ("movement_key_2", "a"): #Key Event für A
        print(f'{Fore.GREEN}"A" Key Pressed')
    elif event in ("movement_key_3", "s"): #Key Event für S
        print(f'{Fore.GREEN}"S" Key Pressed')
    elif event in ("movement_key_2", "d"): #Key Event für D
        print(f'{Fore.GREEN}"D" Key Pressed')
    elif event in ("movement_key_2", "space"): #Key Event für SPACE
        print(f'{Fore.GREEN}"SPACE" Key Pressed')
    elif event == "Start": #Event für den Start button
        print(f'{Fore.YELLOW}Starting drone / DEVICE ID:  ...')

    elif event == "Clear terminal logs":
        os.system("clear || cls")
    elif event == "Exit": #Event für den Exit button
        print(f'{Fore.RED}Exiting GUI...')
        break
# closign gui
window.close()
