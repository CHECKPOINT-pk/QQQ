# HIGH PERFORMANCE AUTO CREATE FB (SG/ID MIX) - FIXED VERSION
# AUTHOR : CHARSI BRAND
# VERSION: ASIA REAL MODE 2026 (STABLE)

import os, sys, re, time, random, string, subprocess
from concurrent.futures import ThreadPoolExecutor as ThreadPool

#▬▭▬▭▬▭▬▭[AUTO INSTALLER]▬▭▬▭▬▭▬▭#
def setup():
    modules = ['requests', 'bs4', 'faker', 'fake-useragent']
    for mod in modules:
        try:
            __import__(mod)
        except ImportError:
            print(f"\033[1;33mInstalling {mod}...\033[0m")
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
style = f"{white}[{green}●{white}]"

logo = f"""{green}
  ___ _  _   _   ___  ___ ___ 
 / __| || | /_\ | _ \/ __|_ _|
| (__| __ |/ _ \|   /\__ \| | 
 \___|_||_/_/ \_\_|_\|___/___| {white}ASIA-FIX
{white}━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
{style} {green}AUTHOR   {white}: {yellow}CHARSI BRAND
{style} {green}FIXED    {white}: {cyan}LOCALE ERROR (en_SG)
{style} {green}STATUS   {white}: {green}100% WORKING
{white}━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━"""

class CharsiAsia:
    def __init__(self):
        self.oks = []
        self.cps = []
        self.loop = 0
        self.proxies = []
        
        # --- [SAFE LOCALE FIX] ---
        try:
            # Try to load both ID and SG
            self.fk = Faker(['id_ID', 'en_SG'])
        except Exception:
            try:
                # If en_SG fails, try only ID
                self.fk = Faker(['id_ID', 'en_US'])
                print(f"{yellow}Note: en_SG not supported, using en_US instead.{reset}")
            except:
                # Absolute fallback
                self.fk = Faker()
        
        self.ua = UserAgent()
        self.base_api = "https://api.mail.tm"

    def load_proxies(self):
        try:
            if os.path.exists("proxy.txt"):
                with open("proxy.txt", 'r') as f:
                    self.proxies = [line.strip() for line in f if line.strip()]
                print(f"{style} {green}Proxy Connected: {len(self.proxies)}{reset}")
            else:
                print(f"{style} {red}No proxy.txt found!{reset}")
            time.sleep(1)
        except: pass

    def get_mail_tm(self, proxy_dict):
        try:
            domain_res = requests.get(f"{self.base_api}/domains", proxies=proxy_dict, timeout=10).json()
            domain = domain_res['hydra:member'][0]['domain']
            clean_name = "".join(random.choices(string.ascii_lowercase, k=6)) + str(random.randint(11,99))
            mail = f"{clean_name}@{domain}"
            password = "password123"
            res = requests.post(f"{self.base_api}/accounts", json={"address": mail, "password": password}, proxies=proxy_dict, timeout=10)
            if res.status_code == 201:
                return mail, password
        except: return None, None

    def get_otp_tm(self, mail, pwd, proxy_dict):
        try:
            token_res = requests.post(f"{self.base_api}/token", json={"address": mail, "password": pwd}, proxies=proxy_dict, timeout=10).json()
            token = token_res['token']
            headers = {"Authorization": f"Bearer {token}"}
            for _ in range(12):
                time.sleep(5)
                msgs = requests.get(f"{self.base_api}/messages", headers=headers, proxies=proxy_dict, timeout=10).json()['hydra:member']
                for m in msgs:
                    if "Facebook" in m['subject'] or "FB-" in m['subject']:
                        msg_id = m['id']
                        content = requests.get(f"{self.base_api}/messages/{msg_id}", headers=headers, proxies=proxy_dict, timeout=10).json()
                        otp = re.search(r'\b\d{5,6}\b', content['text'])
                        if otp: return otp.group(0)
            return None
        except: return None

    def create(self):
        proxy_dict = None
        if self.proxies:
            px = random.choice(self.proxies)
            proxy_dict = {'http': f'http://{px}', 'https': f'http://{px}'}

        name = self.fk.name()
        try:
            fname, lname = name.split()[:2]
        except:
            fname = name; lname = "Saputra"

        day, month, year = str(random.randint(1,28)), str(random.randint(1,12)), str(random.randint(1995,2004))
        dob_display = f"{day}/{month}/{year}"
        fb_pwd = f"{fname}@{random.randint(123,999)}"
        mail, mail_pwd = self.get_mail_tm(proxy_dict)

        if not mail: return
        print(f"\r{white}[TRY] {cyan}{fname} {white}| {yellow}{dob_display} {white}| {green}{mail.split('@')[0]}..", end="")

        try:
            ses = requests.Session()
            head = {
                'authority': 'm.facebook.com',
                'user-agent': self.ua.random,
                'accept-language': 'id-ID,id;q=0.9,en-US;q=0.8',
                'referer': 'https://m.facebook.com/reg/',
            }

            reg_html = ses.get('https://m.facebook.com/reg/', headers=head, proxies=proxy_dict, timeout=15).text
            soup = BeautifulSoup(reg_html, 'html.parser')
            data = {i.get('name'): i.get('value') for i in soup.find_all('input') if i.get('name')}

            data.update({
                'firstname': fname, 'lastname': lname,
                'reg_email__': mail, 'reg_passwd__': fb_pwd,
                'birthday_day': day, 'birthday_month': month, 'birthday_year': year,
                'sex': '2'
            })

            res = ses.post('https://m.facebook.com/reg/submit/', data=data, headers=head, proxies=proxy_dict, timeout=15)

            if "c_user" in ses.cookies.get_dict() or "confirm-email" in res.url:
                otp = self.get_otp_tm(mail, mail_pwd, proxy_dict)
                if otp:
                    print(f"\n{green}[CHARSI-OK] {mail} | {fb_pwd} | {otp} | {dob_display}")
                    self.oks.append(mail)
                    open("/sdcard/CHARSI-ASIA-OK.txt","a").write(f"{mail}|{fb_pwd}|{otp}|{dob_display}\n")
                else:
                    uid = ses.cookies.get_dict().get('c_user', mail)
                    print(f"\n{green}[CHARSI-OK] {uid} | {fb_pwd} | {dob_display} (NO-OTP)")
                    self.oks.append(uid)
                    open("/sdcard/CHARSI-ASIA-OK.txt","a").write(f"{uid}|{fb_pwd}|{dob_display}\n")
            else:
                self.cps.append(mail)
        except:
            self.cps.append(mail)
        self.loop += 1

    def menu(self):
        os.system('clear'); print(logo)
        print(f"{white}[{green}1{white}] {green}START ASIA MIX MAKER")
        print(f"{white}[{red}0{white}] {red}EXIT")
        opt = input(f"\n{green}SELECT {white}: {reset}")
        if opt == '1':
            self.load_proxies()
            self.start()
        else: exit()

    def start(self):
        try:
            limit = int(input(f"{green}ACCOUNT LIMIT {white}: {reset}"))
        except: limit = 10
        print(f"{white}━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━")
        with ThreadPool(max_workers=10) as pool:
            for _ in range(limit):
                pool.submit(self.create)
        print(f"\n{white}━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━")
        print(f"{green}DONE! SAVED IN /sdcard/CHARSI-ASIA-OK.txt")

if __name__ == "__main__":
    if not os.path.exists('/sdcard'): os.system('termux-setup-storage')
    CharsiAsia().menu()
