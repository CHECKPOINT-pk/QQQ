# ENJOY OPEN SOURCE AUTO CREATE FB 
# AUTHOR : ETHAN KLEIN HUILEN
# GITHUB  : MR-ERROR-708
# THANK YOU.
#▬▭▬▭▬▭▬▭[IMPORT]▬▭▬▭▬▭▬▭#
import os,sys,re,time,json,mechanize,asyncio,aiohttp,requests,urllib.parse,bs4,string,faker,random,uuid,hashlib,subprocess,platform
from faker import Faker
from bs4 import BeautifulSoup
from fake_useragent import UserAgent
from datetime import datetime,timedelta
from time import sleep as sp

#▬▭▬▭▬▭▬▭[COLOR CODE]▬▭▬▭▬▭▬▭#
white = "\x1b[1;97m";yelloww = "\033[1;33m";green = "\x1b[38;5;49m";G0 = "\x1b[38;5;155m";green1 = '\x1b[38;5;154m';G2 = '\x1b[38;5;47m';G3 = '\x1b[38;5;48m';G4 = '\x1b[38;5;49m';G5 = '\x1b[38;5;50m';G6 = "\x1b[38;5;52m";s = "\033[0m";W = "\033[1;30m";Y = "\x1b[1;93m";red = "\x1b[38;5;160m";B = "\033[1;95m";BE = "\x1b[1;35m";X = "\x1b[1;96m";Z = "\x1b[1;95m";Y = "\033[1;93m";U = "\033[1;94m";V = "\033[38;5;47m";T = "\033[38;5;48m";Q = "\033[38;5;49m";P = "\033[38;5;50m";O = "\033[38;5;51m";N = "\033[38;5;52m";M = "\x1b[38;5;205m";L = "\033[96;1m";K = "\x1b[1;91m";WH = "\033[1;97m";orange = "\x1b[38;5;196m";yellow = "\x1b[38;5;208m";black="\033[1;30m";rad="\x1b[38;5;160m";YLW="\033[1;33m";blue="\033[38;5;6m";purple="\033[1;35m";cyan="\033[1;36m";white="\033[1;37m";faltu = "\033[1;47m";pvt = "\033[1;0m";gren = "\x1b[38;5;154m";gas = "\033[1;32m"
style=f"\033[1;37m[\033[1;32m●\033[1;37m]"
stylee=f"\033[1;37m[\033[1;31m!\033[1;37m]"

#▬▭▬▭▬▭▬▭[STORAGE PERMISSION]▬▭▬▭▬▭▬▭#
try:
    if not os.path.exists('/sdcard'):
        os.system('termux-setup-storage')
except:pass

#▬▭▬▭▬▭▬▭[USER AGENT]▬▭▬▭▬▭▬▭#
ua=UserAgent()
def get_pro_ua():
    return ua.random

#▬▭▬▭▬▭▬▭[EXTRACTOR]▬▭▬▭▬▭▬▭#
def extractor(data):
    try:
        soup=BeautifulSoup(data,"html.parser")
        inputs_data={}
        for inputs in soup.find_all("input"):
            name=inputs.get("name")
            value=inputs.get("value")
            if name: inputs_data[name]=value
        return inputs_data
    except: return {}

#▬▭▬▭▬▭▬▭[PASSWORDS]▬▭▬▭▬▭▬▭#
random_password1=['magandaako','gandako','pogiako','pogiako123','gwapoako123']
random_password2=['nepal12','nepal123','nepal1234','maya123','kathmandu']
random_password3=['khankhan','khan1122','ali12345','khanbaba','pakistan']
random_password4=['afghan','afghan12345','Afghan123','600700','afghanistan']
random_password5=['Bangladesh','bangladesh','iloveyou','freefire','708090']
random_password6=['57575751','57273200','iloveyou','59039200','708090']

