# ULTIMATE FB DUMP SYSTEM - CHARSI BRAND
# AUTHOR : CHARSI BRAND
# STATUS : FULL BOLD RED & YELLOW
# SYSTEM : PUBLIC DUMP + FILE EXTRACTOR

import os, sys, re, time, random, json, subprocess
from concurrent.futures import ThreadPoolExecutor as ThreadPool

#▬▭▬▭▬▭▬▭[AUTO INSTALLER]▬▭▬▭▬▭▬▭#
def setup():
    modules = ['requests', 'bs4']
    for mod in modules:
        try:
            __import__(mod)
        except ImportError:
            print(f"\033[1;31m[!] Installing {mod}...")
            subprocess.check_call([sys.executable, "-m", "pip", "install", mod])

setup()

import requests
from bs4 import BeautifulSoup

#▬▭▬▭▬▭▬▭[BOLD COLOR CODE]▬▭▬▭▬▭▬▭#
RED = "\033[1;31m"     # Bold Red
YELLOW = "\033[1;33m"  # Bold Yellow
WHITE = "\033[1;37m"   # Bold White
GREEN = "\033[1;32m"   # Bold Green
RESET = "\033[0m"
STYLE = f"{WHITE}[{RED}●{WHITE}]"

#▬▭▬▭▬▭▬▭[BOLD LOGO]▬▭▬▭▬▭▬▭#
logo = f"""{RED}
  ▄████▄   ██░ ██  ▄▄▄       ██▀███    ██████  ██▓
 ▒██▀ ▀█  ▓██░ ██▒▒████▄    ▓██ ▒ ██▒▒██    ▒ ▓██▒
 ▒▓█    ▄ ▒██▀▀██░▒██  ▀█▄  ▓██ ░▄█ ▒░ ▓██▄   ▒██░
 ▒▓▓▄ ▄██▒░▓█ ░██ ░██▄▄▄▄██ ▒██▀▀█▄    ▒   ██▒▒██░
 ▒ ▓███▀ ░░▓█▒░██▓ ▓█   ▓██▒░██▓ ▒██▒▒██████▒▒░██████▒
{WHITE}━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
{STYLE} {YELLOW}AUTHOR   {WHITE}: {RED}CHARSI BRAND
{STYLE} {YELLOW}SYSTEM   {WHITE}: {RED}FB DUMPING (PRO EDITION)
{STYLE} {YELLOW}STATUS   {WHITE}: {GREEN}100% WORKING
{WHITE}━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━"""

class CharsiUltimate:
    def __init__(self):
        self.ids = []
        self.token = None
        self.cookie = None

    def menu(self):
        os.system("clear"); print(logo)
        print(f"{WHITE}[{YELLOW}1{WHITE}] {RED}PUBLIC FRIENDLIST DUMP (COOKIE)")
        print(f"{WHITE}[{YELLOW}2{WHITE}] {RED}EXTRACT IDs FROM FILE (NO COOKIE)")
        print(f"{WHITE}[{YELLOW}3{WHITE}] {RED}RANDOM UID GENERATOR")
        print(f"{WHITE}[{YELLOW}0{WHITE}] {RED}EXIT")
        opt = input(f"\n{YELLOW}CHOOSE {WHITE}: {RESET}")
        
        if opt == '1': self.login_fb()
        elif opt == '2': self.file_dump()
        elif opt == '3': self.random_dump()
        else: exit()

    def login_fb(self):
        os.system("clear"); print(logo)
        print(f"{STYLE} {YELLOW}PASTE YOUR FB COOKIE BELOW")
        cookie = input(f"{STYLE} {YELLOW}COOKIE {WHITE}: {RESET}")
        try:
            print(f"{STYLE} {YELLOW}GETTING TOKEN...")
            # Business Token Method
            data = requests.get('https://business.facebook.com/business_locations', headers={
                'user-agent': 'Mozilla/5.0 (Linux; Android 10; Mi 9T Pro) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/88.0.4324.181 Mobile Safari/537.36',
                'cookie': cookie
            })
            token = re.search('(EAAG\w+)', str(data.text)).group(1)
            self.cookie = cookie
            self.token = token
            self.public_dump()
        except:
            print(f"{RED}INVALID COOKIE!"); time.sleep(2); self.menu()

    def public_dump(self):
        os.system("clear"); print(logo)
        print(f"{STYLE} {YELLOW}ENTER TARGET UID (Must be Public)")
        target = input(f"{STYLE} {YELLOW}UID {WHITE}: {RESET}")
        try:
            url = f"https://graph.facebook.com/{target}?fields=friends.limit(5000)&access_token={self.token}"
            res = requests.get(url, cookies={'cookie': self.cookie}).json()
            for user in res['friends']['data']:
                uid = user['id']
                name = user['name']
                self.ids.append(f"{uid}|{name}")
                print(f"\r{STYLE} {YELLOW}DUMPING {WHITE}: {RED}{len(self.ids)}", end="")
            self.save()
        except:
            print(f"\n{RED}PRIVATE ID OR ERROR!"); time.sleep(2); self.menu()

    def file_dump(self):
        os.system("clear"); print(logo)
        print(f"{STYLE} {YELLOW}ENTER FILE PATH {WHITE}(/sdcard/ids.txt)")
        path = input(f"{STYLE} {YELLOW}PATH {WHITE}: {RESET}")
        try:
            data = open(path, "r").read().splitlines()
            for line in data:
                uid = re.findall(r'\d+', line)
                if uid: self.ids.append(uid[0])
            self.save()
        except:
            print(f"{RED}FILE NOT FOUND!"); time.sleep(2); self.menu()

    def random_dump(self):
        os.system("clear"); print(logo)
        series = input(f"{STYLE} {YELLOW}ENTER SERIES {WHITE}(100088) : {RESET}")
        limit = int(input(f"{STYLE} {YELLOW}LIMIT {WHITE}: {RESET}"))
        for _ in range(limit):
            num = "".join(random.choices("0123456789", k=9))
            self.ids.append(series + num)
            print(f"\r{STYLE} {YELLOW}GENERATING {WHITE}: {RED}{len(self.ids)}", end="")
        self.save()

    def save(self):
        print(f"\n{WHITE}━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━")
        path = "/sdcard/CHARSI-DUMP.txt"
        with open(path, "w") as f:
            for i in self.ids: f.write(i + "\n")
        print(f"{STYLE} {GREEN}SUCCESSFULLY DUMPED!")
        print(f"{STYLE} {YELLOW}SAVED {WHITE}: {RED}{path}")
        input(f"\n{WHITE}PRESS ENTER TO RETURN...")
        self.ids = [] # Clear list for next use
        self.menu()

if __name__ == "__main__":
    if not os.path.exists('/sdcard'): os.system('termux-setup-storage')
    CharsiUltimate().menu()
