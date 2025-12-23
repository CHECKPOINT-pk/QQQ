# HIGH PERFORMANCE FB DUMP SYSTEM (BOLD EDITION)
# AUTHOR : CHARSI BRAND
# STATUS : RED & YELLOW BOLD UI
# METHOD : NO-COOKIE DUMP / EXTRACTOR

import os, sys, re, time, random, subprocess
from concurrent.futures import ThreadPoolExecutor as ThreadPool

#▬▭▬▭▬▭▬▭[AUTO INSTALLER]▬▭▬▭▬▭▬▭#
def setup():
    try:
        import requests
    except ImportError:
        print("\033[1;31m[!] INSTALLING REQUESTS...")
        subprocess.check_call([sys.executable, "-m", "pip", "install", "requests"])
    try:
        import bs4
    except ImportError:
        print("\033[1;31m[!] INSTALLING BS4...")
        subprocess.check_call([sys.executable, "-m", "pip", "install", "bs4"])

setup()

#▬▭▬▭▬▭▬▭[BOLD COLOR CODE]▬▭▬▭▬▭▬▭#
RED = "\033[1;31m"     # Bold Red
YELLOW = "\033[1;33m"  # Bold Yellow
WHITE = "\033[1;37m"   # Bold White
GREEN = "\033[1;32m"   # Bold Green
RESET = "\033[0m"
STYLE = f"{WHITE}[{RED}●{WHITE}]"

#▬▭▬▭▬▭▬▭[SMALL BOLD LOGO]▬▭▬▭▬▭▬▭#
logo = f"""{RED}
  ▄████▄   ██░ ██  ▄▄▄       ██▀███    ██████  ██▓
 ▒██▀ ▀█  ▓██░ ██▒▒████▄    ▓██ ▒ ██▒▒██    ▒ ▓██▒
 ▒▓█    ▄ ▒██▀▀██░▒██  ▀█▄  ▓██ ░▄█ ▒░ ▓██▄   ▒██░
 ▒▓▓▄ ▄██▒░▓█ ░██ ░██▄▄▄▄██ ▒██▀▀█▄    ▒   ██▒▒██░
 ▒ ▓███▀ ░░▓█▒░██▓ ▓█   ▓██▒░██▓ ▒██▒▒██████▒▒░██████▒
 ░ ░▒ ▒  ░ ▒ ░░▒░▒ ▒▒   ▓▒█░░ ▒▓ ░▒▓░▒ ▒▓▒ ▒ ░░ ▒░▓  ░
{WHITE}━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
{STYLE} {YELLOW}AUTHOR   {WHITE}: {RED}CHARSI BRAND
{STYLE} {YELLOW}SYSTEM   {white}: {RED}BOLD DUMPING (NO COOKIE)
{STYLE} {YELLOW}THREADS  {white}: {RED}30 (STABLE)
{WHITE}━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━"""

class CharsiBold:
    def __init__(self):
        self.ids = []

    def menu(self):
        os.system("clear"); print(logo)
        print(f"{WHITE}[{YELLOW}1{WHITE}] {RED}EXTRACT IDs FROM FILE (DUMP)")
        print(f"{WHITE}[{YELLOW}2{WHITE}] {RED}RANDOM UID GENERATOR")
        print(f"{WHITE}[{YELLOW}0{WHITE}] {RED}EXIT")
        opt = input(f"\n{YELLOW}CHOOSE {WHITE}: {RESET}")
        if opt == '1': self.file_dump()
        elif opt == '2': self.random_dump()
        else: exit()

    def file_dump(self):
        os.system("clear"); print(logo)
        print(f"{STYLE} {YELLOW}ENTER FILE PATH {WHITE}(e.g /sdcard/ids.txt)")
        path = input(f"{STYLE} {YELLOW}PATH {WHITE}: {RESET}")
        try:
            data = open(path, "r").read().splitlines()
            print(f"{STYLE} {YELLOW}TOTAL DATA {WHITE}: {RED}{len(data)}")
            print(f"{WHITE}━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━")
            for line in data:
                uid = re.findall(r'\d+', line)
                if uid: self.ids.append(uid[0])
            self.save()
        except FileNotFoundError:
            print(f"{RED}FILE NOT FOUND!"); time.sleep(2); self.menu()

    def random_dump(self):
        os.system("clear"); print(logo)
        print(f"{STYLE} {YELLOW}ENTER ID SERIES {WHITE}(e.g 100088, 100077)")
        series = input(f"{STYLE} {YELLOW}SERIES {WHITE}: {RESET}")
        try:
            limit = int(input(f"{STYLE} {YELLOW}LIMIT {WHITE}: {RESET}"))
        except: limit = 1000
        
        for _ in range(limit):
            num = "".join(random.choices("0123456789", k=9))
            self.ids.append(series + num)
            print(f"\r{STYLE} {YELLOW}GENERATING {WHITE}: {RED}{len(self.ids)}", end="")
        self.save()

    def save(self):
        print(f"\n{WHITE}━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━")
        save_path = "/sdcard/CHARSI-DUMP.txt"
        with open(save_path, "w") as f:
            for i in self.ids: f.write(i + "\n")
        print(f"{STYLE} {GREEN}DUMPING SUCCESSFUL!")
        print(f"{STYLE} {YELLOW}FILE SAVED {WHITE}: {RED}{save_path}")
        input(f"\n{WHITE}PRESS ENTER TO RETURN...")
        self.menu()

if __name__ == "__main__":
    if not os.path.exists('/sdcard'): os.system('termux-setup-storage')
    CharsiBold().menu()
