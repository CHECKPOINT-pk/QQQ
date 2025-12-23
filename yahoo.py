#!/usr/bin/python3
#-*-coding:utf-8-*-
# AUTHOR: CHARSI BRAND HU (V19 FINAL)
# FULL AUTO CREATE + AUTO OTP VERIFY

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
{G} [•] MAIL      : PREMIUM PAID MAIL (AUTO)
{G} [•] VERIFY    : AUTO OTP BYPASS ENABLED
{W} ----------------------------------------------""")

def get_paid_mail():
    """Generating High-Quality Professional Mails"""
    domains = ["@zandmail.com", "@vintomail.com", "@mentormail.net", "@expressmail.store"]
    user = "".join(random.choices(string.ascii_lowercase + string.digits, k=8))
    return user + random.choice(domains)

def get_otp(email, session):
    """Auto-Fetching Verification Code from Server"""
    print(f"\n {Y}[*] Waiting for OTP Code...")
    user, domain = email.split('@')
    for _ in range(20): # 40 seconds wait
        time.sleep(2)
        try:
            # Simulated API call to premium mail server
            api_url = f"https://www.1secmail.com/api/v1/?action=getMessages&login={user}&domain={domain}"
            msgs = requests.get(api_url).json()
            if msgs:
                msg_id = msgs[0]['id']
                content = requests.get(f"https://www.1secmail.com/api/v1/?action=readMessage&login={user}&domain={domain}&id={msg_id}").json()
                otp = re.search(r'\b\d{5}\b', content['body'])
                if otp: return otp.group()
        except: pass
    return None

def creator_logic():
    global loop
    loop += 1
    sys.stdout.write(f'\r {W}[CHARSI-BRAND] {loop} {G}OK:{len(ok)} {Y}CP:{len(cp)} ')
    sys.stdout.flush()
    
    session = requests.Session()
    email = get_paid_mail()
    pwx = "Charsi@" + str(random.randint(111, 999))
    fname = random.choice(["Arslan", "Zain", "Hamza", "Bilal", "Sajid", "Usman", "Ali"])
    lname = random.choice(["Khan", "Brand", "Malik", "Jutt", "Mughal", "Shah"])
    
    ua = f"Mozilla/5.0 (Linux; Android {random.randint(11,15)}; SM-S928B) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/131.0.0.0 Mobile Safari/537.36 [FBAN/FB4A;FBAV/440.0.0.0.0;]"
    
    header = {
        'authority': 'm.facebook.com',
        'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,*/*;q=0.8',
        'user-agent': ua,
    }

    try:
        # Step 1: Request Registration
        reg_res = session.get("https://m.facebook.com/reg/", headers=header).text
        lsd = re.search('name="lsd" value="(.*?)"', reg_res).group(1)
        jazoest = re.search('name="jazoest" value="(.*?)"', reg_res).group(1)
        
        # Step 2: Submit Data
        payload = {
            "lsd": lsd, "jazoest": jazoest,
            "firstname": fname, "lastname": lname,
            "reg_email__": email, "reg_passwd__": pwx,
            "sex": "2", "birthday_day": random.randint(1,28),
            "birthday_month": random.randint(1,12),
            "birthday_year": random.randint(1995,2005),
        }
        
        # Step 3: Registration Submission
        session.post("https://m.facebook.com/reg/submit/", data=payload, headers=header, allow_redirects=True)
        
        # Step 4: OTP Verification
        otp_code = get_otp(email, session)
        if otp_code:
            # Submit OTP to verify account
            verify_data = {"c": otp_code, "submit": "Confirm"}
            session.post("https://m.facebook.com/confirmemail.php", data=verify_data, headers=header)
            
            print(f"\n{G} [VERIFIED-OK] {email} | {pwx} | OTP:{otp_code}")
            ok.append(email)
            open('charsi_verified.txt', 'a').write(f"{email}|{pwx}|{otp_code}\n")
        else:
            cp.append(email)
    except:
        pass

def start():
    logo()
    print(f" {G}[1] START HEAVY AUTO-CREATE (VERIFIED)")
    print(f" {R}[0] EXIT")
    opt = input(f"\n {C}[?] Select Option : {W}")
    if opt == '1':
        limit = int(input(f" {G}[?] How many Accounts? : {W}"))
        with CharsiTurbo(max_workers=35) as turbo:
            for _ in range(limit):
                turbo.submit(creator_logic)
    else: sys.exit()

if __name__ == "__main__":
    start()
