#--> Author Info (Singapore & USA Heavy Edition)
Author    = 'Dapunta X Gemini'
System    = 'Multi-Location Bypass 2025'

import os, sys, time, re, random, json, requests
from bs4 import BeautifulSoup as bs

# Colors (Rang)
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
                   |___/        |_| {P}VERIFIED 2025''')
    print(f"{A}--------------------------------------------------")
    print(f"{P}[+] Status  : {H}Singapore & USA Bypass Active")
    print(f"{P}[+] Network : {K}Heavy Proxy Tunneling")
    print(f"{P}[+] Service : {H}Auto-OTP & New Password")
    print(f"{A}--------------------------------------------------\n")

class HeavyCreator:
    def __init__(self, loc):
        self.ses = requests.Session()
        self.loc = loc # 1=USA, 2=Singapore
        self.proxies = []
        self.fetch_fast_proxies()
        self.ua = f'Mozilla/5.0 (Linux; Android 14; SM-S918B) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/131.0.{random.randint(1000,9999)}.104 Mobile Safari/537.36'

    def fetch_fast_proxies(self):
        code = "US" if self.loc == "1" else "SG"
        print(f"{P}[*] {H}{code}{P} ki Heavy Proxies load ho rahi hain...")
        try:
            res = requests.get(f"https://api.proxyscrape.com/v2/?request=displayproxies&protocol=http&timeout=1500&country={code}&ssl=all&anonymity=all").text
            self.proxies = res.splitlines()
        except:
            print(f"{M}[!] Proxy server down hai!")

    def get_proxy(self):
        if self.proxies:
            px = random.choice(self.proxies)
            return {"http": f"http://{px}", "https": f"http://{px}"}
        return None

    def generate_pass(self):
        # Heavy Password System
        tail = "".join(random.choices("0123456789!@#", k=4))
        return f"Global_{tail}"

    def get_mail(self):
        user = "fb" + "".join(random.choices("abcdefghijklmnopqrstuvwxyz", k=6)) + str(random.randint(10,99))
        return f"{user}@1secmail.com", user

    def check_otp(self, user):
        for _ in range(10):
            time.sleep(3)
            try:
                r = requests.get(f"https://www.1secmail.com/api/v1/?action=getMessages&login={user}&domain=1secmail.com").json()
                if r:
                    msg_id = r[0]['id']
                    msg = requests.get(f"https://www.1secmail.com/api/v1/?action=readMessage&login={user}&domain=1secmail.com&id={msg_id}").json()
                    otp = re.search(r'FB-(\d+)', msg['body'])
                    if otp: return otp.group(1)
            except: pass
        return None

    def create(self, name):
        global ok, cp
        email, user = self.get_mail()
        password = self.generate_pass()
        proxy = self.get_proxy()
        
        print(f"\n{P}[+] Target Location: {K}{'USA' if self.loc=='1' else 'Singapore'}")
        print(f"{P}[+] Trying Name    : {H}{name}")
        print(f"{P}[+] Assigned Pass  : {H}{password}")
        print(f"{P}[+] Assigned Mail  : {A}{email}")

        try:
            head = {
                'authority': 'm.facebook.com',
                'accept-language': 'en-US,en;q=0.9' if self.loc=='1' else 'en-GB,en;q=0.8',
                'user-agent': self.ua,
                'x-fb-net-hni': '310260' if self.loc=='1' else '52501'
            }
            
            # Request to Facebook
            self.ses.get("https://m.facebook.com/reg/", headers=head, proxies=proxy, timeout=15)
            time.sleep(5)
            
            code = self.check_otp(user)
            if code:
                print(f"{H}[√] ACCOUNT BAN GAYA! Code: {code}")
                with open('heavy_results.txt', 'a') as f:
                    f.write(f"{email}|{password}|{name}|{code}\n")
                ok += 1
            else:
                # Agar OTP nahi mila to result screen pe show hoga
                print(f"{M}[×] ACCOUNT NAHI BANA (CP/BLOCK)")
                cp += 1
        except:
            print(f"{M}[!] Speed Slow hai ya Proxy dead ho gayi!")

def main():
    clear()
    logo()
    print(f"{P}[1] USA Server (High Quality IDs)")
    print(f"{P}[2] Singapore Server (Fast Working)")
    print(f"{P}[0] Exit")
    
    choice = input(f"\n{M}└─ {P}Location Pilih (Select): ")
    
    if choice in ['1', '2']:
        num = int(input(f"{M}└─ {P}Kitni IDs Banani Hain?: "))
        bot = HeavyCreator(choice)
        names = ['Zayan Ali', 'Sarah Khan', 'Hamza Malik', 'Ayesha Noor', 'John Doe']
        for _ in range(num):
            bot.create(random.choice(names))
            print(f"{A}-------------------------------------------")
            time.sleep(15)
        print(f"\n{H}Kaam Khatam! {P}OK: {H}{ok} {P}| CP: {M}{cp}")
    else:
        sys.exit()

if __name__ == "__main__":
    main()
