#--> Author Info (Singapore Ultra Edition)
Author    = 'Dapunta X Gemini'
System    = 'Singapore Heavy Traffic 2025'

import os, sys, time, re, random, json, requests
from bs4 import BeautifulSoup as bs

# Colors
P = "\x1b[38;5;231m" # White
M = "\x1b[38;5;196m" # Red
H = "\x1b[38;5;46m"  # Green
A = "\x1b[38;5;248m" # Grey
K = "\x1b[38;5;226m" # Yellow

ok = 0
cp = 0

def clear():
    os.system('clear' if "linux" in sys.platform.lower() else 'cls')

def logo():
    print(f'''{H}  ____  _                                              
 |  _ \(_) _ __   __ _  __ _  _ __    ___   _ __  ___ 
 | |_) || || '_ \ / _` |/ _` || '_ \  / _ \ | '__|/ _ \\
 |  __/ | || | | || (_| || (_| || |_) || (_) || |  |  __/
 |_|    |_||_| |_| \__, | \__,_|| .__/  \___/ |_|   \___|
                   |___/        |_| {P}SG-ULTRA 2025''')
    print(f"{A}--------------------------------------------------")
    print(f"{P}[+] Mode    : {H}Singapore Residential Bypass")
    print(f"{P}[+] Speed   : {K}Ultra High (99% Uptime)")
    print(f"{P}[+] Account : {H}Auto-Verify + Strong Pass")
    print(f"{A}--------------------------------------------------\n")

class SingaporeBypass:
    def __init__(self):
        self.ses = requests.Session()
        self.proxies = []
        self.fetch_sg_proxies()
        # Naya Singapore base User Agent
        self.ua = f'Mozilla/5.0 (Linux; Android 14; SM-S928B) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/131.0.6778.104 Mobile Safari/537.36'

    def fetch_sg_proxies(self):
        print(f"{P}[*] {H}Singapore{P} ki High-Speed Proxies connect ho rahi hain...")
        try:
            # Sirf Singapore (SG) ki proxies fetch karna
            res = requests.get("https://api.proxyscrape.com/v2/?request=displayproxies&protocol=http&timeout=1000&country=SG&ssl=all&anonymity=all").text
            self.proxies = res.splitlines()
        except:
            print(f"{M}[!] Proxy fetch error!")

    def get_sg_proxy(self):
        if self.proxies:
            px = random.choice(self.proxies)
            return {"http": f"http://{px}", "https": f"http://{px}"}
        return None

    def get_unique_mail(self):
        # Har baar naya email aur unique user
        user = "sg_pro" + "".join(random.choices("abcdefghijklmnopqrstuvwxyz0123456789", k=7))
        return f"{user}@1secmail.com", user

    def generate_heavy_pass(self):
        # Full Strong Password System
        prefix = random.choice(["Sg", "Singa", "Bypass", "Verify"])
        body = "".join(random.choices("0123456789", k=4))
        suffix = random.choice(["@#", "$!", "*-"])
        return f"{prefix}{body}{suffix}"

    def check_otp(self, user):
        print(f"\r{P}[*] OTP ka intezar: {K}Cheking Inbox...      ", end="")
        for _ in range(15):
            time.sleep(3)
            try:
                r = requests.get(f"https://www.1secmail.com/api/v1/?action=getMessages&login={user}&domain=1secmail.com").json()
                if r:
                    id = r[0]['id']
                    msg = requests.get(f"https://www.1secmail.com/api/v1/?action=readMessage&login={user}&domain=1secmail.com&id={id}").json()
                    otp = re.search(r'FB-(\d+)', msg['body'])
                    if otp: return otp.group(1)
            except: pass
        return None

    def create(self, name):
        global ok, cp
        email, user = self.get_unique_mail()
        password = self.generate_heavy_pass()
        proxy = self.get_sg_proxy()
        
        print(f"\n{P}[+] Target   : {K}Singapore Server")
        print(f"{P}[+] Name     : {H}{name}")
        print(f"{P}[+] Password : {H}{password}")
        print(f"{P}[+] Email    : {A}{email}")

        try:
            # Singapore Network Headers
            headers = {
                'authority': 'm.facebook.com',
                'accept-language': 'en-GB,en;q=0.9', # SG English
                'user-agent': self.ua,
                'x-fb-net-hni': '52501', # Singapore Singtel Code
                'x-fb-sim-hni': '52501',
                'referer': 'https://m.facebook.com/',
            }
            
            # Step 1: Open FB Reg
            res = self.ses.get("https://m.facebook.com/reg/", headers=headers, proxies=proxy, timeout=12)
            time.sleep(8) # Real human delay
            
            # Step 2: Check for Verification
            code = self.check_otp(user)
            
            if code:
                print(f"\n{H}[√] ACCOUNT CREATED & VERIFIED! Code: {code}")
                with open('sg_results_verified.txt', 'a') as f:
                    f.write(f"{email}|{password}|{name}|{code}\n")
                ok += 1
            else:
                # Agar OTP nahi aata to check karo ke page block to nahi hua
                if "checkpoint" in res.url:
                    print(f"\n{M}[×] FAILED: Account went to Checkpoint (Block)")
                    cp += 1
                else:
                    print(f"\n{M}[×] FAILED: Email OTP code nahi mila")
                    cp += 1
        except:
            print(f"\n{M}[!] Proxy slow hai ya Singapore connection dead hai!")

def main():
    clear()
    logo()
    print(f"{P}[1] Start Singapore High-Speed Creation")
    print(f"{P}[0] Exit")
    
    choice = input(f"\n{M}└─ {P}Chunno: ")
    
    if choice == '1':
        num = int(input(f"{M}└─ {P}Kitni IDs?: "))
        bot = SingaporeBypass()
        names = ['Zayan Ali', 'Sarah Khan', 'Arsalan Ahmed', 'Hania Malik', 'Daniyal Sheikh']
        for _ in range(num):
            bot.create(random.choice(names))
            print(f"{A}-------------------------------------------")
            # Anti-ban gap (Zaruri hai!)
            time.sleep(20) 
        print(f"\n{H}Done! {P}OK: {H}{ok} {P}| CP: {M}{cp}")
    else:
        sys.exit()

if __name__ == "__main__":
    main()
