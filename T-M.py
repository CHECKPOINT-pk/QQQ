# HIGH PERFORMANCE AUTO CREATE FB (CYBER-GOLD EDITION)
# AUTHOR : CHARSI BRAND
# VERSION: 2026.0.1 (ULTRA)

import os, sys, re, time, random, uuid, subprocess, string
from concurrent.futures import ThreadPoolExecutor as ThreadPool

#▬▭▬▭▬▭▬▭[AUTO INSTALLER]▬▭▬▭▬▭▬▭#
def setup():
    modules = ['requests', 'bs4', 'faker']
    for mod in modules:
        try:
            __import__(mod)
        except ImportError:
            print(f"\033[1;37m[!] Installing {mod}...")
            subprocess.check_call([sys.executable, "-m", "pip", "install", mod])

setup()

import requests
from bs4 import BeautifulSoup
from faker import Faker

#▬▭▬▭▬▭▬▭[PREMIUM COLORS]▬▭▬▭▬▭▬▭#
cyan = "\033[1;36m"
gold = "\033[1;33m"
white = "\033[1;37m"
red = "\033[1;31m"
grey = "\033[1;90m"
reset = "\033[0m"

#▬▭▬▭▬▭▬▭[MODERN ASSETS]▬▭▬▭▬▭▬▭#
class Assets:
    def get_ua(self):
        # 2026 Latest Device Matrix
        devices = [
            f"Mozilla/5.0 (Linux; Android 15; SM-S938B) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/{random.randint(128,142)}.0.0.0 Mobile Safari/537.36",
            f"Mozilla/5.0 (Linux; Android 14; Pixel 9 Pro XL Build/UQ1A.{random.randint(23,26)}0105.001) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/{random.randint(128,142)}.0.6613.127 Mobile Safari/537.36",
            f"Mozilla/5.0 (Linux; Android 15; Nothing Phone (3)) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/{random.randint(128,142)}.0.0.0 Mobile Safari/537.36"
        ]
        return random.choice(devices)

#▬▭▬▭▬▭▬▭[CYBER LOGO]▬▭▬▭▬▭▬▭#
logo = f"""
{cyan}   ____ _   _  _    ____  ____ ___  
{cyan}  / ___| | | |/ \  |  _ \/ ___|_ _| 
{gold} | |   | |_| / _ \ | |_) \___ \| |  
{gold} | |___|  _ / ___ \|  _ < ___) | |  
{white}  \____|_| /_/   \_\_| \_\____/___| {cyan}V4.0
{grey}━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
{cyan}[●] {white}AUTHOR   {grey}: {gold}CHARSI BRAND
{cyan}[●] {white}ENGINE   {grey}: {gold}V8-TURBO (2026)
{cyan}[●] {white}SECURITY {grey}: {cyan}ANTI-SUSPEND ENABLED
{grey}━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━"""

