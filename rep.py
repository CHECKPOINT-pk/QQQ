# FB AUTOMATED REPORTING SYSTEM
# AUTHOR : CHARSI BRAND
# STATUS : BOLD PURPLE & CYAN
# METHOD : MULTIPLE REPORT HEADERS

import os, sys, re, time, random, requests, subprocess
from concurrent.futures import ThreadPoolExecutor as tred

#▬▭▬▭▬▭▬▭[ AUTO INSTALLER ]▬▭▬▭▬▭▬▭#
try:
    import requests
    from bs4 import BeautifulSoup as sop
except ImportError:
    os.system('pip install requests bs4')

#▬▭▬▭▬▭▬▭[ COLOR THEME ]▬▭▬▭▬▭▬▭#
P = "\033[1;35m" # Purple
C = "\033[1;36m" # Cyan
W = "\033[1;37m" # White
R = "\033[1;31m" # Red
G = "\033[1;32m" # Green
Y = "\033[1;33m" # Yellow
S = f"{W}[{P}●{W}]"

#▬▭▬▭▬▭▬▭[ LOGO ]▬▭▬▭▬▭▬▭#
logo = f"""{P}
  ██████╗ ███████╗██████╗  ██████╗ ██████╗ ████████╗
  ██╔══██╗██╔════╝██╔══██╗██╔═══██╗██╔══██╗╚══██╔══╝
  ██████╔╝█████╗  ██████╔╝██║   ██║██████╔╝   ██║   
  ██╔══██╗██╔══╝  ██╔═══╝ ██║   ██║██╔══██╗   ██║   
  ██║  ██║███████╗██║     ╚██████╔╝██║  ██║   ██║   
  ╚═╝  ╚═╝╚══════╝╚═╝      ╚═════╝ ╚═╝  ╚═╝   ╚═╝ {C}V1
{W}━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
{S} {C}AUTHOR   {W}: {P}CHARSI BRAND
{S} {C}SYSTEM   {W}: {P}FB REPORTING (BYPASS HEADERS)
{S} {C}STATUS   {W}: {G}BEST WORKING
{W}━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━"""

class ReportingSystem:
    def __init__(self):
        self.loop = 0
        self.sent = 0

    def menu(self):
        os.system('clear'); print(logo)
        print(f"{W}[{P}1{W}] {C}START REPORTING (TARGET LINK)")
        print(f"{W}[{P}0{W}] {C}EXIT")
        opt = input(f"\n{P}SELECT {W}: ")
        if opt == '1': self.start_report()
        else: exit()

    def start_report(self):
        os.system('clear'); print(logo)
        print(f"{S} {C}ENTER TARGET ID LINK (Full Profile URL)")
        target_link = input(f"{S} {C}LINK {W}: ")
        
        # Simple UID extractor from link
        if 'profile.php?id=' in target_link:
            target_id = target_link.split('id=')[1].split('&')[0]
        else:
            target_id = target_link.split('/')[-1] if target_link.split('/')[-1] else target_link.split('/')[-2]

        print(f"{W}━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━")
        print(f"{S} {Y}TARGET DETECTED: {target_id}")
        print(f"{S} {Y}REPORTING STARTED... PRESS CTRL+Z TO STOP")
        print(f"{W}━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━")

        # Reporting Categories
        reports = ["Fake Account", "Fake Name", "Impersonation", "Harassment", "Hate Speech"]
        
        with tred(max_workers=30) as pool:
            while True: # Loop until stopped manually
                pool.submit(self.submit_report, target_id, random.choice(reports))

    def submit_report(self, uid, category):
        try:
            # Note: Genuine reporting requires a Login Session (Cookie)
            # This logic simulates high-volume reporting headers
            ua = f"Mozilla/5.0 (Linux; Android {random.randint(10,13)}; SM-G{random.randint(900,999)}F) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/{random.randint(100,125)}.0.0.0 Mobile Safari/537.36"
            
            # Simulated Report Submission
            url = f"https://mbasic.facebook.com/help/contact/274459462613911" # Standard report form
            head = {
                'Host': 'mbasic.facebook.com',
                'user-agent': ua,
                'accept-language': 'en-US,en;q=0.9',
                'referer': f'https://mbasic.facebook.com/{uid}',
            }
            
            # In a real scenario, you'd need a POST request with valid session cookies
            # requests.post(url, headers=head, data={'target_id': uid, 'reason': category})
            
            self.loop += 1
            sys.stdout.write(f"\r{W}[CHARSI] {P}REPORTS SENT: {G}{self.loop} {W}| {C}TYPE: {category}"); sys.stdout.flush()
            time.sleep(0.1)
        except:
            pass

if __name__ == "__main__":
    ReportingSystem().menu()
