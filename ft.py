#!/usr/bin/python3
#-*-coding:utf-8-*-
# AUTHOR: CHARSI BRAND HU (V20 FINAL 2025)
# AUTO CREATE + AUTO VERIFY + AUTO COOKIE + AUTO BIO

import os, requests, re, sys, time, random, string
from concurrent.futures import ThreadPoolExecutor as CharsiTurbo

# --- COLORS ---
G = '\x1b[1;92m' # Green
W = '\x1b[1;97m' # White
R = '\x1b[1;91m' # Red
C = '\x1b[1;36m' # Cyan
Y = '\x1b[1;93m' # Yellow

loop = 0
ok, cp = [], []

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
{G} [•] TYPE      : FULLY AUTOMATED (VERIFIED)
{G} [•] ENGINE    : GRAPH API HYBRID 2025
{W} ----------------------------------------------""")

def get_premium_mail():
    # Multi-Domain High Speed Mail System
    domains = ["vintomail.com", "zandmail.com", "mentormail.net"]
    user = "".join(random.choices(string.ascii_lowercase + string.digits, k=10))
    return f"{user}@{random.choice(domains)}"

def fetch_otp(email):
    # Fast OTP Fetching from Professional Mail Server
    u, d = email.split('@')
    for _ in range(25): # Wait for code
        try:
            url = f"https://www.1secmail.com/api/v1/?action=getMessages&login={u}&domain={d}"
            msgs = requests.get(url).json()
            if msgs:
                mid = msgs[0]['id']
                content = requests.get(f"https://www.1secmail.com/api/v1/?action=readMessage&login={u}&domain={d}&id={mid}").json()
                # 5 Ya 6 digit OTP extraction
                otp = re.search(r'\b\d{5,6}\b', content['body'])
                if otp: return otp.group()
        except: pass
        time.sleep(2)
    return None

def creator_engine():
    global loop
    loop += 1
    sys.stdout.write(f'\r {W}[CHARSI-RUN] {loop} {G}OK:{len(ok)} {Y}CP:{len(cp)} ')
    sys.stdout.flush()
    
    session = requests.Session()
    email = get_premium_mail()
    pwx = "Charsi@" + "".join(random.choices(string.digits, k=4))
    first = random.choice(["Ali", "Hamza", "Zain", "Bilal", "Usman", "Ahmed"])
    last = random.choice(["Khan", "Brand", "Malik", "Jutt", "Mughal"])
    
    # 2025 High-End Headers
    ua = f"Mozilla/5.0 (Linux; Android {random.randint(11,15)}; SM-S928B) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/{random.randint(120,132)}.0.0.0 Mobile Safari/537.36 [FBAN/FB4A;FBAV/{random.randint(400,450)}.0.0.0;]"
    
    try:
        # Step 1: Open Registration & Get Tokens
        r1 = session.get("https://m.facebook.com/reg/", headers={'user-agent': ua}).text
        lsd = re.search('name="lsd" value="(.*?)"', r1).group(1)
        jazoest = re.search('name="jazoest" value="(.*?)"', r1).group(1)
        
        # Step 2: Form Submission (Creation)
        data = {
            "lsd": lsd, "jazoest": jazoest, "firstname": first, "lastname": last,
            "reg_email__": email, "reg_passwd__": pwx, "sex": "2",
            "birthday_day": random.randint(1,28), "birthday_month": random.randint(1,12),
            "birthday_year": random.randint(1995,2005), "did_submit": "1"
        }
        
        create = session.post("https://m.facebook.com/reg/submit/", data=data, headers={'user-agent': ua}, allow_redirects=True)
        
        # Step 3: Check and Verify
        otp = fetch_otp(email)
        if otp:
            # Automatic Confirmation
            v_data = {"c": otp, "submit": "Confirm"}
            session.post("https://m.facebook.com/confirmemail.php", data=v_data, headers={'user-agent': ua})
            
            # Step 4: Extract Cookies for Ready Accounts
            cookies = session.cookies.get_dict()
            if 'c_user' in cookies:
                coki = ";".join([f"{k}={v}" for k,v in cookies.items()])
                res = f"{email}|{pwx}|{coki}"
                ok.append(email)
                print(f"\n{G} [CHARSI-OK] {email} | {pwx} \n [COOKIE] {coki}")
                open('charsi_full_ready.txt', 'a').write(res + '\n')
            else:
                cp.append(email)
        else:
            cp.append(email)
            
    except Exception as e:
        pass

def main():
    logo()
    print(f" {G}[1] START HEAVY AUTO-VERIFY CREATOR")
    print(f" {G}[2] CLEAN CACHE & RESTART")
    print(f" {R}[0] EXIT")
    opt = input(f"\n {C}[?] Choice : {W}")
    if opt == '1':
        num = int(input(f" {G}[?] How Many Accounts? : {W}"))
        with CharsiTurbo(max_workers=35) as turbo:
            for _ in range(num):
                turbo.submit(creator_engine)
        print(f"\n{G} [√] Process Done. Total OK: {len(ok)}")
    elif opt == '2':
        os.system('rm -rf __pycache__'); main()
    else:
        sys.exit()

if __name__ == "__main__":
    main()
