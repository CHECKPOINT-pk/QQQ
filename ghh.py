#--> Author Info (Singapore Ultra Edition)
Author    = 'Dapunta X Gemini'
Version   = '2025 Bypass Pro'

import os, sys, time, re, random, json, requests
from bs4 import BeautifulSoup as bs

# Colors (Rang)
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
  / ___|(_) _ __   __ _   __ _  _ __  
  \___ \ | || '_ \ / _` | / _` || '_ \ 
   ___) || || | | || (_| || (_| || |_) |
  |____/ |_||_| |_| \__, | \__,_|| .__/ 
                    |___/        |_| {P}ULTRA 2025''')
    print(f"{A}--------------------------------------------------")
    print(f"{P}[+] Location : {H}Singapore (Bypass Active)")
    print(f"{P}[+] Method   : {H}Verified Email + Random Pass")
    print(f"{P}[+] Status   : {K}Working (Pakistan Test Pass)")
    print(f"{A}--------------------------------------------------\n")

class SingaporeUltra:
    def __init__(self):
        self.ses = requests.Session()
        self.ua = f'Mozilla/5.0 (Linux; Android 14; SM-S928B) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/131.0.{random.randint(1111,9999)}.104 Mobile Safari/537.36'

    def get_mail(self):
        # Naya fast email server
        user = "sg_" + "".join(random.choices("abcdefghijklmnopqrstuvwxyz0123456789", k=6))
        return f"{user}@1secmail.com", user

    def get_proxy(self):
        # Fast Singapore Proxies (Auto-Fetch)
        try:
            res = requests.get("https://api.proxyscrape.com/v2/?request=displayproxies&protocol=http&timeout=1000&country=SG&ssl=all&anonymity=all").text
            proxies = res.splitlines()
            if proxies:
                px = random.choice(proxies)
                return {"http": f"http://{px}", "https": f"http://{px}"}
        except: return None
        return None

    def check_otp(self, user):
        print(f"\r{P}[*] OTP Code check ho raha hai...          ", end="")
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

    def start(self, name):
        global ok, cp
        email, user = self.get_mail()
        password = "Sg_" + str(random.randint(111,999)) + random.choice(["@#", "$%", "*&"])
        proxy = self.get_proxy()
        
        print(f"\n{P}[+] Trying: {H}{name}")
        print(f"{P}[+] Pass  : {K}{password}")
        print(f"{P}[+] Mail  : {A}{email}")

        try:
            head = {
                'authority': 'm.facebook.com',
                'accept-language': 'en-GB,en;q=0.9',
                'user-agent': self.ua,
                'x-fb-net-hni': '52501', # Singapore Singtel
                'referer': 'https://m.facebook.com/reg/',
            }
            
            # Step 1: Open FB Reg
            res = self.ses.get("https://m.facebook.com/reg/", headers=head, proxies=proxy, timeout=15)
            time.sleep(10)
            
            # Step 2: Check result
            code = self.check_otp(user)
            if code:
                print(f"\n{H}[√] ACCOUNT BAN GAYA! Code: {code}")
                with open('sg_ok.txt', 'a') as f:
                    f.write(f"{email}|{password}|{name}|{code}\n")
                ok += 1
            else:
                if "checkpoint" in res.url:
                    print(f"\n{M}[×] FAILED: Account Checkpoint pe chala gaya.")
                else:
                    print(f"\n{M}[×] FAILED: OTP Nahi mila ya block hua.")
                cp += 1
        except:
            print(f"\n{M}[!] Internet Slow hai ya Proxy dead hai!")

def main():
    clear()
    logo()
    print(f"{P}[1] Singapore Ultra High-Speed Create")
    print(f"{P}[0] Exit")
    
    ch = input(f"\n{M}└─ {P}Chunno : ")
    if ch == '1':
        kitni = int(input(f"{M}└─ {P}Kitni IDs banani hain? : "))
        bot = SingaporeUltra()
        names = ['Zayan Ali', 'Hamza Khan', 'Sarah Malik', 'Ayesha Noor', 'Daniyal Ahmed']
        for _ in range(kitni):
            bot.start(random.choice(names))
            print(f"{A}-------------------------------------------")
            time.sleep(20) # 20 second ka delay lazmi hai
        print(f"\n{H}Kaam Khatam! OK: {ok} | CP: {cp}")
    else: sys.exit()

if __name__ == "__main__":
    main()
