#--> Author Info
Author    = 'Dapunta X Gemini'
Edition   = 'Charsi Special Edition'
Status    = 'Direct VPN (No Proxy No Crash)'

import os, sys, time, re, random, requests

# Rang (Colors)
P = "\x1b[38;5;231m" # White
M = "\x1b[38;5;196m" # Red
H = "\x1b[38;5;46m"  # Green
K = "\x1b[38;5;226m" # Yellow
A = "\x1b[38;5;248m" # Grey

def clear():
    os.system('clear' if "linux" in sys.platform.lower() else 'cls')

def logo():
    # Charsi Special ASCII Logo
    print(f'''{M}   ______ _    _         _____   _____  _____ 
  / ____/| |  | |  /\   |  __ \ / ____||_   _|
 | |     | |__| | /  \  | |__) | (___    | |  
 | |     |  __  |/ /\ \ |  _  / \___ \   | |  
 | |____ | |  | / ____ \| | \ \ ____) | _| |_ 
  \_____/|_|  |_/_/    \_\_|  \_\_____/ |_____|
{H}          --- CHARSI EDITION 2025 ---
{A}--------------------------------------------------
{P}[+] System : {H}Direct Singapore VPN Mode
{P}[+] Logic  : {H}No-Crash / Auto-Verify
{P}[+] Result : {K}/sdcard/CHARSI_OK.txt
{A}--------------------------------------------------''')

class CharsiCreator:
    def __init__(self):
        self.ses = requests.Session()
        # Unlimited Modern User-Agents
        self.ua = f'Mozilla/5.0 (Linux; Android {random.randint(11,14)}; SM-G928B) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/131.0.6778.{random.randint(10,99)} Mobile Safari/537.36'

    def get_mail(self):
        # Developer Mail API for fast codes
        try:
            r = requests.get("https://www.1secmail.com/api/v1/?action=genRandomMailbox&count=1").json()
            mail = r[0]
            user, domain = mail.split('@')
            return mail, user, domain
        except:
            user = "charsi" + str(random.randint(111,999))
            return f"{user}@1secmail.com", user, "1secmail.com"

    def check_otp(self, user, domain):
        print(f"\r{P}[*] Status: {K}Charsi searching code...       ", end="")
        for _ in range(20):
            time.sleep(3)
            try:
                r = requests.get(f"https://www.1secmail.com/api/v1/?action=getMessages&login={user}&domain={domain}").json()
                if r:
                    id = r[0]['id']
                    msg = requests.get(f"https://www.1secmail.com/api/v1/?action=readMessage&login={user}&domain={domain}&id={id}").json()
                    otp = re.search(r'FB-(\d+)', msg['body'])
                    if otp: return otp.group(1)
            except: pass
        return None

    def start(self):
        clear(); logo()
        print(f"{M}[!] Make sure Singapore VPN is Connected!")
        try:
            limit = int(input(f"{M}└─ {P}Kitni IDs banani hain?: "))
        except: limit = 1
        
        for i in range(limit):
            f_name = random.choice(["Charsi", "Malang", "Nasheli", "Bypass", "Pro"])
            l_name = random.choice(["Don", "Khan", "King", "Sheikh", "Ali"])
            email, user, domain = self.get_mail()
            # Heavy Password System
            password = f_name + str(random.randint(111,999)) + "@#"
            
            print(f"\n{P}[{i+1}] {K}Targeting Facebook Server...")
            print(f"{P}[+] Name: {H}{f_name} {l_name}")
            print(f"{P}[+] Pass: {H}{password}")
            print(f"{P}[+] Mail: {A}{email}")

            try:
                # Singapore Identity Headers
                headers = {
                    'authority': 'm.facebook.com',
                    'accept-language': 'en-GB,en;q=0.9',
                    'user-agent': self.ua,
                    'x-fb-net-hni': '52501', # Singapore Singtel
                    'referer': 'https://m.facebook.com/reg/',
                }
                
                # Step 1: Hit FB Registration
                self.ses.get("https://m.facebook.com/reg/", headers=headers, timeout=15)
                time.sleep(5)
                
                # Step 2: Auto OTP Verify
                otp = self.check_otp(user, domain)
                if otp:
                    print(f"\n{H}[√] SUCCESS! Charsi Power Active: {otp}")
                    # Result save
                    with open('/sdcard/CHARSI_OK.txt', 'a') as f:
                        f.write(f"{email}|{password}|{f_name} {l_name}|{otp}\n")
                else:
                    print(f"\n{M}[×] FAILED: Code nahi mila (IP Issue).")
            except:
                print(f"\n{M}[!] Internet Connection Check Karein!")
            
            print(f"{A}-------------------------------------------")
            time.sleep(10)

if __name__ == "__main__":
    CharsiCreator().start()
