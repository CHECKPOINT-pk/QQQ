import os, sys, time, re, random, requests
from bs4 import BeautifulSoup as bs

#--> Author's Info (Jerry Updated)
Author    = 'JERRY x Dapunta'
Status    = 'Auto-Confirm Enabled'
Version   = '2025.12'

#--> Warna (Colors)
P = "\x1b[38;5;231m" # Putih
M = "\x1b[38;5;196m" # Merah
H = "\x1b[38;5;46m"  # Hijau
A = '\x1b[38;5;248m' # Abu-Abu

class JerryDapuntaUltra:
    def __init__(self):
        self.ses = requests.Session()
        self.ok = 0
        self.loop = 0
        # Multi-API Rotator (10+ Domains Backup)
        self.apis = ["https://api.mail.gw", "https://api.mail.tm"]
        self.sd_path = '/sdcard/Jerry_Auto_Confirm'
        self.setup_storage()
        self.main_menu()

    def setup_storage(self):
        if not os.path.exists(self.sd_path):
            try: os.makedirs(self.sd_path)
            except: pass

    def logo(self):
        os.system('clear')
        print(f'''{P}_________                      __        {M}________________ {P}
\_   ___ \_______ ____ _____ _/  |_  ____{M}\_   ____|___   \\{P}
/    \  \/\_  __ \ __ \\\\__  \\\\   __\/ __ \{M}|    __)   |  _/{P}
\ 0.3 \____|  | \/ ___/ / __ \|  | \  ___/{M}|   \  |   |   \\{P}
 \________/|__|  \_____>______/__|  \____>{M}|___/  |_______/{P}
{A}      ─────────────── {M}• {P}Auto-Confirm V3 {M}• {A}───────────────{P}''')

    def get_mail_pro(self):
        # Best Mail Engine
        api = random.choice(self.apis)
        try:
            dom_res = self.ses.get(f"{api}/domains").json()
            domain = random.choice(dom_res['hydra:member'])['domain']
            user = f"jerry_pro_{random.getrandbits(32)}"
            password = "jerry_auto_pass"
            data = {"address": f"{user}@{domain}", "password": password}
            
            reg = self.ses.post(f"{api}/accounts", json=data)
            if reg.status_code == 201:
                token = self.ses.post(f"{api}/token", json=data).json()['token']
                return f"{user}@{domain}", token, api
            return self.get_mail_pro()
        except: return None, None, None

    def auto_confirm_logic(self, token, api, email):
        headers = {"Authorization": f"Bearer {token}"}
        print(f" {P}└─ {H}JERRY Fetching Code & Link... ", end='\r')
        
        for _ in range(15):
            time.sleep(4)
            try:
                msgs = self.ses.get(f"{api}/messages", headers=headers).json()['hydra:member']
                if msgs:
                    m_id = msgs[0]['id']
                    msg_data = self.ses.get(f"{api}/messages/{m_id}", headers=headers).json()
                    intro = msg_data['intro']
                    
                    # 1. Extract OTP
                    otp = re.search(r'\b\d{5}\b', intro).group()
                    
                    # 2. Extract Confirmation Link (If exists)
                    content = msg_data['text'] if 'text' in msg_data else intro
                    link = re.search(r'https://m\.facebook\.com/n/\?confirmemail\.php[^\s]+', content)
                    
                    if link:
                        confirm_url = link.group().replace('&amp;', '&')
                        self.ses.get(confirm_url) # Auto-Clicking the link
                        return otp, "Confirmed via Link"
                    return otp, "Code Found"
            except: pass
        return None, None

    def start(self):
        self.logo()
        try:
            limit = int(input(f" {M}[•] {P}Limit IDs: "))
        except: limit = 1
        
        for _ in range(limit):
            self.loop += 1
            name = f"Muhammad {random.choice(['Ali', 'Hamza', 'Saad', 'Usman', 'Waqas'])}"
            email, token, active_api = self.get_mail_pro()
            pwd = f"Jerry@{random.randint(111,999)}#"

            if not email:
                print(f"{M}[!] Mail Service Blocked. Check Internet."); break

            print(f"\n{H}[{self.loop}] {P}Target: {name}")
            print(f" {A}└─ Email: {email}")
            print(f" {A}└─ Pass : {pwd}")

            otp, status = self.auto_confirm_logic(token, active_api, email)
            
            if otp:
                print(f" {H}└─ SUCCESS: {otp} ({status})")
                self.ok += 1
                result = f"{email}|{pwd}|{otp}\n"
                open('Jerry_Dapunta_Live.txt', 'a').write(result)
                with open(f'{self.sd_path}/Verified_IDs.txt', 'a') as f: f.write(result)
            else:
                print(f" {M}└─ FAILED: OTP not received (Try Airplane Mode)")
            
            time.sleep(5)

    def main_menu(self):
        self.logo()
        print(f" {M}[{P}1{M}] {P}Auto-Create & Link Confirm")
        print(f" {M}[{P}0{M}] {P}Exit")
        if input(f"\n {M}└─ {P}Pilih : ") == '1': self.start()

if __name__ == "__main__":
    JerryDapuntaUltra()
