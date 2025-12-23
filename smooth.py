# HIGH PERFORMANCE AUTO CREATE FB + AUTO VERIFY
# AUTHOR : CHARSI BRAND
# GITHUB : CHARSI-BRAND-708
# VERSION: BEST WORKING 2025

import os, sys, re, time, random, uuid, subprocess
from concurrent.futures import ThreadPoolExecutor as ThreadPool

#▬▭▬▭▬▭▬▭[AUTO INSTALLER]▬▭▬▭▬▭▬▭#
def setup():
    modules = ['requests', 'bs4', 'faker', 'fake-useragent']
    for mod in modules:
        try:
            __import__(mod)
        except ImportError:
            print(f"\033[1;37mInstalling {mod}...")
            subprocess.check_call([sys.executable, "-m", "pip", "install", mod])

setup()

import requests
from bs4 import BeautifulSoup
from faker import Faker
from fake_useragent import UserAgent

#▬▭▬▭▬▭▬▭[COLOR & STYLE]▬▭▬▭▬▭▬▭#
green = "\x1b[38;5;49m"
white = "\033[1;37m"
red = "\x1b[38;5;160m"
yellow = "\033[1;33m"
reset = "\033[0m"
style = f"{white}[{green}●{white}]"

#▬▭▬▭▬▭▬▭[SMALL GREEN LOGO]▬▭▬▭▬▭▬▭#
logo = f"""{green}
  ___ _  _   _   ___  ___ ___ 
 / __| || | /_\ | _ \/ __|_ _|
| (__| __ |/ _ \|   /\__ \| | 
 \___|_||_/_/ \_\_|_\|___/___| {white}BRAND
{white}━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
{style} {green}AUTHOR   {white}: {yellow}CHARSI BRAND
{style} {green}THREADS  {white}: {yellow}30 (SPEED MODE)
{style} {green}STATUS   {white}: {green}100% WORKING
{white}━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━"""

class CharsiPro:
    def __init__(self):
        self.oks = []
        self.cps = []
        self.loop = 0
        self.fk = Faker()
        self.ua = UserAgent()

    def get_mail(self):
        try:
            user = "".join(random.choices(string.ascii_lowercase + string.digits, k=10))
            return f"{user}@1secmail.com"
        except:
            return f"charsi{random.randint(111,999)}@1secmail.com"

    def get_otp(self, email):
        login, domain = email.split('@')
        for _ in range(15):
            time.sleep(4)
            try:
                url = f"https://www.1secmail.com/api/v1/?action=getMessages&login={login}&domain={domain}"
                msgs = requests.get(url).json()
                for m in msgs:
                    if "Facebook" in str(m['subject']) or "FB-" in str(m['subject']):
                        msg_id = m['id']
                        read_url = f"https://www.1secmail.com/api/v1/?action=readMessage&login={login}&domain={domain}&id={msg_id}"
                        content = requests.get(read_url).json()
                        otp = re.search(r'\b\d{5}\b', content['body'])
                        if otp: return otp.group(0)
            except: pass
        return None

    def menu(self):
        os.system('clear'); print(logo)
        print(f"{white}[{green}1{white}] {green}START BEST AUTO CREATION")
        print(f"{white}[{red}0{white}] {red}EXIT PROGRAM")
        opt = input(f"\n{green}SELECT {white}: {reset}")
        if opt == '1': self.start()
        else: exit()

    def start(self):
        os.system('clear'); print(logo)
        try:
            limit = int(input(f"{green}ACCOUNT LIMIT {white}: {reset}"))
        except: limit = 5
        print(f"{white}━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━")
        
        with ThreadPool(max_workers=30) as pool:
            for _ in range(limit):
                pool.submit(self.create)
        
        print(f"\n{white}━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━")
        print(f"{green}SUCCESS: {len(self.oks)} | {red}CP: {len(self.cps)}")

    def create(self):
        fname = self.fk.first_name()
        lname = self.fk.last_name()
        pwd = fname + str(random.randint(111, 999))
        mail = self.get_mail()
        
        try:
            ses = requests.Session()
            head = {
                'authority': 'm.facebook.com',
                'user-agent': self.ua.random,
                'accept-language': 'en-GB,en-US;q=0.9,en;q=0.8',
            }
            
            # Form Fetch
            reg_html = ses.get('https://m.facebook.com/reg/', headers=head).text
            soup = BeautifulSoup(reg_html, 'html.parser')
            data = {i.get('name'): i.get('value') for i in soup.find_all('input') if i.get('name')}
            
            data.update({
                'firstname': fname, 'lastname': lname,
                'reg_email__': mail, 'reg_passwd__': pwd,
                'birthday_day': str(random.randint(1,28)),
                'birthday_month': str(random.randint(1,12)),
                'birthday_year': str(random.randint(1992,2005)),
                'sex': '2'
            })
            
            # Post Data
            res = ses.post('https://m.facebook.com/reg/submit/', data=data, headers=head)
            
            if "confirm-email" in res.url:
                print(f"\r{white}[{yellow}VERIFYING{white}] {mail}          ", end="")
                otp = self.get_otp(mail)
                if otp:
                    print(f"\n{green}[CHARSI-OK] {mail} | {pwd} | {otp}")
                    self.oks.append(mail)
                    open("/sdcard/CHARSI-OK.txt","a").write(f"{mail}|{pwd}|{otp}\n")
                else:
                    self.cps.append(mail)
            elif "c_user" in ses.cookies.get_dict():
                uid = ses.cookies.get_dict()['c_user']
                self.oks.append(uid)
                print(f"\n{green}[CHARSI-OK] {uid} | {pwd}")
                open("/sdcard/CHARSI-OK.txt","a").write(f"{uid}|{pwd}\n")
            else:
                self.cps.append(mail)
            
            self.loop += 1
            print(f"\r{white}[RUNNING] {self.loop} | {green}OK:{len(self.oks)} {red}CP:{len(self.cps)}", end="")
            
        except: pass

if __name__ == "__main__":
    if not os.path.exists('/sdcard'): os.system('termux-setup-storage')
    import string
    CharsiPro().menu()
