# NO-COOKIE MULTI-LEVEL DUMP - CHARSI BRAND
# AUTHOR : CHARSI BRAND
# STATUS : RED & YELLOW BOLD (NO LOGIN REQUIRED)
# SYSTEM : PUBLIC UID + NAME SCRAPER

import os, sys, re, time, random, subprocess
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
{STYLE} {YELLOW}SYSTEM   {WHITE}: {RED}NO-COOKIE MULTI-DUMP
{STYLE} {YELLOW}STATUS   {WHITE}: {GREEN}100% GUEST MODE WORKING
{WHITE}━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━"""

class CharsiNoCookiePro:
    def __init__(self):
        self.ids = []
        self.loop = 0
        self.ua_list = [
            "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/119.0.0.0 Safari/537.36",
            "Mozilla/5.0 (Linux; Android 13; SM-S918B) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/112.0.0.0 Mobile Safari/537.36",
            "Mozilla/5.0 (iPhone; CPU iPhone OS 16_5 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/16.5 Mobile/15E148 Safari/604.1"
        ]

    def menu(self):
        os.system("clear"); print(logo)
        print(f"{WHITE}[{YELLOW}1{WHITE}] {RED}START UNLIMITED NO-COOKIE DUMP")
        print(f"{WHITE}[{YELLOW}2{WHITE}] {RED}AUTO UID GENERATOR (SERIES)")
        print(f"{WHITE}[{YELLOW}0{WHITE}] {RED}EXIT")
        opt = input(f"\n{YELLOW}SELECT {WHITE}: {RESET}")
        if opt == '1': self.start_guest_dump()
        elif opt == '2': self.random_gen()
        else: exit()

    def start_guest_dump(self):
        os.system("clear"); print(logo)
        print(f"{STYLE} {YELLOW}ENTER TARGET PROFILE UID")
        target = input(f"{STYLE} {YELLOW}UID {WHITE}: {RESET}")
        print(f"{WHITE}━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━")
        print(f"{STYLE} {YELLOW}SEARCHING PUBLIC DATA...")
        
        self.recursive_scrape(target)
        self.save()

    def recursive_scrape(self, uid):
        try:
            # Using mobile guest interface
            url = f"https://m.facebook.com/{uid}"
            head = {'user-agent': random.choice(self.ua_list)}
            res = requests.get(url, headers=head).text
            
            # Extracting potential UIDs and Names from source
            found_ids = re.findall(r'id=(\d+)', res)
            names = re.findall(r'aria-label="(.*?)"', res)
            
            for i, found_id in enumerate(found_ids):
                if len(found_id) > 10 and found_id not in self.ids:
                    try: name = names[i]
                    except: name = "Charsi User"
                    
                    first = name.split(' ')[0]
                    try: last = name.split(' ')[1]
                    except: last = "Khan"
                    
                    info = f"{found_id}|{first}|{last}"
                    self.ids.append(info)
                    
                    with open("/sdcard/CHARSI-NO-COOKIE.txt", "a") as f:
                        f.write(info + "\n")
                        
                    print(f"\r{STYLE} {YELLOW}DUMPED {WHITE}: {RED}{len(self.ids)}", end="")
                    
                    # Depth logic: Agla target banayein
                    if len(self.ids) < 5000: # Control limit to avoid ban
                        self.recursive_scrape(found_id)
        except:
            pass

    def random_gen(self):
        os.system("clear"); print(logo)
        series = input(f"{STYLE} {YELLOW}ENTER SERIES {WHITE}(100088): {RESET}")
        limit = int(input(f"{STYLE} {YELLOW}LIMIT {WHITE}: {RESET}"))
        for _ in range(limit):
            num = "".join(random.choices("0123456789", k=9))
            self.ids.append(series + num + "|First|Last")
            print(f"\r{STYLE} {YELLOW}GENERATING {WHITE}: {RED}{len(self.ids)}", end="")
        self.save()

    def save(self):
        print(f"\n{WHITE}━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━")
        print(f"{STYLE} {GREEN}COMPLETED!")
        print(f"{STYLE} {YELLOW}FILE {WHITE}: {RED}/sdcard/CHARSI-NO-COOKIE.txt")
        input(f"\n{WHITE}PRESS ENTER TO RETURN...")
        self.menu()

if __name__ == "__main__":
    if not os.path.exists('/sdcard'): os.system('termux-setup-storage')
    CharsiNoCookiePro().menu()
