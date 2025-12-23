# HIGH PERFORMANCE AUTO CREATE FB - 2025 BEST VERSION
# AUTHOR : CHARSI BRAND
# GITHUB  : CHARSI-BRAND-708
# STATUS : HIGHEST OPTIMIZED - NO APPROVAL

import os, sys, re, time, random, uuid, string, subprocess
from concurrent.futures import ThreadPoolExecutor as ThreadPool

#▬▭▬▭▬▭▬▭[AUTO INSTALLER]▬▭▬▭▬▭▬▭#
def install_modules():
    modules = ['requests', 'bs4', 'faker', 'fake-useragent']
    for module in modules:
        try:
            __import__(module)
        except ImportError:
            print(f"Installing {module}...")
            subprocess.check_call([sys.executable, "-m", "pip", "install", module])

install_modules()

import requests
from bs4 import BeautifulSoup
from faker import Faker
from fake_useragent import UserAgent

#▬▭▬▭▬▭▬▭[COLOR CODE]▬▭▬▭▬▭▬▭#
green = "\x1b[38;5;49m"; white = "\033[1;37m"; red = "\x1b[38;5;160m"; reset = "\033[0m"
style = f"{white}[{green}●{white}]"

#▬▭▬▭▬▭▬▭[BANNER]▬▭▬▭▬▭▬▭#
logo = f"""{green}
  ▄████▄   ██░ ██  ▄▄▄       ██▀███    ██████  ██▓    ██▄███   ▄▄▄       ███▄    █ ▓█████▄ 
 ▒██▀ ▀█  ▓██░ ██▒▒████▄    ▓██ ▒ ██▒▒██    ▒ ▓██▒   ▓██ ▒ ██▒▒████▄     ██ ▀█   █ ▒██▀ ██▌
 ▒▓█    ▄ ▒██▀▀██░▒██  ▀█▄  ▓██ ░▄█ ▒░ ▓██▄   ▒██░   ▓██ ░▄█ ▒▒██  ▀█▄   ▓██  ▀█ ██▒░██   █▌
 ▒▓▓▄ ▄██▒░▓█ ░██ ░██▄▄▄▄██ ▒██▀▀█▄    ▒   ██▒▒██░   ▒██▀▀█▄  ░██▄▄▄▄██  ▓██▒  ▐▌██▒░▓█▄   ▌
 ▒ ▓███▀ ░░▓█▒░██▓ ▓█   ▓██▒░██▓ ▒██▒▒██████▒▒░██████▒░██▓ ▒██▒ ▓█   ▓██▒ ▒██░   ▓██░░▒████▓ 
 ░ ░▒ ▒  ░ ▒ ░░▒░▒ ▒▒   ▓▒█░░ ▒▓ ░▒▓░▒ ▒▓▒ ▒ ░░ ▒░▓  ░░ ▒▓ ░▒▓░ ▒▒   ▓▒█░ ░ ▒░   ▒ ▒  ░▒ ▒  ░ 
  ░  ▒     ▒ ░▒░ ░  ▒   ▒▒ ░  ░▒ ░ ▒░░ ░▒  ░ ░░ ░ ▒  ░  ░▒ ░ ▒░  ▒   ▒▒ ░ ░ ░░   ░ ▒░ ░ ░  ▒  
░          ░  ░░ ░  ░   ▒     ░░   ░ ░  ░  ░    ░ ░     ░░   ░   ░   ▒       ░   ░ ░  ░ ░  ░  
░ ░        ░  ░  ░      ░  ░   ░           ░      ░  ░   ░           ░  ░         ░    ░     
░                                                                                     ░      
{white}━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
{style} AUTHOR  : CHARSI BRAND
{style} UPDATE  : HIGHEST PERFORMANCE (2025)
{style} FILES   : /sdcard/CHARSI-OK.txt
{white}━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━"""

class CharsiBrand:
    def __init__(self):
        self.oks = []
        self.cps = []
        self.loop = 0
        self.ua = UserAgent()
        self.fk = Faker()

    def menu(self):
        os.system('clear'); print(logo)
        print(f"{white}[1] Start Auto Creation (Charsi Speed)")
        print(f"[0] Exit")
        opt = input(f"\n{green}Select Option: {reset}")
        if opt == '1': self.start()
        else: exit()

    def start(self):
        os.system('clear'); print(logo)
        try:
            limit = int(input(f"{green}Account Limit: {white}"))
        except: limit = 10
        print(f"{green}Speed: Maximum Threads Active...")
        print(f"{white}━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━")
        
        with ThreadPool(max_workers=35) as pool:
            for _ in range(limit):
                pool.submit(self.create)
        
        print(f"\n{white}━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━")
        print(f"{green}SUCCESS: {len(self.oks)} | {red}CP: {len(self.cps)}")
        print(f"{white}Results saved in /sdcard/CHARSI-OK.txt")

    def create(self):
        first = self.fk.first_name()
        last = self.fk.last_name()
        password = first + str(random.randint(111, 999))
        birthday = f"{random.randint(1992, 2005)}-{random.randint(1, 12)}-{random.randint(1, 28)}"
        email = f"{first.lower()}{last.lower()}{random.randint(10,999)}@gmail.com"
        
        try:
            ses = requests.Session()
            headers = {
                'authority': 'm.facebook.com',
                'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8',
                'accept-language': 'en-GB,en-US;q=0.9,en;q=0.8',
                'referer': 'https://m.facebook.com/reg/',
                'user-agent': self.ua.random,
            }
            
            # Form extraction
            reg_page = ses.get('https://m.facebook.com/reg/', headers=headers).text
            soup = BeautifulSoup(reg_page, 'html.parser')
            form_data = {i.get('name'): i.get('value') for i in soup.find_all('input') if i.get('name')}
            
            payload = {
                **form_data,
                'firstname': first,
                'lastname': last,
                'reg_email__': email,
                'reg_passwd__': password,
                'birthday_day': birthday.split('-')[2],
                'birthday_month': birthday.split('-')[1],
                'birthday_year': birthday.split('-')[0],
                'sex': '2'
            }
            
            response = ses.post('https://m.facebook.com/reg/submit/', data=payload, headers=headers)
            
            if 'c_user' in ses.cookies.get_dict():
                uid = ses.cookies.get_dict()['c_user']
                print(f"\n{green}[CHARSI-OK] {uid} | {password}      ")
                self.oks.append(uid)
                with open("/sdcard/CHARSI-OK.txt", "a") as f:
                    f.write(f"{uid}|{password}\n")
            elif 'checkpoint' in response.url:
                self.cps.append(email)
                with open("/sdcard/CHARSI-CP.txt", "a") as f:
                    f.write(f"{email}|{password}\n")
            
            self.loop += 1
            print(f"\r{white}[RUNNING] {self.loop} | OK:{len(self.oks)} CP:{len(self.cps)}", end="")
            
        except Exception:
            pass

if __name__ == "__main__":
    if not os.path.exists('/sdcard'): os.system('termux-setup-storage')
    CharsiBrand().menu()
