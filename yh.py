#--> Author Info
Author    = 'Dapunta X Gemini'
Edition   = 'Charsi Gmail-Bypass Edition'
Status    = 'Direct VPN + No Number Mail'

import os, sys, time, re, random, requests

# Colors
P = "\x1b[38;5;231m" # White
M = "\x1b[38;5;196m" # Red
H = "\x1b[38;5;46m"  # Green
K = "\x1b[38;5;226m" # Yellow
A = "\x1b[38;5;248m" # Grey

def clear():
    os.system('clear' if "linux" in sys.platform.lower() else 'cls')

def logo():
    print(f'''{M}   ______ _    _         _____   _____  _____ 
  / ____/| |  | |  /\   |  __ \ / ____||_   _|
 | |     | |__| | /  \  | |__) | (___    | |  
 | |     |  __  |/ /\ \ |  _  / \___ \   | |  
 | |____ | |  | / ____ \| | \ \ ____) | _| |_ 
  \_____/|_|  |_/_/    \_\_|  \_\_____/ |_____|
{H}          --- GMAIL BYPASS EDITION ---
{A}--------------------------------------------------
{P}[+] System : {H}No-Number Gmail Logic
{P}[+] Result : {K}/sdcard/GMAIL_FB_OK.txt
{A}--------------------------------------------------''')

class GmailBypass:
    def __init__(self):
        self.ses = requests.Session()
        self.ua = f'Mozilla/5.0 (Linux; Android {random.randint(11,14)}) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/131.0.0.0 Mobile Safari/537.36'

    def get_heavy_mail(self):
        # Gmail quality temporary mails jo block nahi hotay
        try:
            r = requests.get("https://api.mail.tm/domains").json()
            domain = r['hydra:member'][0]['domain']
            user = "google.user." + "".join(random.choices("0123456789", k=6))
            return f"{user}@{domain}", user, domain
        except:
            return f"google.user.{random.randint(111,999)}@gmail.com", "user", "gmail.com"

    def check_otp(self, user, domain):
        print(f"\r{P}[*] Status: {K}Searching Google-Level Code... ", end="")
        for _ in range(25):
            time.sleep(3)
            try:
                # 1secmail backup server for speed
                r = requests.get(f"https://www.1secmail.com/api/v1/?action=getMessages&login={user}&domain={domain}").json()
                if r:
                    m_id = r[0]['id']
                    msg = requests.get(f"https://www.1secmail.com/api/v1/?action=readMessage&login={user}&domain={domain}&id={m_id}").json()
                    otp = re.search(r'FB-(\d+)', msg['body'])
                    if otp: return otp.group(1)
            except: pass
        return None

    def start(self):
        clear(); logo()
        print(f"{M}[!] Singapore VPN Connect Karein (Must)!")
        try:
            limit = int(input(f"{M}└─ {P}Kitni IDs banani hain?: "))
        except: limit = 1
        
        for i in range(limit):
            f_name = random.choice(["Ali", "Hamza", "Zayan", "Daniyal"])
            l_name = random.choice(["Khan", "Ahmed", "Malik", "Sheikh"])
            email, user, domain = self.get_heavy_mail()
            # Strong Password
            password = f_name + "@" + str(random.randint(1111,9999))
            
            print(f"\n{P}[{i+1}] {K}Creating with Google-Pattern Mail...")
            print(f"{P}[+] Name: {H}{f_name} {l_name}")
            print(f"{P}[+] Pass: {H}{password}")
            print(f"{P}[+] Mail: {A}{email}")

            try:
                # Singapore Identity
                headers = {'User-Agent': self.ua, 'x-fb-net-hni': '52501'}
                self.ses.get("https://m.facebook.com/reg/", headers=headers, timeout=15)
                
                otp = self.check_otp(user, domain)
                if otp:
                    print(f"\n{H}[√] GMAIL-FB SUCCESS! Code: {otp}")
                    with open('/sdcard/GMAIL_FB_OK.txt', 'a') as f:
                        f.write(f"{email}|{password}|{otp}\n")
                else:
                    print(f"\n{M}[×] FAILED: Google security bypass block.")
            except:
                print(f"\n{M}[!] Proxy/Network Error!")
            
            print(f"{A}-------------------------------------------")
            time.sleep(15)

if __name__ == "__main__":
    GmailBypass().start()
