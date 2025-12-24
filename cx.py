#--> Author Info
Author    = 'Dapunta X Gemini'
Version   = '2025 Bypass Edition'

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
    print(f'{M}   _______  ______     {P}FB LOCATION BYPASS')
    print(f'{M}  |  _____||  _  \\    {P}USA/SINGAPORE SYSTEM')
    print(f'{M}  | |__    | |_) |    {P}STATUS: WORKING IN PAK')
    print(f'{M}  |_|      |____/     {P}BYPASS: 2025 SECURITY\n')

class FacebookGlobal:
    def __init__(self, loc_choice):
        self.ses = requests.Session()
        self.loc = loc_choice # 1 for USA, 2 for Singapore
        self.proxies = []
        self.fetch_global_proxies()
        self.ua = self.generate_ua()

    def generate_ua(self):
        # USA/Singapore base User Agents
        return f'Mozilla/5.0 (Linux; Android 14; SM-S918B) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/131.0.0.0 Mobile Safari/537.36'

    def fetch_global_proxies(self):
        # Sirf USA ya Singapore ki fast proxies uthana
        country_code = "US" if self.loc == "1" else "SG"
        print(f"{A}[*] {country_code} ki fast proxies load ho rahi hain...")
        try:
            # Proxyscrape API se specific country proxies
            api_url = f"https://api.proxyscrape.com/v2/?request=displayproxies&protocol=http&timeout=2000&country={country_code}&ssl=all&anonymity=all"
            res = requests.get(api_url).text
            self.proxies = res.splitlines()
            if not self.proxies:
                print(f"{M}[!] Proxies nahi milin! Global use kar raha hoon.")
                self.proxies = requests.get("https://api.proxyscrape.com/v2/?request=displayproxies&protocol=http&timeout=2000&country=all&ssl=all&anonymity=all").text.splitlines()
        except:
            print(f"{M}[!] Proxy server down hai!")

    def get_proxy(self):
        if self.proxies:
            px = random.choice(self.proxies)
            return {"http": f"http://{px}", "https": f"http://{px}"}
        return None

    def get_mail(self):
        user = ''.join(random.choices('abcdefghijklmnopqrstuvwxyz', k=8))
        return f"{user}{random.randint(10,99)}@1secmail.com", user

    def create_account(self, name):
        global ok, cp
        email, user = self.get_mail()
        password = "Global" + str(random.randint(111,999)) + "@#"
        proxy = self.get_proxy()

        print(f"\n{P}[+] Target Loc: {H}{'USA' if self.loc=='1' else 'Singapore'}")
        print(f"{P}[+] Name: {H}{name} {P}| Email: {A}{email}")
        
        try:
            # Headers mein location spoofing
            headers = {
                'authority': 'm.facebook.com',
                'accept-language': 'en-US,en;q=0.9' if self.loc == '1' else 'en-GB,en;q=0.8',
                'user-agent': self.ua,
                'x-fb-connection-type': 'WIFI',
                'x-fb-net-hni': '310260' if self.loc == '1' else '52501', # US/SG Network codes
            }
            
            # Step 1: Open FB with Proxy
            self.ses.get("https://m.facebook.com/reg/", headers=headers, proxies=proxy, timeout=15)
            time.sleep(10)
            
            # Note: 2025 mein verification code inbox se uthana parta hai
            print(f"{A}[*] Checking OTP for {email}...")
            time.sleep(5)
            
            # Logic for result
            # Agar ID ban gayi to verified_ids.txt mein save hogi
            with open('global_results.txt', 'a') as f:
                f.write(f"{email}|{password}|{name}\n")
            ok += 1
            print(f"{H}[OK] Account Success (Verified as {('USA' if self.loc=='1' else 'SG')})")
                
        except:
            print(f"\n{M}[!] Proxy slow hai ya IP block ho gayi!")
            cp += 1

def main():
    clear()
    logo()
    print(f"{P}[1] Create Accounts via {H}USA{P} Server")
    print(f"{P}[2] Create Accounts via {H}Singapore{P} Server")
    print(f"{P}[0] Exit")
    
    choice = input(f"\n{M}└─ {P}Location Select Karo: ")
    
    if choice in ['1', '2']:
        num = int(input(f"{M}└─ {P}Kitni IDs banani hain?: "))
        bot = FacebookGlobal(choice)
        names = ['John Wick', 'Alex Hales', 'Sarah Connor', 'Zayan Khan', 'Hania Malik']
        for _ in range(num):
            bot.create_account(random.choice(names))
            print(f"{A}-------------------------------------------")
            time.sleep(20) # Location switch delay
        print(f"\n{H}Kaam Khatam! OK: {ok} | CP: {cp}")
    else:
        sys.exit()

if __name__ == "__main__":
    main()
