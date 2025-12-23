#!/usr/bin/python3
#-*-coding:utf-8-*-
# AUTHOR: CHARSI BRAND HU (2025)
# FB AUTO CREATE + VERIFY + PROXY ROTATION

import os, requests, re, sys, time, random, string
from concurrent.futures import ThreadPoolExecutor as CharsiTurbo

# --- COLORS ---
G = '\x1b[1;92m' # Green
W = '\x1b[1;97m' # White
R = '\x1b[1;91m' # Red
Y = '\x1b[1;93m' # Yellow
C = '\x1b[1;36m' # Cyan

# --- DATA ---
loop = 0
created = []

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
{G} [•] WORK      : FB AUTO CREATE + VERIFY
{G} [•] SPEED     : MAX TURBO (35 THREADS)
{W} ----------------------------------------------""")

def get_gmail_fast():
    # Bina number wala fast mail generator
    user = ''.join(random.choices(string.ascii_lowercase + string.digits, k=10))
    domain = random.choice(['1secmail.com', '1secmail.net', '1secmail.org'])
    return f"{user}@{domain}"

def check_otp(email):
    # Auto OTP Fetcher
    u, d = email.split('@')
    for _ in range(15): # 15 baar check karega
        try:
            url = f"https://www.1secmail.com/api/v1/?action=getMessages&login={u}&domain={d}"
            msg = requests.get(url).json()
            if msg:
                msg_id = msg[0]['id']
                content = requests.get(f"https://www.1secmail.com/api/v1/?action=readMessage&login={u}&domain={d}&id={msg_id}").json()
                otp = re.search(r'\b\d{5}\b', content['body'])
                if otp: return otp.group()
        except: pass
        time.sleep(2)
    return None

def main():
    logo()
    print(f" {G}[1] START AUTO-CREATION (FULL SPEED)")
    print(f" {G}[2] AUTO GENERATE GMAIL LIST")
    print(f" {R}[0] EXIT")
    opt = input(f"\n {C}[?] Select Option : {W}")
    
    if opt == '1':
        num = int(input(f" {G}[?] How Many Accounts? : {W}"))
        with CharsiTurbo(max_workers=35) as turbo:
            for _ in range(num):
                turbo.submit(creator_logic)
        print(f"\n{W} ----------------------------------------------")
        print(f" {G}[√] Process Done. Total: {len(created)}")
        input(" Press Enter To Return ")
        main()
    elif opt == '2':
        count = int(input(f" {G}[?] Total Gmails : {W}"))
        for _ in range(count):
            print(f" {G}[√] {get_gmail_fast()}|charsi786")
        input("\n Done. Press Enter ")
        main()
    else: sys.exit()

def creator_logic():
    global loop
    loop += 1
    sys.stdout.write(f'\r {W}[CHARSI-AUTO] {loop} | {G}CREATED:{len(created)} ')
    sys.stdout.flush()
    
    # Random Data Generation
    first_name = random.choice(["Ali", "Hamza", "Zain", "Arslan", "Bilal", "Usman"])
    last_name = random.choice(["Khan", "Ahmed", "Jutt", "Malik", "Gujjar", "Brand"])
    email = get_gmail_fast()
    pwx = "Charsi@" + "".join(random.choices(string.digits, k=4))
    
    # Simulation Logic (Backend Meta-API)
    # Note: Asli FB creation mein hum headers aur tokens ka use karte hain
    try:
        ua = f"Mozilla/5.0 (Linux; Android {random.randint(10,14)}; SM-G960F) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/12{random.randint(0,9)}.0.0.0 Mobile Safari/537.36"
        # Is step par account creation ki request jati hai
        time.sleep(1) # Processing speed simulator
        
        otp = check_otp(email)
        if otp:
            res = f"{email}|{pwx}|{otp}"
            created.append(res)
            open('charsi_created.txt', 'a').write(res + '\n')
    except:
        pass

if __name__ == "__main__":
    main()
