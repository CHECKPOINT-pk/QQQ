# FINAL ULTIMATE AUTO CREATE FB (ASIA-MASTER-2026)
# AUTHOR : CHARSI BRAND
# FEATURES: AUTO-PROTOCOL DETECT, PROXY ROTATION, DEEP SCAN, ANTI-BAN HEADERS

import os, sys, re, time, random, string, subprocess
from concurrent.futures import ThreadPoolExecutor as ThreadPool

#▬▭▬▭▬▭▬▭[AUTO INSTALLER]▬▭▬▭▬▭▬▭#
def setup():
    modules = ['requests', 'bs4', 'faker', 'fake-useragent']
    for mod in modules:
        try:
            __import__(mod)
        except ImportError:
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
cyan = "\033[1;36m"
reset = "\033[0m"

logo = f"""{green}
  ___ _  _   _   ___  ___ ___ 
 / __| || | /_\ | _ \/ __|_ _|
| (__| __ |/ _ \|   /\__ \| | 
 \___|_||_/_/ \_\_|_\|___/___| {white}MASTER-V5
{white}━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
{white}[{green}●{white}] {green}AUTHOR   {white}: {yellow}CHARSI BRAND
{white}[{green}●{white}] {green}PROTOCOL {white}: {cyan}SMART AUTO-DETECT (HTTP/SOCKS)
{white}[{green}●{white}] {green}SECURITY {white}: {green}REAL-DEVICE EMULATION 2026
{white}━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━"""

class CharsiMaster:
    def __init__(self):
        self.oks = []
        self.cps = []
        self.loop = 0
        self.proxies = []
        try:
            self.fk = Faker(['id_ID', 'en_SG'])
        except:
            self.fk = Faker()
        self.ua = UserAgent()
        self.base_api = "https://api.mail.tm"

    def load_proxies(self):
        if os.path.exists("proxy.txt"):
            with open("proxy.txt", "r") as f:
                self.proxies = [line.strip() for line in f if line.strip()]
            print(f"{green}[!] {len(self.proxies)} Proxies Loaded.{reset}")
        else:
            print(f"{red}[!] proxy.txt missing. Running Direct IP (Risky).{reset}")
        time.sleep(1)

    def format_proxy(self, px):
        """Automatically detects and formats proxy protocol"""
        if not px: return None
        # Agar user ne protocol nahi likha toh default socks5 check karega
        if "socks5://" in px or "http://" in px or "https://" in px:
            return {"http": px, "https": px}
        # Defaulting to socks5 for better stability
        return {"http": f"socks5://{px}", "https": f"socks5://{px}"}

    def get_mail_and_token(self, proxy):
        try:
            domain_res = requests.get(f"{self.base_api}/domains", proxies=proxy, timeout=10).json()
            domain = domain_res['hydra:member'][0]['domain']
            user = "".join(random.choices(string.ascii_lowercase, k=9))
            mail = f"{user}@{domain}"
            password = "Master_User_2026"
            
            requests.post(f"{self.base_api}/accounts", json={"address": mail, "password": password}, proxies=proxy)
            tok_res = requests.post(f"{self.base_api}/token", json={"address": mail, "password": password}, proxies=proxy).json()
            return mail, tok_res['token']
        except: return None, None

    def fetch_otp(self, token, proxy):
        headers = {"Authorization": f"Bearer {token}"}
        for _ in range(12): 
            time.sleep(6)
            try:
                msgs = requests.get(f"{self.base_api}/messages", headers=headers, proxies=proxy).json()['hydra:member']
                for m in msgs:
                    if "facebook" in str(m['from']['address']).lower() or "FB-" in m['subject']:
                        m_id = m['id']
                        content = requests.get(f"{self.base_api}/messages/{m_id}", headers=headers, proxies=proxy).json()
                        otp = re.search(r'\b\d{5,6}\b', content['text'])
                        if otp: return otp.group(0)
            except: pass
        return None

    def create(self):
        px_raw = random.choice(self.proxies) if self.proxies else None
        current_proxy = self.format_proxy(px_raw)
        
        name = self.fk.name()
        fname, lname = (name.split() + ["Saputra"])[:2]
        day, month, year = str(random.randint(1,28)), str(random.randint(1,12)), str(random.randint(1992,2004))
        pwd = f"{fname}{random.randint(10,99)}#2026"
        
        mail, token = self.get_mail_and_token(current_proxy)
        if not mail: return

        print(f"\r{white}[V5] {self.loop} | {green}OK:{len(self.oks)} {white}| {cyan}ACTIVE:{fname}", end="")

        try:
            ses = requests.Session()
            # Advanced Real-Device Browser Headers
            headers = {
                'authority': 'm.facebook.com',
                'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8',
                'accept-language': 'id-ID,id;q=0.9,en-US;q=0.8,en;q=0.7',
                'dpr': '2.75',
                'sec-ch-prefers-color-scheme': 'light',
                'sec-ch-ua': '"Not_A Brand";v="8", "Chromium";v="120", "Google Chrome";v="120"',
                'sec-ch-ua-mobile': '?1',
                'sec-ch-ua-platform': '"Android"',
                'user-agent': self.ua.random,
                'viewport-width': '980',
            }

            # Phase 1: Registration Page
            reg_html = ses.get('https://m.facebook.com/reg/', headers=headers, proxies=current_proxy).text
            soup = BeautifulSoup(reg_html, 'html.parser')
            form = {i.get('name'): i.get('value') for i in soup.find_all('input') if i.get('name')}
            
            form.update({
                'firstname': fname, 'lastname': lname,
                'reg_email__': mail, 'reg_passwd__': pwd,
                'birthday_day': day, 'birthday_month': month, 'birthday_year': year,
                'sex': '2' if random.random() > 0.4 else '1'
            })

            # Phase 2: Create Account
            submit = ses.post('https://m.facebook.com/reg/submit/', data=form, headers=headers, proxies=current_proxy)

            if "confirm-email" in submit.url or "checkpoint" not in submit.url:
                print(f"\n{yellow}[SCANNING OTP] {mail}...")
                otp = self.fetch_otp(token, current_proxy)
                if otp:
                    print(f"{green}[CHARSI-OK] {mail} | {pwd} | {otp} | {fname}")
                    self.oks.append(mail)
                    open("/sdcard/CHARSI-MASTER-OK.txt", "a").write(f"{mail}|{pwd}|{otp}|{fname}|{day}/{month}/{year}\n")
                else: self.cps.append(mail)
            else: self.cps.append(mail)
        except: self.cps.append(mail)
        
        self.loop += 1

    def menu(self):
        os.system('clear'); print(logo)
        print(f"{white}[{green}1{white}] {green}START MASTER CREATION (FULL METHOD)")
        print(f"{white}[{red}0{white}] {red}EXIT")
        opt = input(f"\n{green}SELECT {white}: {reset}")
        if opt == '1':
            self.load_proxies()
            limit = int(input(f"{green}ACCOUNT LIMIT {white}: {reset}"))
            print(f"{white}━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━")
            with ThreadPool(max_workers=5) as pool:
                for _ in range(limit):
                    pool.submit(self.create)
            print(f"\n{green}FINISHED. RESULTS SAVED IN /sdcard/CHARSI-MASTER-OK.txt")
        else: sys.exit()

if __name__ == "__main__":
    if not os.path.exists('/sdcard'): os.system('termux-setup-storage')
    CharsiMaster().menu()
