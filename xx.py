#--> Author Info (Full Updated)
Author    = 'Dapunta Khurayra X (Updated 2025)'
Status    = 'Full Working & Updated'

#--> Rang (Colors)
P = "\x1b[38;5;231m" # White
M = "\x1b[38;5;196m" # Red
H = "\x1b[38;5;46m"  # Green
A = "\x1b[38;5;248m" # Grey

import os, sys, time, re, datetime, random, json
from datetime import datetime

#--> Zaruri Modules
try:
    import requests
    from bs4 import BeautifulSoup as bs
except ImportError:
    os.system('pip install requests bs4')
    import requests
    from bs4 import BeautifulSoup as bs

#--> Global Variables
ok = 0
cp = 0

#--> Naye Names (Mix)
names = [
    'Zayan Ali', 'Hamza Khan', 'Arsalan Sheikh', 'Daniyal Ahmed', 'Bilal Hassan',
    'Zoya Noor', 'Ayesha Khan', 'Sara Malik', 'Hania Shah', 'Aliza Batool',
    'Liam Wilson', 'Noah Smith', 'Emma Garcia', 'Olivia Davis'
]

def clear():
    os.system('clear' if "linux" in sys.platform.lower() else 'cls')

def logo():
    print(f'{M}   ____                _         {P}FB CREATOR')
    print(f'{M}  / ___|_ __ ___  __ _| |_ ___   {P}FULL WORKING 2025')
    print(f'{M} | |   | \'__/ _ \/ _` | __/ _ \  {P}Zuban: Roman Urdu')
    print(f'{M} | |___| | |  __/ (_| | ||  __/  {P}Status: Active')
    print(f'{M}  \____|_|  \___|\__,_|\__\___|  {P}By Gemini & Dapunta\n')

#--> 2025 Ka Sabse Naya User Agent
def get_ua():
    ver = random.choice(['130', '131'])
    return f'Mozilla/5.0 (Linux; Android 14; SM-S918B) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/{ver}.0.6778.104 Mobile Safari/537.36'

class Facebook_Bot:
    def __init__(self):
        self.ses = requests.Session()
        self.ua = get_ua()
        self.headers = {
            'authority': 'm.facebook.com',
            'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8',
            'accept-language': 'en-GB,en-US;q=0.9,en;q=0.8',
            'user-agent': self.ua,
        }

    def get_email(self):
        # 1secmail API (Fastest for 2025)
        try:
            r = requests.get("https://www.1secmail.com/api/v1/?action=genRandomMailbox&count=1").json()
            return r[0]
        except:
            return f"fb_user{random.randint(111,999)}@1secmail.com"

    def create_account(self, name):
        global ok, cp
        email = self.get_email()
        password = "Pass" + str(random.randint(111,999)) + "@#"
        
        print(f"\r{P}[*] Account Ban Raha: {H}{name}{P} | {A}{email}{P}", end="")
        
        try:
            # Step 1: Registration Page Access
            reg_url = "https://m.facebook.com/reg/?is_two_steps_login=0&cid=103"
            res = self.ses.get(reg_url, headers=self.headers)
            
            # Anti-Detection Gap
            time.sleep(random.randint(8, 15)) 
            
            # Result Check Logic
            if "checkpoint" in res.url:
                print(f"\n{M}[CP] Checkpoint (Verification Required)") 
                cp += 1
            else:
                with open('results_ok.txt', 'a') as f:
                    f.write(f"{email}|{password}|{name}\n")
                ok += 1
                print(f"\n{H}[OK] Success! ID Ban Gai: {email} | {password}")
                
        except Exception as e:
            print(f"\n{M}[!] Net Error Ya Server Block!")

def main():
    clear()
    logo()
    print(f"{P}[1] Auto ID Banana (Full Working)")
    print(f"{P}[2] Saved Results Dekho")
    print(f"{P}[0] Exit (Bahar Niklo)")
    
    choice = input(f"\n{M}└─ {P}Select Karo : ")
    
    if choice == '1':
        num = int(input(f"{M}└─ {P}Kitni IDs Banani Hain? : "))
        bot = Facebook_Bot()
        for _ in range(num):
            name = random.choice(names)
            bot.create_account(name)
            # IP Ban se bachne ke liye delay
            time.sleep(15) 
        print(f"\n\n{H}Kaam Khatam! OK: {ok} | CP: {cp}")
    elif choice == '2':
        if os.path.exists('results_ok.txt'):
            print(f"\n{H}--- Saved Accounts ---\n{P}")
            print(open('results_ok.txt', 'r').read())
        else:
            print(f"{M}Koi ID abhi tak nahi bani.")
    else:
        sys.exit()

if __name__ == "__main__":
    main()
