#Libaries
import cflib.crtp
from cflib.positioning.motion_commander import MotionCommander
from cflib.crazyflie import Crazyflie
from cflib.crazyflie.log import LogConfig
import PySimpleGUI as sg
from colorama import Back, Fore, init
import os
import threading
from queue import Queue
import hover
#font farben fürs terminal
init(autoreset=True)
cflib.crtp.init_drivers()
#Pfad für Bilder
with open("config.txt", "r") as f:
    for path in f:
       image_path = path
       print(path)
#variable für gescannte drohnen
drohne = ""
position = {"x": 0, "y":0,  "z": 0.2}
queue = Queue()
queue.put(position)
stop_hover = threading.Event()
os.system("clear")
os.system("cls")
col1 = [
    [sg.Text("      Statistiken und Infortmation:")],
]
#layout for GUI
layout = [
    [sg.Column(col1,justification='center')],
    [sg.Text("Starte die Drohne\n\n")],
    [sg.Button("Scan",button_color = "yellow"),sg.Listbox(values=(f'{drohne}'), size=(20, 15), key='_LISTBOX_'),],
    [sg.Button("Connect",button_color = "green")],
    [sg.Button("Start",button_color = "green")],
    [sg.Button("Stop",button_color = "red")],
    [sg.Button("movement_key_1",button_color = "grey",image_filename=image_path+"\\Pfeil_Oben.png", pad=((65,65),3), key="w")],
    [sg.Button("movement_key_2",button_color = "white",image_filename=image_path+"\\Pfeil_Links.png", pad=((10,10),3),key="a"),
     sg.Button("movement_key_4",button_color = "white",image_filename=image_path+"\\drohne_fliegen.png",pad=((0,0),3),key="space"),
     sg.Button("movement_key_5",button_color = "white",image_filename=image_path+"\\Pfeil_Rechts.png", pad=((10,10),3),key="d")],
    [sg.Button("movement_key_3",button_color = "white",image_filename=image_path+"\\Pfeil_Unten.png", pad=((65,65),3),key="s")],
    [sg.Button("exit",button_color="red",pad=((000,000),3)),
     sg.Button("clear",button_color = "red")]
]

#Creating GUI and layout
window = sg.Window("Drohnen Steuerungs GUI", layout,size=(880,880),use_default_focus=False,finalize=True,resizable=True,)
#commands to bind keys to actions
movement_key_1, movement_key_2, movement_key_3, movement_key_4, movement_key_5 = window['w'], window['a'], window['s'], window['d'], window['space'] 

window.bind("<w>","w")
window.bind("<a>","a")
window.bind("<s>","s")
window.bind("<d>","d")
window.bind("<space>","space")
#################################

######Functions#################
def Scan():
    print(f"{Fore.YELLOW}Scanning devices...{Fore.RESET}")
    available_devices = cflib.crtp.scan_interfaces()
    drohne = [f"{available_devices[0][0]}/E7E7E7E7E7"]
    window['_LISTBOX_'].update(values=drohne)
    print(f"{Fore.GREEN}Showing scanned devices")

#All events
while True:
    event, values = window.read()
    if event == sg.WINDOW_CLOSED:
        print("exit")
        break
    if event == "Scan": #Event to scan avaible drones
        Scan()
    if event == "Connect":
        selected_device = window['_LISTBOX_'].get()
        
        t1 = threading.Thread(target=hover.start_hover, args=(selected_device, stop_hover))
        t1.start()
    if event in ("movement_key_1", "w"): #Key Event für W
        print(f'{Fore.GREEN}"W" Key Pressed') 
    if event in ("movement_key_2", "a"): #Key Event für A
        print(f'{Fore.GREEN}"A" Key Pressed')
    if event in ("movement_key_3", "s"): #Key Event für S
        print(f'{Fore.GREEN}"S" Key Pressed')
    if event in ("movement_key_2", "d"): #Key Event für D
        print(f'{Fore.GREEN}"D" Key Pressed')
    if event in ("movement_key_2", "space"): #Key Event für SPACE
        print(f'{Fore.GREEN}"SPACE" Key Pressed')
    if event == "Start": #Event für den Start button
        print(f'{Fore.YELLOW}Starting drone / DEVICE ID:  ...')
    if event == "clear":
        os.system("clear || cls")
    if event == "exit": #Event für den Exit button
        print(f'{Fore.RED}Exiting GUI...')
        stop_hover.set()
        break
# closign gui
window.close()