#▬▭▬▭▬▭▬▭[BANNER]▬▭▬▭▬▭▬▭#
logo = f"""{green}
 ▗▖ ▗  ▖▄▄▄▖ ▄▄      ▗▄ ▗▄▄ ▗▄▄▖ ▗▖ ▄▄▄▖▗▄▄▖    ▗▄▄▖▗▄▄ 
 ▐▌ ▐  ▌ ▐  ▗▘▝▖    ▗▘ ▘▐ ▝▌▐    ▐▌  ▐  ▐       ▐   ▐  ▌
 ▌▐ ▐  ▌ ▐  ▐  ▌    ▐   ▐▄▄▘▐▄▄▖ ▌▐  ▐  ▐▄▄▖    ▐▄▄▖▐▄▄▘
 ▙▟ ▐  ▌ ▐  ▐  ▌    ▐   ▐ ▝▖▐    ▙▟  ▐  ▐       ▐   ▐  ▌
▐  ▌▝▄▄▘ ▐   ▙▟      ▚▄▘▐  ▘▐▄▄▖▐  ▌ ▐  ▐▄▄▖    ▐   ▐▄▄▘ {white}MR-ERROR"""

def main_logo():
    os.system("clear")
    print(logo)
    print(f"\033[1;37m━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━")
    print(f"{style} \033[1;32mAUTHOR   \033[1;37m: \033[1;32mETHAN KLEIN HUILEN")
    print(f"{style} \033[1;32mVERSION  \033[1;37m: \033[1;32m0.9 (WORKING)")
    print(f"\033[1;37m━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━")

oks, cps, loop = [], [], 0

#▬▭▬▭▬▭▬▭[MAIN MENU]▬▭▬▭▬▭▬▭#
def main():
    main_logo()
    print(f'\033[1;37m[\033[1;32mA\033[1;37m]\033[1;32m START AUTO CREATE')
    print(f'\033[1;37m[\033[1;32mO\033[1;37m]\033[1;31m EXIT PROGRAM')
    print(f"\033[1;37m━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━")
    opt = input(f'{style} \033[1;32mCHOOSE {white}: ')
    if opt in ['A','a','1']: create_menu()
    else: sys.exit()

def create_menu():
    main_logo()
    try: limit = int(input(f"{style} \033[1;32mACCOUNT LIMIT {white}: "))
    except: limit = 10
    
    print(f"\033[1;37m━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━")
    print(f"[A] PHILIPPINES [B] NEPAL [C] PAKISTAN")
    print(f"[D] AFGHANISTAN [E] BANGLADESH [F] INDIA")
    print(f"\033[1;37m━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━")
    p_opt = input(f'{style} \033[1;32mCHOOSE COUNTRY {white}: ').upper()
    
    main_logo()
    print(f"{style} \033[1;32mCREATING {limit} ACCOUNTS...")
    print(f"\033[1;37m━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━")

    for i in range(limit):
        process_creation(p_opt)
        print(f"\r{white}[PROGRESS] {i+1}/{limit} | {green}OK:{len(oks)} {red}CP:{len(cps)}", end="")

def process_creation(p_opt):
    global loop
    ses = requests.Session()
    fk = Faker()
    fname = fk.first_name()
    lname = fk.last_name()
    email = f"{fname.lower()}{lname.lower()}{random.randint(100,999)}@gmail.com"
    
    if p_opt == 'A': pwd = random.choice(random_password1)
    elif p_opt == 'B': pwd = random.choice(random_password2)
    elif p_opt == 'C': pwd = random.choice(random_password3)
    elif p_opt == 'D': pwd = random.choice(random_password4)
    elif p_opt == 'E': pwd = random.choice(random_password5)
    else: pwd = random.choice(random_password6)

    try:
        res = ses.get('https://m.facebook.com/reg/', timeout=15)
        form = extractor(res.text)
        
        payload = {
            'firstname': fname,
            'lastname': lname,
            'reg_email__': email,
            'reg_passwd__': pwd,
            'birthday_day': str(random.randint(1,28)),
            'birthday_month': str(random.randint(1,12)),
            'birthday_year': str(random.randint(1992,2005)),
            'sex': '2',
            **form
        }
        
        headers = {'User-Agent': get_pro_ua(), 'Accept-Language': 'en-US,en;q=0.9'}
        reg_submit = ses.post('https://m.facebook.com/reg/submit/', data=payload, headers=headers, timeout=15)
        
        if "c_user" in ses.cookies.get_dict():
            uid = ses.cookies.get_dict()['c_user']
            oks.append(uid)
            print(f"\n{green}[SUCCESS-OK] {uid} | {pwd}")
            open("/sdcard/MR-ERROR-OK.txt","a").write(f"{uid}|{pwd}\n")
        else:
            cps.append(email)
    except:
        pass

if __name__ == "__main__":
    main()
