import os, sys, re, time, random, string, subprocess
from concurrent.futures import ThreadPoolExecutor as ThreadPool

# --- [AUTO-INSTALLER] ---
def setup():
    modules = ['requests', 'bs4', 'faker', 'fake-useragent']
    for mod in modules:
        try: __import__(mod)
        except: subprocess.check_call([sys.executable, "-m", "pip", "install", mod])

setup()

import requests
from bs4 import BeautifulSoup
from faker import Faker
from fake_useragent import UserAgent

# --- [FILE PATHS] ---
if os.path.exists('/sdcard'):
    ok_path = '/sdcard/CHARSI_MASTER_OK.txt'
else:
    ok_path = 'CHARSI_MASTER_OK.txt'

green, white, red, yellow, cyan, reset = "\x1b[38;5;49m", "\033[1;37m", "\x1b[38;5;160m", "\033[1;33m", "\033[1;36m", "\033[0m"

logo = f"""{green}
  ██████╗██╗  ██╗ █████╗ ██████╗ ███████╗██╗
 ██╔════╝██║  ██║██╔══██╗██╔══██╗██╔════╝██║
 ██║     ███████║███████║██████╔╝███████╗██║
 ██║     ██╔══██║██╔══██║██╔══██╗╚════██║██║
 ╚██████╗██║  ██║██║  ██║██║  ██║███████║██║
  ╚═════╝╚═╝  ╚═╝╚═╝  ╚═╝╚═╝  ╚═╝╚══════╝╚═╝ {white}v5.1-FIX
{white}━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
{white}[{green}●{white}] {green}LOCALE   {white}: {yellow}FIXED (en_SG Error Patch)
{white}[{green}●{white}] {green}ENGINE   {white}: {cyan}SELF-HEALING v5.1
{white}━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━"""

class CharsiMaster:
    def __init__(self):
        self.loop, self.oks, self.cps = 0, [], []
        self.proxies = []
        self.ua = UserAgent()
        self.base_api = "https://api.mail.tm"
        
        # --- [LOCALE ERROR FIX] ---
        try:
            # Try to load SG and ID
            self.fk = Faker(['id_ID', 'en_SG'])
        except:
            try:
                # If en_SG fails, fallback to ID and US
                self.fk = Faker(['id_ID', 'en_US'])
            except:
                # Absolute fallback to default
                self.fk = Faker()

    def load_proxies(self):
        if os.path.exists("proxy.txt"):
            with open("proxy.txt", 'r') as f:
                self.proxies = [line.strip() for line in f if line.strip()]

    def get_mail_and_token(self, px):
        try:
            domains = requests.get(f"{self.base_api}/domains", proxies=px, timeout=10).json()['hydra:member']
            domain = random.choice(domains)['domain']
            user = "".join(random.choices(string.ascii_lowercase, k=8))
            mail = f"{user}@{domain}"
            password = "Pass" + str(random.randint(111,999))
            res = requests.post(f"{self.base_api}/accounts", json={"address": mail, "password": password}, proxies=px, timeout=10)
            if res.status_code == 201:
                token_res = requests.post(f"{self.base_api}/token", json={"address": mail, "password": password}, proxies=px, timeout=10).json()
                return mail, password, token_res['token']
        except: return None, None, None
        return None, None, None

    def fetch_otp(self, token, px):
        headers = {"Authorization": f"Bearer {token}"}
        for _ in range(12):
            time.sleep(4)
            try:
                msgs = requests.get(f"{self.base_api}/messages", headers=headers, proxies=px, timeout=10).json()['hydra:member']
                for m in msgs:
                    content = requests.get(f"{self.base_api}/messages/{m['id']}", headers=headers, proxies=px, timeout=10).json()
                    otp = re.search(r'\b\d{5,6}\b', content['text'])
                    if otp: return otp.group(0)
            except: pass
        return None

    def create(self):
        self.loop += 1
        sys.stdout.write(f"\r{white}[RUNNING] {self.loop} | {green}OK:{len(self.oks)} {red}CP:{len(self.cps)} "); sys.stdout.flush()
        
        px = {'http': f'http://{random.choice(self.proxies)}', 'https': f'http://{random.choice(self.proxies)}'} if self.proxies else None
        
        name = self.fk.name()
        fname, lname = (name.split() + ["Saputra"])[:2]
        mail, m_pass, token = self.get_mail_and_token(px)
        if not mail: return
        
        fb_pwd = f"{fname}@{random.randint(11,99)}#"

        try:
            ses = requests.Session()
            h = {
                'authority': 'm.facebook.com',
                'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,*/*;q=0.8',
                'accept-language': 'id-ID,id;q=0.9,en-US;q=0.8',
                'sec-ch-ua-mobile': '?1',
                'user-agent': self.ua.random,
            }

            reg_page = ses.get('https://m.facebook.com/reg/', headers=h, proxies=px, timeout=15).text
            soup = BeautifulSoup(reg_page, 'html.parser')
            data = {i.get('name'): i.get('value') for i in soup.find_all('input') if i.get('name')}
            
            data.update({
                'firstname': fname, 'lastname': lname, 'reg_email__': mail, 
                'reg_passwd__': fb_pwd, 'birthday_day': str(random.randint(1,28)),
                'birthday_month': str(random.randint(1,12)), 'birthday_year': str(random.randint(1994,2005)),
                'sex': '2'
            })

            res = ses.post('https://m.facebook.com/reg/submit/', data=data, headers=h, proxies=px, timeout=15)

            if "c_user" in ses.cookies.get_dict():
                otp = self.fetch_otp(token, px)
                uid = ses.cookies.get_dict().get('c_user')
                print(f"\n{green}[MASTER-OK] {uid} | {fb_pwd} | {otp if otp else 'NO-OTP'}")
                self.oks.append(uid)
                with open(ok_path, "a") as f: f.write(f"{uid}|{fb_pwd}|{mail}|{otp}\n")
            elif "checkpoint" in res.url:
                self.cps.append(mail)
        except: pass

    def menu(self):
        os.system('clear' if os.name == 'posix' else 'cls')
        print(logo)
        self.load_proxies()
        try:
            limit = int(input(f"{white}[?] Target Accounts: {green}"))
            threads = int(input(f"{white}[?] Thread Power: {green}"))
        except: limit, threads = 10, 5
        
        with ThreadPool(max_workers=threads) as executor:
            for _ in range(limit): executor.submit(self.create)
        
        print(f"\n{green}[FINISH] OK: {len(self.oks)} | Results: {ok_path}")

if __name__ == "__main__":
    CharsiMaster().menu()
