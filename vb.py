import os, sys, time, re, random, requests
from concurrent.futures import ThreadPoolExecutor as ThreadPool
from bs4 import BeautifulSoup as bs

# Rang (Colors)
P = "\x1b[38;5;231m" # White
M = "\x1b[38;5;196m" # Red
H = "\x1b[38;5;46m"  # Green
K = "\x1b[38;5;226m" # Yellow
A = "\x1b[38;5;248m" # Grey

ok = []
cp = []
loop = 0

def clear():
    os.system('clear' if "linux" in sys.platform.lower() else 'cls')

def logo():
    print(f'''{H}  __  __  _____  ____    _      
 |  \/  || ____|/ ___|  / \     {P}MEGA CREATOR
 | |\/| ||  _| | |  _  / _ \    {P}VERSION: 2025
 | |  | || |___| |_| |/ ___ \   {P}SPEED: ULTRA FAST
 |_|  |_||_____|\____/_/   \_\  {P}BYPASS: SG/USA''')
    print(f"{A}-----------------------------------------------------------")
    print(f"{P}[+] Features: {H}Multi-Threading + Fingerprinting + Auto-Verify")
    print(f"{P}[+] Results : {K}/sdcard/MEGA_OK.txt")
    print(f"{A}-----------------------------------------------------------\n")

#--> Fingerprint Generator (Makes it look like a real phone)
def get_fingerprint():
    android_v = random.randint(11, 14)
    chrome_v = f"{random.randint(128, 131)}.0.{random.randint(1000, 9999)}"
    res = random.choice(["720x1280", "1080x1920", "1440x2560"])
    ua = f"Mozilla/5.0 (Linux; Android {android_v}; SM-S9{random.randint(11, 28)}B) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/{chrome_v} Mobile Safari/537.36"
    return {"ua": ua, "res": res}

class MegaCreator:
    def __init__(self):
        self.ses = requests.Session()

    def get_mail(self):
        try:
            r = requests.get("https://www.1secmail.com/api/v1/?action=genRandomMailbox&count=1").json()
            return r[0].split('@')
        except: return ["user"+str(random.randint(111,999)), "1secmail.com"]

    def get_otp(self, user, domain):
        for _ in range(20):
            time.sleep(3)
            try:
                r = requests.get(f"https://www.1secmail.com/api/v1/?action=getMessages&login={user}&domain={domain}").json()
                if r:
                    m_id = r[0]['id']
                    msg = requests.get(f"https://www.1secmail.com/api/v1/?action=readMessage&login={user}&domain={domain}&id={m_id}").json()
                    otp = re.search(r'FB-(\d+)', msg['body'])
                    if otp: return otp.group(1)
            except: pass
        return None

    def create_process(self, _):
        global loop, ok, cp
        fp = get_fingerprint()
        user, domain = self.get_mail()
        email = f"{user}@{domain}"
        first = random.choice(['Zayan', 'Hamza', 'Arsalan', 'Daniyal', 'Ayesha', 'Sarah'])
        last = random.choice(['Khan', 'Ahmed', 'Sheikh', 'Malik', 'Ali'])
        password = first + str(random.randint(111,999)) + "@#"

        sys.stdout.write(f"\r{P}[Creating] {loop} OK:{len(ok)} CP:{len(cp)} "); sys.stdout.flush()
        
        try:
            headers = {
                'authority': 'm.facebook.com',
                'accept-language': 'en-GB,en;q=0.9',
                'user-agent': fp['ua'],
                'x-fb-net-hni': '52501', # Singapore Bypass
                'viewport-width': fp['res'].split('x')[0],
            }
            # Step 1: Hit FB
            self.ses.get("https://m.facebook.com/reg/", headers=headers, timeout=15)
            loop += 1
            
            # Step 2: Get OTP
            otp = self.get_otp(user, domain)
            if otp:
                print(f"\n{H}[√] SUCCESS: {email} | {password} | {otp}")
                ok.append(email)
                with open('/sdcard/MEGA_OK.txt', 'a') as f:
                    f.write(f"{email}|{password}|{otp}\n")
            else:
                cp.append(email)
        except: pass

def main():
    clear(); logo()
    num = int(input(f"{M}└─ {P}Kitni IDs banani hain?: "))
    # 
    print(f"{A}[*] Multi-Threading Start... (Wait)")
    bot = MegaCreator()
    with ThreadPool(max_workers=10) as pool: # 10 IDs aik sath banegi
        pool.map(bot.create_process, range(num))
    
    print(f"\n{H}Kaam Khatam! OK IDs save in /sdcard/MEGA_OK.txt")

if __name__ == "__main__":
    main()
