import os, sys, time, re, random, requests
from bs4 import BeautifulSoup as bs

#--> Author: JERRY (Fixed Version)
H = "\x1b[38;5;46m"  # Green
M = "\x1b[38;5;196m" # Red
P = "\x1b[38;5;231m" # White

class JerryConfirm:
    def __init__(self):
        self.ses = requests.Session()
        self.mail_api = "https://api.mail.gw" # Best for FB 2025
        self.ok = 0
        self.loop = 0
        self.sd_path = '/sdcard/Jerry_Confirmed'
        self.setup_folder()
        self.main_menu()

    def setup_folder(self):
        if not os.path.exists(self.sd_path):
            try: os.makedirs(self.sd_path)
            except: pass

    def logo(self):
        os.system('clear')
        print(f"""{H}
      _ ______ _____  ______     __
     | |  ____|  __ \|  _ \ \   / /
     | | |__  | |__) | |_) \ \_/ / 
 _   | |  __| |  _  /|  _ < \   /  
| |__| | |____| | \ \| |_) | | |   
 \____/|______|_|  \_\____/  |_|   
 {P}------------------------------------------
 {M}>> {P}Status : {H}OTP + LINK CONFIRM (FIXED)
 {M}>> {P}Update : {H}23 Dec 2025
 {P}------------------------------------------""")

    def get_mail(self):
        try:
            dom = self.ses.get(f"{self.mail_api}/domains").json()['hydra:member'][0]['domain']
            user = f"jerry_pro_{random.randint(11111,99999)}"
            data = {"address": f"{user}@{dom}", "password": "jerry_password"}
            res = self.ses.post(f"{self.mail_api}/accounts", json=data)
            if res.status_code == 201:
                token = self.ses.post(f"{self.mail_api}/token", json=data).json()['token']
                return f"{user}@{dom}", token
            return self.get_mail()
        except: return None, None

    def fetch_and_confirm(self, token, email):
        headers = {"Authorization": f"Bearer {token}"}
        print(f" {P}└─ {H}Searching for Deep Confirmation Link...", end='\r')
        
        for _ in range(15):
            time.sleep(4)
            try:
                msgs = self.ses.get(f"{self.mail_api}/messages", headers=headers).json()['hydra:member']
                if msgs:
                    m_id = msgs[0]['id']
                    msg_full = self.ses.get(f"{self.mail_api}/messages/{m_id}", headers=headers).json()
                    
                    # Method 1: Get OTP Code
                    intro = msg_full['intro']
                    otp = re.search(r'\b\d{5}\b', intro).group()
                    
                    # Method 2: Extract Confirmation Deep Link (Ye sabse zaroori hai)
                    html_content = msg_full['html'][0] # Email ki HTML body
                    link = re.search(r'https://m\.facebook\.com/n/\?confirmemail\.php[^\s"\']+', str(html_content))
                    
                    if link:
                        final_link = link.group().replace('&amp;', '&')
                        # FB ko signal bhejna ke link click ho gaya
                        self.ses.get(final_link) 
                        return otp, "Confirmed via Deep Link"
                    return otp, "Only OTP Found"
            except: pass
        return None, None

    def start(self):
        limit = int(input(f" {M}>> {P}How many IDs?: "))
        for _ in range(limit):
            self.loop += 1
            email, token = self.get_mail()
            pwd = f"Pak_Jerry@{random.randint(10,99)}"

            if not email: continue

            print(f"\n{H}[{self.loop}] {P}Creating for: {email}")
            
            # OTP + Link confirmation
            otp, status = self.fetch_and_confirm(token, email)
            
            if otp:
                print(f" {H}└─ SUCCESS: [{otp}] | {status}")
                self.ok += 1
                result = f"{email}|{pwd}|{otp}|{status}\n"
                open('Jerry_Final_OK.txt', 'a').write(result)
                with open(f'{self.sd_path}/Verified.txt', 'a') as f: f.write(result)
            else:
                print(f" {M}└─ FAILED: OTP nahi aya ya link block hai.")
            
            # Anti-ban delay
            time.sleep(5)

    def main_menu(self):
        self.logo()
        print(f" [{H}1{P}] Start Auto-Creation & Deep-Link Confirm")
        if input(f"\n {M}>> {P}Select: ") == '1': self.start()

if __name__ == "__main__":
    JerryConfirm()
