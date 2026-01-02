# FINAL MASTER V7 (2026) - THE BEAST MODE
# AUTHOR : CHARSI BRAND
# FEATURES: DEVICE ID CHANGER, AUTO-CONFIRM OTP, FAST PROXY ROTATION

import os, sys, re, time, random, string, subprocess, json
from concurrent.futures import ThreadPoolExecutor as ThreadPool

def setup():
    modules = ['requests', 'bs4', 'faker', 'fake-useragent']
    for mod in modules:
        try: __import__(mod)
        except ImportError: subprocess.check_call([sys.executable, "-m", "pip", "install", mod])

setup()

import requests
from bs4 import BeautifulSoup
from faker import Faker
from fake_useragent import UserAgent

# STYLE & LOGO
green, white, red, yellow, cyan, reset = "\x1b[38;5;49m", "\033[1;37m", "\x1b[38;5;160m", "\033[1;33m", "\033[1;36m", "\033[0m"

logo = f"""{green}
  __  __   _   ___ _____ ___ ___ 
 |  \/  | /_\ / __|_   _| __| _ \\
 | |\/| |/ _ \\__ \ | | | _||   /
 |_|  |_/_/ \_\___/ |_| |___|_|_\\ {white}V7.0
{white}━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
{white}[{green}●{white}] {green}AUTHOR   {white}: {yellow}CHARSI BRAND
{white}[{green}●{white}] {green}DEVICE   {white}: {cyan}SMART ID CHANGER (SAMSUNG/APPLE)
{white}[{green}●{white}] {green}OTP MODE {white}: {green}AUTO-VERIFY & CONFIRM
{white}━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━"""

class CharsiBeast:
    def __init__(self):
        self.oks, self.cps, self.loop = [], [], 0
        self.proxies = []
        try: self.fk = Faker(['id_ID', 'en_SG'])
        except: self.fk = Faker()
        self.ua = UserAgent()
        self.base_api = "https://api.mail.tm"

    def get_device_info(self):
        """Generates fake hardware info to bypass FB detection"""
        models = ['SM-G998B', 'SM-A525F', 'iPhone 13 Pro', 'Pixel 6', 'Redmi Note 11']
        return {
            'model': random.choice(models),
            'id': "".join(random.choices(string.digits + "ABCDEF", k=16)),
            'ua': self.ua.random
        }

    def load_proxies(self):
        if os.path.exists("proxy.txt"):
            with open("proxy.txt", "r") as f:
                self.proxies = [line.strip() for line in f if line.strip()]
            print(f"{green}[!] {len(self.proxies)} High-Speed Proxies Loaded.{reset}")
        else:
            print(f"{red}[!] proxy.txt not found. Please run scraper first!{reset}")

    def fetch_otp(self, token, proxy):
        """Advanced Inbox Scraper with Token Bypass"""
        headers = {"Authorization": f"Bearer {token}"}
        for _ in range(15): # 75 Seconds scan
            time.sleep(5)
            try:
                msgs = requests.get(f"{self.base_api}/messages", headers=headers, proxies=proxy, timeout=5).json()['hydra:member']
                for m in msgs:
                    if "Facebook" in str(m['subject']) or "FB-" in str(m['subject']):
                        c = requests.get(f"{self.base_api}/messages/{m['id']}", headers=headers, proxies=proxy).json()
                        otp = re.search(r'\b\d{5,6}\b', c['text'])
                        if otp: return otp.group(0)
            except: pass
        return None

    def confirm_fb(self, ses, otp, proxy):
        """Submits the code to FB and Verifies the account"""
        try:
            # Facebook confirmation URL parsing
            conf_page = ses.get('https://m.facebook.com/confirmemail.php', proxies=proxy, timeout=10).text
            soup = BeautifulSoup(conf_page, 'html.parser')
            form = {i.get('name'): i.get('value') for i in soup.find_all('input') if i.get('name')}
            form['code'] = otp
            ses.post('https://m.facebook.com/confirmemail.php', data=form, proxies=proxy, timeout=10)
            return True
        except: return False

    def create(self):
        # 1. Setup Proxy & Device
        px_raw = random.choice(self.proxies) if self.proxies else None
        proxy = {"http": f"socks5://{px_raw}", "https": f"socks5://{px_raw}"} if px_raw else None
        device = self.get_device_info()
        
        # 2. Generate Identity
        name = self.fk.name()
        fname, lname = (name.split() + ["Saputra"])[:2]
        day, month, year = str(random.randint(1,28)), str(random.randint(1,12)), str(random.randint(1993,2005))
        pwd = f"{fname}@{random.randint(11,99)}#"
        
        # 3. Create Mail
        try:
            dom = requests.get(f"{self.base_api}/domains", proxies=proxy, timeout=5).json()['hydra:member'][0]['domain']
            mail = f"{''.join(random.choices(string.ascii_lowercase, k=8))}@{dom}"
            requests.post(f"{self.base_api}/accounts", json={"address": mail, "password": "User@123"}, proxies=proxy)
            token = requests.post(f"{self.base_api}/token", json={"address": mail, "password": "User@123"}, proxies=proxy).json()['token']
        except: return

        print(f"\r{white}[V7-RUN] {self.loop} | {green}OK:{len(self.oks)} {white}| {cyan}TRY:{fname}", end="")

        try:
            ses = requests.Session()
            head = {
                'authority': 'm.facebook.com',
                'user-agent': device['ua'],
                'accept-language': 'id-ID,en-US;q=0.9',
                'sec-ch-ua-platform': '"Android"',
                'x-fb-device-model': device['model'], # Hardware Emulation
            }

            # Phase: Registration
            res = ses.get('https://m.facebook.com/reg/', headers=head, proxies=proxy).text
            form_data = {i.get('name'): i.get('value') for i in BeautifulSoup(res, 'html.parser').find_all('input') if i.get('name')}
            form_data.update({'firstname': fname, 'lastname': lname, 'reg_email__': mail, 'reg_passwd__': pwd, 'birthday_day': day, 'birthday_month': month, 'birthday_year': year, 'sex': '2'})
            
            submit = ses.post('https://m.facebook.com/reg/submit/', data=form_data, headers=head, proxies=proxy)

            # Phase: OTP & Verify
            print(f"\n{yellow}[SCAN] OTP for {mail}...", end="")
            otp = self.fetch_otp(token, proxy)
            
            if otp:
                self.confirm_fb(ses, otp, proxy)
                print(f"\n{green}[VERIFIED-OK] {mail} | {pwd} | {otp} | {device['model']}")
                self.oks.append(mail)
                open("/sdcard/CHARSI-V7-MASTER.txt", "a").write(f"{mail}|{pwd}|{otp}|{device['model']}\n")
            else: self.cps.append(mail)
        except: self.cps.append(mail)
        self.loop += 1

    def menu(self):
        os.system('clear'); print(logo)
        print(f"{white}[1] START HEAVY CREATOR (V7 MASTER)")
        print(f"{white}[0] EXIT")
        if input(f"\n{green}SELECT: {reset}") == '1':
            self.load_proxies()
            limit = int(input(f"{green}LIMIT: {reset}"))
            with ThreadPool(max_workers=5) as pool:
                for _ in range(limit): pool.submit(self.create)
            print(f"\n{green}DONE! SAVED: /sdcard/CHARSI-V7-MASTER.txt")
        else: sys.exit()

if __name__ == "__main__":
    if not os.path.exists('/sdcard'): os.system('termux-setup-storage')
    CharsiBeast().menu()
