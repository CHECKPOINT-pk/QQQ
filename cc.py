# Script: AUTO ACCOUNT CREATOR (NO CLONING)
# Author: CHARSI HUB (ERROR X ETHAN)
import os, requests, json, time, re, random, sys, uuid

# --- Colors ---
G = "\033[1;32m" # Green
R = "\033[1;31m" # Red
W = "\033[1;97m" # White
loop = 0
oks = []

# --- Banner ---
def clear():
    os.system('clear')
    print(f"""{G}
  ____ _   _    _    ____  ____ ___ 
 / ___| | | |  / \  |  _ \/ ___|_ _|
| |   | |_| | / _ \ | |_) \___ \ | | 
| |___|  _  |/ ___ \|  _ < ___) || | 
 \____|_| |_/_/   \_\_| \_\____/___|
{R}--------------------------------------------------
{W} [•] AUTHOR    : {G}CHARSI HUB
{W} [•] FEATURE   : {G}AUTO FB ID CREATOR
{W} [•] STATUS    : {G}ONLY CREATION (NO CLONING)
{R}--------------------------------------------------""")

# --- Super USA User-Agent ---
def get_ua():
    ver = random.choice(['12','13','14'])
    fbv = f"{random.randint(440, 490)}.0.0.{random.randint(10, 80)}"
    device = random.choice(['Pixel 7','SM-S918U','Pixel 8 Pro'])
    return f'Mozilla/5.0 (Linux; Android {ver}; {device}) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/{random.randint(110,128)}.0.0.0 Mobile Safari/537.36 [FB_IAB/FB4A;FBAV/{fbv};FBBV/{random.randint(500000000, 600000000)};FBLC/en_US;]'

# --- Main Menu ---
def Menu():
    clear()
    print(f' {W}[1] AUTO CREATE (BINA VERIFICATION - FAST)')
    print(f' {W}[2] AUTO CREATE (WITH EMAIL VERIFICATION)')
    print(f' {W}[0] EXIT')
    print(f'{R}--------------------------------------------------')
    opt = input(f' {G}SELECT : {W}')
    if opt == '1': Create_Fast()
    elif opt == '2': Create_Verify()
    else: exit()

# --- Method 1: Fast Creation (No Verification) ---
def Create_Fast():
    clear()
    limit = int(input(f' {G}HOW MANY IDS? : {W}'))
    print(f' {G}CREATING WITHOUT VERIFICATION...')
    print(f'{R}--------------------------------------------------')
    for _ in range(limit):
        submit_reg(verify=False)
    print(f'\n{G}DONE! CHECK /sdcard/CHARSI-CREATED.txt')

# --- Method 2: Creation with Verification ---
def Create_Verify():
    clear()
    limit = int(input(f' {G}HOW MANY IDS? : {W}'))
    print(f' {G}CREATING WITH EMAIL VERIFICATION...')
    print(f'{R}--------------------------------------------------')
    for _ in range(limit):
        submit_reg(verify=True)

def submit_reg(verify):
    global loop, oks
    try:
        # Generate Fake Identity
        first = random.choice(['John','David','Mike','Robert'])
        last = random.choice(['Smith','Brown','Wilson','Taylor'])
        
        # Get Temp Email
        mail_api = requests.get('https://www.1secmail.com/api/v1/?action=genEmail&count=1').json()
        email = mail_api[0]
        password = first + str(random.randint(111,999)) + "@"
        
        ua = get_ua()
        url = "https://b-api.facebook.com/method/user.register"
        data = {
            'firstname': first, 'lastname': last, 'email': email,
            'password': password, 'gender': 'MALE', 'format': 'json',
            'device_id': str(uuid.uuid4()), 'access_token': '350685531728|62f8ce9f74b12f84c123cc23437a4a32'
        }
        
        res = requests.post(url, data=data, headers={'User-Agent': ua}).json()
        
        if 'session_key' in str(res):
            print(f'\n{G} [SUCCESS] {email} | {password}')
            if verify:
                print(f' {W}Checking Code for {email}...')
                time.sleep(10) # Wait for code
                # Logic to check inbox
                user_mail, domain = email.split('@')
                check_url = f'https://www.1secmail.com/api/v1/?action=getMessages&login={user_mail}&domain={domain}'
                msg = requests.get(check_url).json()
                if msg: print(f' {G}Verification Code Found: {msg[0]["id"]}')
            
            oks.append(email)
            open('/sdcard/CHARSI-CREATED.txt', 'a').write(email+'|'+password+'\n')
        else:
            print(f'\r {R}Spam Detected/Failed...           ', end='')
        
        loop += 1
    except: pass

if __name__ == "__main__":
    Menu()
