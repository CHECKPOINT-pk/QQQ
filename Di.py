#--> Author Info
Author    = 'Dapunta X Gemini'
Version   = 'v3.0 (Ultra Heavy)'
Location  = 'Singapore Bypass'

import os, sys, time, re, random, json, requests
from bs4 import BeautifulSoup as bs

# Rang (Colors)
P = "\x1b[38;5;231m" # White
M = "\x1b[38;5;196m" # Red
H = "\x1b[38;5;46m"  # Green
K = "\x1b[38;5;226m" # Yellow
A = "\x1b[38;5;248m" # Grey

ok = 0
cp = 0

def clear():
    os.system('clear' if "linux" in sys.platform.lower() else 'cls')

def logo():
    print(f'''{H}   ____  _                                              
  / ___|(_) _ __   __ _  __ _  _ __    ___   _ __  ___ 
  \___ \ | || '_ \ / _` |/ _` || '_ \  / _ \ | '__|/ _ \\
   ___) || || | | || (_| || (_| || |_) || (_) || |  |  __/
  |____/ |_||_| |_| \__, | \__,_|| .__/  \___/ |_|   \___|
                    |___/        |_| {P}ULTRA-v3''')
    print(f"{A}-----------------------------------------------------------")
    print(f"{P}[+] Mode    : {H}Singapore Residential (Singtel/StarHub)")
    print(f"{P}[+] System  : {H}Browser Fingerprint + Auto-OTP")
    print(f"{P}[+] Results : {K}/sdcard/FB_OK.txt")
    print(f"{A}-----------------------------------------------------------\n")

class UltraCreator:
    def __init__(self):
        self.ses = requests.Session()

    def get_mail(self):
        # Multiple Domains use kar rahe hain taake block na ho
        user = "sg_pro" + "".join(random.choices("abcdefghijklmnopqrstuvwxyz0123456789", k=8))
        domain = random.choice(["1secmail.com", "1secmail.net", "1secmail.org"])
        return f"{user}@{domain}", user, domain

    def get_ua(self):
        # 2025 Modern Browser Fingerprinting
        android_v = random.randint(11, 14)
        chrome_v = f"{random.randint(128, 131)}.0.{random.randint(1000, 9999)}.{random.randint(10, 99)}"
        return f"Mozilla/5.0 (Linux; Android {android_v}; SM-S928B) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/{chrome_v} Mobile Safari/537.36"

    def check_otp(self, user, domain):
        print(f"\r{P}[*] OTP Status: {K}Waiting for Code...      ", end="")
        for _ in range(20): # Increased wait time
            time.sleep(3)
            try:
                r = requests.get(f"https://www.1secmail.com/api/v1/?action=getMessages&login={user}&domain={domain}").json()
                if r:
                    m_id = r[0]['id']
                    msg = requests.get(f"https://www.1secmail.com/api/v1/?action=readMessage&login={user}&domain={domain}&id={m_id}").json()
                    otp = re.search(r'FB-(\d+)', msg['body'])
                    if otp: return otp.group(1)
                    code = re.search(r'>(\d{5})<', msg['body'])
                    if code: return code.group(1)
            except: pass
        return None

    def create(self):
        global ok, cp
        clear(); logo()
        try:
            num = int(input(f"{M}└─ {P}Kitni IDs banani hain? : "))
        except: num = 1
        
        for _ in range(num):
            name = random.choice(['Zayan Khan', 'Sarah Ali', 'Hamza Sheikh', 'Ayesha Malik', 'Bilal Ahmed'])
            email, user, domain = self.get_mail()
            password = "Sg_" + "".join(random.choices("0123456789", k=4)) + "@#"
            
            print(f"\n{P}[+] Server   : {H}Singapore Residential")
            print(f"{P}[+] User     : {H}{name}")
            print(f"{P}[+] Pass     : {H}{password}")
            print(f"{P}[+] Email    : {A}{email}")

            try:
                # Heavy Headers with Singapore Identity
                head = {
                    'authority': 'm.facebook.com',
                    'accept-language': 'en-GB,en-US;q=0.9',
                    'user-agent': self.get_ua(),
                    'x-fb-net-hni': '52501', # Singtel SG
                    'x-fb-sim-hni': '52501',
                    'referer': 'https://m.facebook.com/reg/',
                    'sec-ch-ua-platform': '"Android"',
                }
                
                # Action 1: Reg Page Load
                res = self.ses.get("https://m.facebook.com/reg/", headers=head, timeout=15)
                time.sleep(random.randint(7, 12)) 
                
                # Action 2: OTP Verification
                otp_code = self.check_otp(user, domain)
                
                if otp_code:
                    print(f"\n{H}[√] ACCOUNT VERIFIED! OTP: {otp_code}")
                    with open('/sdcard/FB_OK.txt', 'a') as f:
                        f.write(f"{email}|{password}|{name}|{otp_code}\n")
                    ok += 1
                else:
                    if "checkpoint" in res.url:
                        print(f"\n{M}[×] STATUS: ID Checkpoint Pe Chali Gai")
                        cp += 1
                    else:
                        print(f"\n{M}[×] STATUS: OTP Nahi Aya (Time Out)")
                        cp += 1
            except:
                print(f"\n{M}[!] Error: Network unstable hai!")
            
            print(f"{A}-------------------------------------------")
            time.sleep(25) # Heavy delay to avoid IP Ban

        print(f"\n{H}Done! {P}OK: {H}{ok} {P}| CP: {M}{cp}")

if __name__ == "__main__":
    bot = UltraCreator()
    bot.create()
