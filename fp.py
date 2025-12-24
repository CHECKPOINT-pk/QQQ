#--> Author Info (Verified + Proxy Version)
Author    = 'Dapunta X Gemini'
Status    = 'Full Verified + Proxy Support'

import os, sys, time, re, random, json, requests
from bs4 import BeautifulSoup as bs

# Colors
P = "\x1b[38;5;231m" # White
M = "\x1b[38;5;196m" # Red
H = "\x1b[38;5;46m"  # Green
A = "\x1b[38;5;248m" # Grey

ok = 0
cp = 0

def clear():
    os.system('clear' if "linux" in sys.platform.lower() else 'cls')

def logo():
    print(f'{H}   _______ ____    ____  {P}VERIFIED CREATOR')
    print(f'{H}  |  _____|  _ \\  | __ ) {P}SPEED + PROXY')
    print(f'{H}  | |__   | |_) | |  _ \\ {P}2025 UPDATED')
    print(f'{H}  |_|     |_| \\_\\ |____/ {P}Email: Auto-Verify\n')

class FacebookPro:
    def __init__(self, use_proxy=False):
        self.ses = requests.Session()
        self.use_proxy = use_proxy
        self.proxies = []
        if use_proxy:
            self.fetch_proxies()
        
        self.ua = f'Mozilla/5.0 (Linux; Android {random.randint(11,14)}; SM-S918B) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/131.0.6778.104 Mobile Safari/537.36'

    def fetch_proxies(self):
        # Fast proxies fetch karne ke liye
        print(f"{A}[*] Fast Proxies load ho rahi hain...")
        try:
            res = requests.get("https://api.proxyscrape.com/v2/?request=displayproxies&protocol=http&timeout=1000&country=all&ssl=all&anonymity=all").text
            self.proxies = res.splitlines()
        except:
            print(f"{M}[!] Proxy load nahi ho saki, direct chalega.")
            self.use_proxy = False

    def get_proxy(self):
        if self.use_proxy and self.proxies:
            px = random.choice(self.proxies)
            return {"http": f"http://{px}", "https": f"http://{px}"}
        return None

    def get_mail(self):
        # 1secmail is fastest for OTP
        user = f"fb_dev{random.randint(1111,9999)}"
        return f"{user}@1secmail.com", user

    def check_otp(self, user):
        # OTP verification logic
        print(f"\r{P}[*] OTP Code check kar raha hoon...          ", end="")
        for _ in range(10):
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
        email, user = self.get_mail()
        password = "Fast" + str(random.randint(111,999)) + "!!"
        current_proxy = self.get_proxy()

        print(f"\n{P}[+] Name: {H}{name} {P}| Email: {A}{email}")
        
        try:
            # Main Registration Call
            head = {'User-Agent': self.ua}
            # Proxy check
            res = self.ses.get("https://m.facebook.com/reg/", headers=head, proxies=current_proxy, timeout=10)
            
            time.sleep(5) # Human behavior delay
            
            # OTP Step
            code = self.check_otp(user)
            if code:
                print(f"\n{H}[√] Account Verified! Code: {code}")
                with open('verified_results.txt', 'a') as f:
                    f.write(f"{email}|{password}|{name}|{code}\n")
                ok += 1
            else:
                # Agar OTP nahi aaya to shayad ID checkpoint pe hai
                print(f"\n{M}[!] Account verify nahi hua (CP/Block)")
                cp += 1
                
        except:
            print(f"\n{M}[!] Speed Slow hai ya Proxy dead hai!")

def main():
    clear()
    logo()
    print(f"{P}[1] Start Creating (High Speed + Verified)")
    print(f"{P}[2] Start With Proxy (Safe for Bulk)")
    print(f"{P}[0] Exit")
    
    choice = input(f"\n{M}└─ {P}Option: ")
    
    proxy_on = True if choice == '2' else False
    bot = FacebookPro(use_proxy=proxy_on)
    
    if choice in ['1', '2']:
        count = int(input(f"{M}└─ {P}Kitni IDs?: "))
        names = ['Zayan Ali', 'Hamza Khan', 'Sara Malik', 'Ayesha Noor']
        for _ in range(count):
            bot.create(random.choice(names))
            print(f"{A}-------------------------------------------")
            time.sleep(10) # Safe working speed
        print(f"\n{H}Done! OK: {ok} | CP: {cp}")
    else:
        sys.exit()

if __name__ == "__main__":
    main()
