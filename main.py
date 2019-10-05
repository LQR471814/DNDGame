import curses
import time

CampaignSelectObj = open("CampaignSelection.txt", "r")
CampaignSelect = CampaignSelectObj.read()
SettingsMenuObj = open("SettingsMenu.txt", "r")
SettingsMenu = SettingsMenuObj.read()
MenuObj = open("Menu.txt", "r")
Menu = MenuObj.read()
title = [
" _____                                                           _       _                                   _ ",
"|  __ \\                                                         | |     | |                                 | |",
"| |  | |_   _ _ __   __ _  ___  ___  _ __  ___    __ _ _ __   __| |   __| |_ __ __ _  __ _  ___  _ __  ___  | |",
"| |  | | | | | '_ \\ / _` |/ _ \\/ _ \\| '_ \\/ __|  / _` | '_ \\ / _` |  / _` | '__/ _` |/ _` |/ _ \\| '_ \\/ __/ | |",
"| |__| | |_| | | | | (_| |  __/ (_) | | | \\__ \\ | (_| | | | | (_| | | (_| | | | (_| | (_| | (_) | | | \\__ \\ |_|",
"|_____/ \\__,_|_| |_|\\__, |\\___|\\___/|_| |_|___/  \\__,_|_| |_|\\__,_|  \\__,_|_|  \\__,_|\\__, |\\___/|_| |_|___/ (_)",
"                     __/ |                                                             _/ |                    ",
"                    |____/                                                            |___/                    "
]

StartOptions = """
 =====================<-([-+-])->=====================
Dungeons and Dragons                         v0.1_Alpha

Campaign modes (I need a writer)                    [C]
Multiplayer                                         [M]
Achievements (WIP)                                  [A]



Settings                                            [S]
Quit                                                [Q]
 =====================<-([-+-])->=====================
"""

def main(stdscr):
    global title
    global Menu
    global SettingsMenu
    global StartOptions
    global CampaignSelect
    
    OnCampSelect = False
    OnSettings = False
    StartMenu = True
    EscMenu = False
    stdscr.nodelay(True)
    stdscr.clear()
    stdscr.keypad(True)
    QuitKey = 27
    CurrentText = ""
    count = 0
    direction = 1
    
    for line in title:
        stdscr.addstr(line)
        stdscr.addstr("\n")
    stdscr.addstr(StartOptions)

    while True:
        try:
            keyInp = stdscr.getkey()
            print(str(ord(keyInp)), keyInp)
        except:
            continue
        if OnSettings == True: #? Exit from settings
            if ord(keyInp) == 27:
                stdscr.clear()
                for line in title:
                    stdscr.addstr(line)
                    stdscr.addstr("\n")
                stdscr.addstr(StartOptions)
                OnSettings = False
                continue

        if EscMenu == True: #? ESC Menu toggled
            if ord(keyInp) == 27: #? Detect ESC toggled
                stdscr.clear()
                for line in title:
                    stdscr.addstr(line)
                    stdscr.addstr("\n")
                stdscr.addstr(StartOptions)
                EscMenu = False
                continue
            if keyInp == "r": #? Detect R pressed (Return to start)
                stdscr.clear()
                for line in title:
                    stdscr.addstr(line)
                    stdscr.addstr("\n")
                stdscr.addstr(StartOptions)
                EscMenu = False
                continue
            if keyInp == "s": #? Detect S pressed (Go to settings)
                OnSettings = True
                stdscr.clear()
                stdscr.addstr(SettingsMenu)
                EscMenu = False
            if keyInp == "q": #? Detect Q pressed (Quit)
                return
                EscMenu = False
            continue
        
        if StartMenu == True: #? If on Start screen
            if keyInp == "c":
                stdscr.clear()
                stdscr.addstr(CampaignSelect)
                OnCampSelect = True
            if keyInp == "q":
                return
            if keyInp == "s":
                stdscr.clear()
                stdscr.addstr(SettingsMenu)
                OnSettings = True
                
        if OnCampSelect == True:
            if ord(keyInp) == 27:
                stdscr.clear()
                for line in title:
                    stdscr.addstr(line)
                    stdscr.addstr("\n")
                stdscr.addstr(StartOptions)
                OnCampSelect = False
                continue
                
        if OnSettings == False or OnCampSelect == False:
            if ord(keyInp) == 27: #? Detect ESC toggled
                stdscr.clear()
                stdscr.addstr(Menu)
                EscMenu = True

curses.wrapper(main)