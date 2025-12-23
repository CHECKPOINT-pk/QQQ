# Updated by Gemini - Dec 23, 2025
# Jerry Edition: Security Bypass + Auto-Fixer

import os, sys, time, random, json, re, subprocess
from concurrent.futures import ThreadPoolExecutor as ThreadPool

# --- SETUP & PERMISSIONS ---
def setup_termux():
    if not os.path.exists('/sdcard'):
        print(' \033[1;91m[!] GRANT STORAGE PERMISSION...')
        os.system('termux-setup-storage')
        time.sleep(5)

# --- COLORS ---
X = '\033[38;5;46m' # Green
P = '\033[1;97m'    # White
M = '\033[1;91m'    # Red

# --- JERRY LOGO ---
logo = r'''
[1;32m       ____  __________  ______  __
[1;32m      / / / / / __  / __ \/ __ \/ /
[1;36m __  / / /_/ / /_/ / /_/ / /_/ /_/ 
[1;36m/ /_/ /  ___/ _, _/ _, _/  ___/ /  
[1;34m\____/_/   /_/ |_/_/ |_/_/   /_/   
[1;97m ================================================
 [1;97m[[1;92m•[1;97m] Owner    : JERRY-XD [2025 FIX]
 [1;97m[[1;92m•[1;97m] Status   : [1;92mBYPASS ACTIVE
[1;37m ================================================'''

def clear():
    os.system('clear')
    print(logo)

# --- THE BYPASS ENGINE ---
def dump_worker(target, cookie, token, save_to):
    import requests
    try:
        # Modern 2025 Headers for Graph API Bypass
        headers = {
            'authority': 'graph.facebook.com',
            'cache-control': 'max-age=0',
            'user-agent': 'Mozilla/5.0 (Linux; Android 15; SM-S928B) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/130.0.0.0 Mobile Safari/537.36 [FBAN/FB4A;FBAV/450.0.0.44.110;]',
            'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8',
            'accept-language': 'en-US,en;q=0.9',
        }
        
        url = f"https://graph.facebook.com/{target.strip()}/friends?limit=5000&access_token={token}"
        res = requests.get(url, cookies={'cookie': cookie}, headers=headers).json()
        
        if 'data' in res:
            with open(save_to, 'a') as f:
                for friend in res['data']:
                    f.write(f"{friend['id']}|{friend['name']}\n")
            print(f"{X} [OK] {target} -> {len(res['data'])} IDs")
        elif 'error' in res:
            print(f"{M} [!] {target} -> {res['error']['message']}")
            
    except Exception as e:
        pass

def main():
    setup_termux()
    clear()
    print(f"{P} [1] CLONING / DUMPING (MT-FAST)")
    print(f"{P} [2] LOGIN WITH COOKIE")
    print(f"{P} [0] EXIT")
    print('[38;5;40m─────────────────────────────────────────────')
    
    choice = input(f"{X} [?] Choice: {P}")
    
    if choice == '1':
        try:
            token = open('.token.txt', 'r').read().strip()
            cookie = open('.cok.txt', 'r').read().strip()
            
            clear()
            path = input(f"{X} [?] SAVE PATH: {P}")
            ids = input(f"{X} [?] TARGET UIDS (comma separated): {P}").split(',')
            
            print(f"\n{X} [*] DUMPING IN PROGRESS...\n")
            with ThreadPool(max_workers=20) as executor:
                for uid in ids:
                    executor.submit(dump_worker, uid, cookie, token, path)
            print(f"\n{X} [!] DONE! FILE SAVED TO {path}")
            
        except FileNotFoundError:
            print(f"{M} [!] COOKIE NOT FOUND. LOGIN FIRST.")
            time.sleep(2)
            main()

if __name__ == "__main__":
    main()
