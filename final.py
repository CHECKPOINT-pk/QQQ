# FINAL ULTIMATE V6 - FULL AUTO-CONFIRM & VERIFY
# AUTHOR : CHARSI BRAND
# POWERED BY : ASIA ELITE REAL-TIME ENGINE

import os, sys, re, time, random, string, subprocess
from concurrent.futures import ThreadPoolExecutor as ThreadPool

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

# COLORS
green, white, red, yellow, cyan, reset = "\x1b[38;5;49m", "\033[1;37m", "\x1b[38;5;160m", "\033[1;33m", "\033[1;36m", "\033[0m"

logo = f"""{green}
  ___ _  _   _   ___  ___ ___ 
 / __| || | /_\ | _ \/ __|_ _|
| (__| __ |/ _ \|   /\__ \| | 
 \___|_||_/_/ \_\_|_\|___/___| {white}MASTER-V6
{white}━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
{white}[{green}●{white}] {green}SYSTEM   {white}: {yellow}AUTO-CONFIRM & VERIFY (OTP)
{white}[{green}●{white}] {green}COUNTRY  {white}: {cyan}SINGAPORE / INDONESIA
{white}[{green}●{white}] {green}STATUS   {white}: {green}STABLE 2026
{white}━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━"""

class CharsiV6:
    def __init__(self):
        self.oks, self.cps, self.loop = [], [], 0
        self.proxies = []
        try: self.fk = Faker(['id_ID', 'en_SG'])
        except: self.fk = Faker()
        self.ua = UserAgent()
        self.base_api = "https://api.mail.tm"

    def load_proxies(self):
        if os.path.exists("proxy.txt"):
            with open("proxy.txt", "r") as f:
                self.proxies = [line.strip() for line in f if line.strip()]
            print(f"{green}[!] {len(self.proxies)} Proxies Loaded.{reset}")
        else:
            print(f"{red}[!] proxy.txt missing!{reset}")

    def get_proxy(self):
        if not self.proxies: return None
        px = random.choice(self.proxies)
        return {"http": f"socks5://{px}", "https": f"socks5://{px}"}

    def get_mail_token(self, proxy):
        try:
            domain = requests.get(f"{self.base_api}/domains", proxies=proxy, timeout=10).json()['hydra:member'][0]['domain']
            user = "".join(random.choices(string.ascii_lowercase + string.digits, k=10))
            mail = f"{user}@{domain}"
            passw = "Master@123"
            requests.post(f"{self.base_api}/accounts", json={"address": mail, "password": passw}, proxies=proxy)
            token = requests.post(f"{self.base_api}/token", json={"address": mail, "password": passw}, proxies=proxy).json()['token']
            return mail, token
        except: return None, None

    def fetch_otp(self, token, proxy):
        headers = {"Authorization": f"Bearer {token}"}
        for _ in range(15):
            time.sleep(5)
            try:
                msgs = requests.get(f"{self.base_api}/messages", headers=headers, proxies=proxy).json()['hydra:member']
                for m in msgs:
                    if "Facebook" in m['subject'] or "FB-" in m['subject']:
                        content = requests.get(f"{self.base_api}/messages/{m['id']}", headers=headers, proxies=proxy).json()
                        otp = re.search(r'\b\d{5,6}\b', content['text'])
                        if otp: return otp.group(0)
            except: pass
        return None

    def confirm_account(self, ses, otp, proxy):
        """SUBMITS OTP TO FACEBOOK FOR FULL VERIFICATION"""
        try:
            res = ses.get('https://m.facebook.com/confirmemail.php', proxies=proxy).text
            soup = BeautifulSoup(res, 'html.parser')
            # Extracting the confirmation form
            form_data = {i.get('name'): i.get('value') for i in soup.find_all('input') if i.get('name')}
            form_data['code'] = otp
            # Submitting OTP
            conf = ses.post('https://m.facebook.com/confirmemail.php', data=form_data, proxies=proxy)
            if "c_user" in ses.cookies.get_dict(): return True
            return False
        except: return False

    def create(self):
        proxy = self.get_proxy()
        name = self.fk.name()
        fname, lname = (name.split() + ["Saputra"])[:2]
        mail, token = self.get_mail_token(proxy)
        if not mail: return
        
        pwd = f"{fname}@{random.randint(111,999)}"
        print(f"\r{white}[TRYING] {self.loop} | {green}OK:{len(self.oks)} {white}| {cyan}{fname}", end="")

        try:
            ses = requests.Session()
            head = {'authority': 'm.facebook.com', 'user-agent': self.ua.random, 'accept-language': 'id-ID,id;q=0.9,en-US;q=0.8'}
            
            # Step 1: Reg
            reg_page = ses.get('https://m.facebook.com/reg/', headers=head, proxies=proxy).text
            data = {i.get('name'): i.get('value') for i in BeautifulSoup(reg_page, 'html.parser').find_all('input') if i.get('name')}
            data.update({'firstname': fname, 'lastname': lname, 'reg_email__': mail, 'reg_passwd__': pwd, 'birthday_day': str(random.randint(1,28)), 'birthday_month': str(random.randint(1,12)), 'birthday_year': str(random.randint(1995,2004)), 'sex': '2'})
            
            # Step 2: Submit
            submit = ses.post('https://m.facebook.com/reg/submit/', data=data, headers=head, proxies=proxy)
            
            # Step 3: OTP Scan & Auto-Confirm
            print(f"\n{yellow}[SCANNING] OTP for {fname}...", end="")
            otp = self.fetch_otp(token, proxy)
            
            if otp:
                verified = self.confirm_account(ses, otp, proxy)
                status = "VERIFIED" if verified else "NOT-CONFIRMED"
                print(f"\n{green}[OK-{status}] {mail} | {pwd} | {otp}")
                self.oks.append(mail)
                open("/sdcard/CHARSI-V6-FULL.txt", "a").write(f"{mail}|{pwd}|{otp}|{status}\n")
            else:
                self.cps.append(mail)
        except: self.cps.append(mail)
        self.loop += 1

    def menu(self):
        os.system('clear'); print(logo)
        print(f"{white}[1] START AUTO-CREATE + AUTO-VERIFY")
        print(f"{white}[0] EXIT")
        if input(f"\n{green}SELECT: {reset}") == '1':
            self.load_proxies()
            limit = int(input(f"{green}LIMIT: {reset}"))
            with ThreadPool(max_workers=5) as pool:
                for _ in range(limit): pool.submit(self.create)
        else: sys.exit()

if __name__ == "__main__":
    if not os.path.exists('/sdcard'): os.system('termux-setup-storage')
    CharsiV6().menu()
