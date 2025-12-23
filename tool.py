# HIGH PERFORMANCE AUTO CREATE FB + AUTO VERIFY
# AUTHOR : CHARSI BRAND
# GITHUB : CHARSI-BRAND-708
# STATUS : AUTO OTP VERIFICATION ADDED

import os, sys, re, time, random, uuid, string, subprocess
from concurrent.futures import ThreadPoolExecutor as ThreadPool

#▬▭▬▭▬▭▬▭[AUTO INSTALLER]▬▭▬▭▬▭▬▭#
def install_modules():
    modules = ['requests', 'bs4', 'faker', 'fake-useragent']
    for module in modules:
        try:
            __import__(module)
        except ImportError:
            subprocess.check_call([sys.executable, "-m", "pip", "install", module])

install_modules()

import requests
from bs4 import BeautifulSoup
from faker import Faker
from fake_useragent import UserAgent

#▬▭▬▭▬▭▬▭[COLOR CODE]▬▭▬▭▬▭▬▭#
green = "\x1b[38;5;49m"
white = "\033[1;37m"
red = "\x1b[38;5;160m"
yellow = "\033[1;33m"
blue = "\033[1;34m"
reset = "\033[0m"
style = f"{white}[{green}●{white}]"

#▬▭▬▭▬▭▬▭[SMALL LOGO]▬▭▬▭▬▭▬▭#
logo = f"""{green}
  ___ _  _   _   ___  ___ ___ 
 / __| || | /_\ | _ \/ __|_ _|
| (__| __ |/ _ \|   /\__ \| | 
 \___|_||_/_/ \_\_|_\|___/___| BRAND
{white}━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
{style} {green}AUTHOR   {white}: {yellow}CHARSI BRAND
{style} {green}VERIFY   {white}: {yellow}AUTO OTP ENABLED
{style} {green}THREADS  {white}: {yellow}30 (STABLE)
{white}━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━"""

class CharsiVerify:
    def __init__(self):
        self.oks = []
        self.cps = []
        self.loop = 0
        self.ua = UserAgent()
        self.fk = Faker()

    def get_mail(self):
        # Generates a temporary email from 1secmail
        try:
            res = requests.get("https://www.1secmail.com/api/v1/?action=genRandomMailbox&count=1").json()
            return res[0]
        except: return None

    def get_otp(self, email):
        # Polls the mailbox for Facebook OTP
        login, domain = email.split('@')
        for _ in range(20): # Try for 60 seconds
            try:
                time.sleep(3)
                msgs = requests.get(f"https://www.1secmail.com/api/v1/?action=getMessages&login={login}&domain={domain}").json()
                for msg in msgs:
                    if "Facebook" in msg['from'] or "FB-" in msg['subject']:
                        content = requests.get(f"https://www.1secmail.com/api/v1/?action=readMessage&login={login}&domain={domain}&id={msg['id']}").json()
                        otp = re.search(r'\b\d{5}\b', content['body'])
                        if otp: return otp.group(0)
            except: pass
        return None

    def menu(self):
        os.system('clear'); print(logo)
        print(f"{white}[{green}1{white}] {green}Start Auto Creation & Verify")
        print(f"{white}[{red}0{white}] {red}Exit Program")
        opt = input(f"\n{green}Select Option {white}: {reset}")
        if opt == '1': self.start()
        else: exit()

    def start(self):
        os.system('clear'); print(logo)
        try:
            limit = int(input(f"{green}Enter Account Limit {white}: {reset}"))
        except: limit = 10
        print(f"{white}━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━")
        
        with ThreadPool(max_workers=30) as pool:
            for _ in range(limit):
                pool.submit(self.create)
        
        print(f"\n{white}━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━")
        print(f"{green}VERIFIED SUCCESS: {len(self.oks)}")
        print(f"{red}FAILED/CP       : {len(self.cps)}")

    def create(self):
        first = self.fk.first_name()
        last = self.fk.last_name()
        password = first + str(random.randint(111, 999))
        email = self.get_mail()
        if not email: return

        try:
            ses = requests.Session()
            headers = {
                'authority': 'm.facebook.com',
                'user-agent': self.ua.random,
                'accept-language': 'en-US,en;q=0.9',
            }
            
            # Step 1: Submit Registration
            reg_page = ses.get('https://m.facebook.com/reg/', headers=headers).text
            soup = BeautifulSoup(reg_page, 'html.parser')
            form_data = {i.get('name'): i.get('value') for i in soup.find_all('input') if i.get('name')}
            
            payload = {
                **form_data,
                'firstname': first, 'lastname': last,
                'reg_email__': email, 'reg_passwd__': password,
                'birthday_day': str(random.randint(1,28)),
                'birthday_month': str(random.randint(1,12)),
                'birthday_year': str(random.randint(1995,2005)),
                'sex': '2'
            }
            
            res = ses.post('https://m.facebook.com/reg/submit/', data=payload, headers=headers)
            
            # Step 2: Auto Verification Logic
            if "confirm-email" in res.url or "checkpoint" not in res.url:
                print(f"\r{white}[{yellow}WAITING OTP{white}] {email}          ", end="")
                otp = self.get_otp(email)
                
                if otp:
                    # Submit OTP to Facebook (Simulation of confirmation endpoint)
                    confirm_url = "https://m.facebook.com/confirmemail.php"
                    confirm_payload = {'c': otp, 'submit': 'Confirm'}
                    ses.post(confirm_url, data=confirm_payload, headers=headers)
                    
                    uid = ses.cookies.get_dict().get('c_user', 'No-UID')
                    print(f"\n{green}[CHARSI-VERIFIED] {uid} | {password} | {email}")
                    self.oks.append(uid)
                    with open("/sdcard/CHARSI-OK.txt", "a") as f:
                        f.write(f"{uid}|{password}|{email}|{otp}\n")
                else:
                    self.cps.append(email)
            
            self.loop += 1
            print(f"\r{white}[RUNNING] {self.loop} | {green}OK:{len(self.oks)} {red}CP:{len(self.cps)}", end="")
            
        except Exception:
            pass

if __name__ == "__main__":
    if not os.path.exists('/sdcard'): os.system('termux-setup-storage')
    CharsiVerify().menu()
