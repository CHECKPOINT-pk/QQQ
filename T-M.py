# HIGH PERFORMANCE FB CREATOR (CYBER-GOLD BIRTHDAY EDITION)
# AUTHOR : CHARSI BRAND
# FEATURES: 10 MAIL SERVERS + RANDOM BIRTHDAY + SD-SAVER

import os, sys, re, time, random, uuid, subprocess, string
from concurrent.futures import ThreadPoolExecutor as ThreadPool

def setup():
    if not os.path.exists('/sdcard'):
        print("\033[1;33m[!] Granting Storage Permission...")
        os.system('termux-setup-storage')
        time.sleep(2)
    
    modules = ['requests', 'bs4', 'faker']
    for mod in modules:
        try:
            __import__(mod)
        except ImportError:
            subprocess.check_call([sys.executable, "-m", "pip", "install", mod])

setup()

import requests
from bs4 import BeautifulSoup
from faker import Faker

# UI Colors
cyan, gold, white, red, grey = "\033[1;36m", "\033[1;33m", "\033[1;37m", "\033[1;31m", "\033[1;90m"
reset = "\033[0m"

class CharsiGold:
    def __init__(self):
        self.oks, self.cps, self.loop = [], [], 0
        self.fk = Faker()
        self.ok_path = "/sdcard/CHARSI_OK.txt"
        self.mail_domains = [
            "vintomaper.com", "mentonit.com", "nowdigitalevents.com",
            "prowebmasters.net", "the-best-mail.com", "security-mail.org",
            "freemail-hosting.com", "business-temp.com", "cloud-mail.pro",
            "digital-inbox.net"
        ]

    def save_account(self, data):
        with open(self.ok_path, "a") as f:
            f.write(data + "\n")

    def create_account(self):
        # 2026 Latest UA
        ua = f"Mozilla/5.0 (Linux; Android {random.randint(11,15)}; SM-S928B) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/{random.randint(125,135)}.0.0.0 Mobile Safari/537.36"
        first, last = self.fk.first_name(), self.fk.last_name()
        email = f"{''.join(random.choices(string.ascii_lowercase, k=7))}@{random.choice(self.mail_domains)}"
        pwd = first + str(random.randint(11,99)) + "!"
        
        # Random Birthday Generation
        b_day = str(random.randint(1, 28))
        b_month = str(random.randint(1, 12))
        b_year = str(random.randint(1992, 2004))
        full_birthday = f"{b_day}-{b_month}-{b_year}"

        session = requests.Session()
        try:
            headers = {
                'authority': 'm.facebook.com',
                'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,*/*;q=0.8',
                'accept-language': 'en-US,en;q=0.9',
                'user-agent': ua
            }
            
            # Registration Page
            res = session.get('https://m.facebook.com/reg/', headers=headers)
            soup = BeautifulSoup(res.text, 'html.parser')
            data = {i.get('name'): i.get('value') for i in soup.find_all('input') if i.get('name')}
            
            time.sleep(random.uniform(2, 5))
            
            data.update({
                'firstname': first,
                'lastname': last,
                'reg_email__': email,
                'reg_passwd__': pwd,
                'birthday_day': b_day,
                'birthday_month': b_month,
                'birthday_year': b_year,
                'sex': str(random.randint(1, 2))
            })

            # Submit Form
            post = session.post('https://m.facebook.com/reg/submit/', data=data, headers=headers)
            
            if "c_user" in session.cookies.get_dict():
                uid = session.cookies.get_dict()['c_user']
                # Saving with Birthday Info
                account_info = f"{uid} | {pwd} | {email} | DOB: {full_birthday}"
                print(f"\n{cyan}[OK] {account_info}")
                self.oks.append(uid)
                self.save_account(account_info)
            else:
                self.cps.append(email)
                
        except: pass
        self.loop += 1
        print(f"\r{cyan}[RUNNING] {self.loop} | OK:{len(self.oks)} CP:{len(self.cps)}", end="")

    def menu(self):
        os.system('clear')
        print(f"{gold}CHARSI BRAND BIRTHDAY-INFO EDITION 2026")
        print(f"{grey}File Path: {white}/sdcard/CHARSI_OK.txt")
        print(f"━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━")
        print(f"{cyan}[1] Start Creation (With Random DOB)")
        print(f"{red}[0] Exit")
        choice = input(f"\n{cyan}SELECT: {reset}")
        if choice == '1':
            limit = int(input(f"{cyan}LIMIT: {reset}"))
            with ThreadPool(max_workers=30) as pool:
                for _ in range(limit):
                    pool.submit(self.create_account)
        else: exit()

if __name__ == "__main__":
    CharsiGold().menu()