class CharsiGold:
    def __init__(self):
        self.oks = []
        self.cps = []
        self.loop = 0
        self.fk = Faker()
        self.assets = Assets()

    def get_mail(self):
        user = "".join(random.choices(string.ascii_lowercase + string.digits, k=7))
        return f"{user}@1secmail.com"

    def get_otp(self, email):
        login, domain = email.split('@')
        for i in range(12):
            time.sleep(5)
            try:
                url = f"https://www.1secmail.com/api/v1/?action=getMessages&login={login}&domain={domain}"
                msgs = requests.get(url).json()
                for m in msgs:
                    if "Facebook" in m['subject'] or "FB-" in m['subject']:
                        msg_id = m['id']
                        read_url = f"https://www.1secmail.com/api/v1/?action=readMessage&login={login}&domain={domain}&id={msg_id}"
                        content = requests.get(read_url).json()
                        otp = re.search(r'\b\d{5}\b', content['body'])
                        if otp: return otp.group(0)
            except: pass
        return None

    def menu(self):
        os.system('clear'); print(logo)
        print(f"{cyan}[1] {white}CREATE UNLIMITED ACCOUNTS {gold}(BEST)")
        print(f"{cyan}[2] {white}JOIN OUR TELEGRAM")
        print(f"{red}[0] {white}EXIT SYSTEM")
        choice = input(f"\n{cyan}┌─[{white}SELECT{cyan}]\n└─╼ {gold}")
        if choice == '1': self.start()
        else: exit()

    def start(self):
        os.system('clear'); print(logo)
        try:
            limit = int(input(f"{cyan}[?] {white}ENTER ACCOUNT LIMIT {grey}: {gold}"))
        except: limit = 10
        print(f"{grey}━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━")
        
        with ThreadPool(max_workers=30) as pool:
            for _ in range(limit):
                pool.submit(self.create_engine)
        
        print(f"\n{grey}━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━")
        print(f"{cyan}[#] {white}PROCESS COMPLETED")
        print(f"{cyan}[#] {white}TOTAL OK: {gold}{len(self.oks)}")
        print(f"{cyan}[#] {white}TOTAL CP: {red}{len(self.cps)}")

    def create_engine(self):
        ua = self.assets.get_ua()
        first = self.fk.first_name()
        last = self.fk.last_name()
        mail = self.get_mail()
        pwd = first + str(random.randint(111, 999)) + "@"
        
        session = requests.Session()
        
        # Advanced 2026 Fingerprint Headers
        headers = {
            'authority': 'm.facebook.com',
            'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7',
            'accept-language': 'en-GB,en-US;q=0.9,en;q=0.8',
            'sec-ch-prefers-color-scheme': 'light',
            'sec-ch-ua': f'"Not/A)Brand";v="8", "Chromium";v="{random.randint(128,135)}", "Google Chrome";v="{random.randint(128,135)}"',
            'sec-ch-ua-full-version-list': f'"Not/A)Brand";v="8.0.0.0", "Chromium";v="131.0.6778.204", "Google Chrome";v="131.0.6778.204"',
            'sec-ch-ua-mobile': '?1',
            'sec-ch-ua-platform': '"Android"',
            'sec-fetch-dest': 'document',
            'sec-fetch-mode': 'navigate',
            'sec-fetch-site': 'none',
            'sec-fetch-user': '?1',
            'upgrade-insecure-requests': '1',
            'user-agent': ua,
        }

        try:
            # Registration Initial Hit
            res = session.get('https://m.facebook.com/reg/', headers=headers)
            soup = BeautifulSoup(res.text, 'html.parser')
            form_data = {i.get('name'): i.get('value') for i in soup.find_all('input') if i.get('name')}
            
            # Simulated typing delay
            time.sleep(random.uniform(2, 4))
            
            form_data.update({
                'firstname': first, 'lastname': last,
                'reg_email__': mail, 'reg_passwd__': pwd,
                'birthday_day': str(random.randint(1,28)),
                'birthday_month': str(random.randint(1,12)),
                'birthday_year': str(random.randint(1992,2005)),
                'sex': str(random.randint(1,2))
            })

            # Submit Data
            post_headers = headers.copy()
            post_headers['origin'] = 'https://m.facebook.com'
            post_headers['referer'] = 'https://m.facebook.com/reg/'
            
            response = session.post('https://m.facebook.com/reg/submit/', data=form_data, headers=post_headers)
            
            if "c_user" in session.cookies.get_dict():
                uid = session.cookies.get_dict()['c_user']
                self.oks.append(uid)
                print(f"\n{cyan}[CHARSI-OK] {uid} | {pwd}")
                open("/sdcard/CHARSI-OK.txt","a").write(f"{uid}|{pwd}\n")
            
            elif "confirm-email" in response.url or "checkpoint" in response.url:
                print(f"\r{grey}[{gold}VERIFYING{grey}] {mail}..       ", end="")
                otp = self.get_otp(mail)
                if otp:
                    print(f"\n{cyan}[CHARSI-OK] {mail} | {pwd} | {otp}")
                    self.oks.append(mail)
                    open("/sdcard/CHARSI-OK.txt","a").write(f"{mail}|{pwd}|{otp}\n")
                else:
                    self.cps.append(mail)
            else:
                self.cps.append(mail)

        except: pass
        
        self.loop += 1
        print(f"\r{cyan}[RUNNING] {self.loop} {white}| {cyan}OK:{len(self.oks)} {red}CP:{len(self.cps)}", end="")

if __name__ == "__main__":
    if not os.path.exists('/sdcard'): os.system('termux-setup-storage')
    CharsiGold().menu()
