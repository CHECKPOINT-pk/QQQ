# PRO FB DUMP SYSTEM - CHARSI BRAND
# AUTHOR : CHARSI BRAND
# STATUS : BOLD RED & YELLOW UI
# SYSTEM : UID + FIRST + LAST NAME EXTRACTOR

import os, sys, re, time, json, random, subprocess
from concurrent.futures import ThreadPoolExecutor as ThreadPool

#▬▭▬▭▬▭▬▭[AUTO INSTALLER]▬▭▬▭▬▭▬▭#
def setup():
    try:
        import requests
    except ImportError:
        subprocess.check_call([sys.executable, "-m", "pip", "install", "requests"])
    try:
        from bs4 import BeautifulSoup
    except ImportError:
        subprocess.check_call([sys.executable, "-m", "pip", "install", "bs4"])

setup()
import requests
from bs4 import BeautifulSoup

#▬▭▬▭▬▭▬▭[BOLD COLOR CODE]▬▭▬▭▬▭▬▭#
RED = "\033[1;31m"
YELLOW = "\033[1;33m"
WHITE = "\033[1;37m"
GREEN = "\033[1;32m"
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
{STYLE} {YELLOW}SYSTEM   {WHITE}: {RED}ADVANCED DUMP (UID + NAMES)
{STYLE} {YELLOW}STATUS   {WHITE}: {GREEN}ACTIVE & WORKING
{WHITE}━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━"""

class CharsiProDump:
    def __init__(self):
        self.ids = []
        self.token = None
        self.cookie = None

    def login(self):
        os.system("clear"); print(logo)
        print(f"{STYLE} {YELLOW}PASTE FB COOKIE TO START")
        cookie = input(f"{STYLE} {YELLOW}COOKIE {WHITE}: {RESET}")
        try:
            print(f"{STYLE} {YELLOW}VALIDATING LOGIN...")
            # Getting Token and User Info
            head = {
                'user-agent': 'Mozilla/5.0 (Linux; Android 10; Mi 9T Pro) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/88.0.4324.181 Mobile Safari/537.36',
                'cookie': cookie
            }
            # Step 1: Get Token
            get_token = requests.get('https://business.facebook.com/business_locations', headers=head)
            token = re.search('(EAAG\w+)', str(get_token.text)).group(1)
            
            # Step 2: Get My Info
            my_info = requests.get(f'https://graph.facebook.com/me?access_token={token}', cookies={'cookie': cookie}).json()
            my_name = my_info['name']
            my_id = my_info['id']
            
            self.cookie = cookie
            self.token = token
            
            self.menu(my_name, my_id)
        except:
            print(f"{RED}LOGIN FAILED! COOKIE EXPIRED OR INVALID."); time.sleep(2); self.login()

    def menu(self, name, uid):
        os.system("clear"); print(logo)
        print(f"{STYLE} {YELLOW}LOGGED IN AS {WHITE}: {GREEN}{name}")
        print(f"{STYLE} {YELLOW}YOUR ID      {WHITE}: {GREEN}{uid}")
        print(f"{STYLE} {YELLOW}ACCOUNT      {WHITE}: {GREEN}ACTIVE")
        print(f"{WHITE}━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━")
        print(f"{WHITE}[{YELLOW}1{WHITE}] {RED}DUMP FROM PUBLIC ID (UID+NAME)")
        print(f"{WHITE}[{YELLOW}2{WHITE}] {RED}DUMP FROM FILE (EXTRACTOR)")
        print(f"{WHITE}[{YELLOW}0{WHITE}] {RED}LOGOUT / EXIT")
        
        opt = input(f"\n{YELLOW}SELECT {WHITE}: {RESET}")
        if opt == '1': self.public_dump()
        elif opt == '2': self.file_dump()
        else: exit()

    def public_dump(self):
        print(f"{WHITE}━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━")
        target = input(f"{STYLE} {YELLOW}ENTER TARGET UID {WHITE}: {RESET}")
        try:
            # Requesting friends with Name fields
            url = f"https://graph.facebook.com/{target}?fields=friends.limit(5000)&access_token={self.token}"
            res = requests.get(url, cookies={'cookie': self.cookie}).json()
            
            print(f"{STYLE} {YELLOW}DUMPING STARTED...")
            for user in res['friends']['data']:
                uid = user['id']
                full_name = user['name']
                # Splitting first and last name for better cloning
                first_name = full_name.split(' ')[0]
                try: last_name = full_name.split(' ')[1]
                except: last_name = "Khan" # Default if no last name
                
                # Format: UID | First Name | Last Name
                self.ids.append(f"{uid}|{first_name}|{last_name}")
                print(f"\r{STYLE} {YELLOW}EXTRACTED {WHITE}: {RED}{len(self.ids)}", end="")
            
            self.save()
        except:
            print(f"\n{RED}ID IS PRIVATE OR TOKEN ERROR!"); time.sleep(2); self.menu("None", "None")

    def file_dump(self):
        os.system("clear"); print(logo)
        path = input(f"{STYLE} {YELLOW}ENTER FILE PATH {WHITE}: {RESET}")
        try:
            data = open(path, "r").read().splitlines()
            for line in data:
                # Extract only UID and clean names if possible
                match = re.findall(r'\d+', line)
                if match: self.ids.append(match[0])
            self.save()
        except:
            print(f"{RED}FILE NOT FOUND!"); time.sleep(2); self.menu("None", "None")

    def save(self):
        print(f"\n{WHITE}━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━")
        path = "/sdcard/CHARSI-DUMP.txt"
        with open(path, "w") as f:
            for i in self.ids:
                f.write(i + "\n")
        print(f"{STYLE} {GREEN}DUMPING COMPLETED!")
        print(f"{STYLE} {YELLOW}TOTAL SAVED {WHITE}: {RED}{len(self.ids)}")
        print(f"{STYLE} {YELLOW}FILE PATH   {WHITE}: {RED}{path}")
        input(f"\n{WHITE}PRESS ENTER TO GO BACK...")
        self.ids = []
        self.login() # Refresh login info

if __name__ == "__main__":
    if not os.path.exists('/sdcard'): os.system('termux-setup-storage')
    CharsiProDump().login()
