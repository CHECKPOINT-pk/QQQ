# Updated by Gemini - Dec 23, 2025
# Jerry Edition: CLI Mode + Multi-Threaded Dumping

import os, sys, time, random, json, argparse
from concurrent.futures import ThreadPoolExecutor as ThreadPool

# --- COLORS ---
X = '\033[38;5;46m' # Green
P = '\033[1;97m'    # White
M = '\033[1;91m'    # Red
B = '\033[1;94m'    # Blue

# --- JERRY LOGO ---
logo = r'''
[1;32m       ____  __________  ______  __
[1;32m      / / / / / __  / __ \/ __ \/ /
[1;36m __  / / /_/ / /_/ / /_/ / /_/ /_/ 
[1;36m/ /_/ /  ___/ _, _/ _, _/  ___/ /  
[1;34m\____/_/   /_/ |_/_/ |_/_/   /_/   
[1;97m ================================================
 [1;97m[[1;92m•[1;97m] Owner    : JERRY-XD [2025 UPDATED]
 [1;97m[[1;92m•[1;97m] Mode     : CLI & MENU SUPPORTED
[1;37m ================================================'''

def clear():
    os.system('clear')
    print(logo)

# --- THE DUMPING ENGINE ---
def dump_worker(target, cookie, token, save_to):
    try:
        import requests
        headers = {
            'user-agent': '[FBAN/FB4A;FBAV/450.0.0.10.100;FBBV/650000000;FBDM/{density=3.0,width=1080,height=2340};FBLC/en_US;FBRV/0;FBCR/T-Mobile;FBMF/samsung;FBBD/samsung;FBPN/com.facebook.katana;FBDV/SM-S928B;FBSV/15;FBOP/19;FBCA/arm64-v8a:;]',
            'host': 'graph.facebook.com'
        }
        res = requests.get(f'https://graph.facebook.com/{target.strip()}?fields=friends.limit(5000)', 
                           cookies={'cookie': cookie}, 
                           params={'access_token': token}, 
                           headers=headers).json()
        
        count = 0
        with open(save_to, 'a') as f:
            for friend in res.get('friends', {}).get('data', []):
                f.write(f"{friend['id']}|{friend['name']}\n")
                count += 1
        print(f"{X} [SUCCESS] {target.strip()} | Extracted: {count}")
    except Exception as e:
        print(f"{M} [ERROR] {target.strip()} | Account Protected or Token Expired")

def start_cli():
    parser = argparse.ArgumentParser(description="Jerry Tool CLI Mode")
    parser.add_argument("--dump", help="Target UIDs separated by comma")
    parser.add_argument("--output", help="Output file path", default="/sdcard/jerry_dump.txt")
    
    args = parser.parse_args()
    
    if args.dump:
        clear()
        try:
            token = open('.token.txt', 'r').read().strip()
            cookie = open('.cok.txt', 'r').read().strip()
        except:
            print(f"{M} [!] No login detected. Please run the tool normally first.")
            return

        targets = args.dump.split(',')
        print(f"{B} [*] Threads: 15 | Saving to: {args.output}")
        print('[38;5;40m─────────────────────────────────────────────')
        
        with ThreadPool(max_workers=15) as executor:
            for t in targets:
                executor.submit(dump_worker, t, cookie, token, args.output)
        
        print('[38;5;40m─────────────────────────────────────────────')
        print(f"{X} [!] Done! IDs saved in {args.output}")
    else:
        # If no arguments, run the standard menu
        main_menu()

def main_menu():
    clear()
    print(f"{P} [1] Start Multi-Thread Dump")
    print(f"{P} [2] Login with Cookie")
    print(f"{P} [0] Exit")
    # ... rest of your menu logic ...

if __name__ == "__main__":
    if len(sys.argv) > 1:
        start_cli()
    else:
        main_menu()
