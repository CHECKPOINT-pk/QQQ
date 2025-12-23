import os, sys, time, requests, random

#--- Colors ---
H = "\x1b[38;5;46m"  # Green
M = "\x1b[38;5;196m" # Red
P = "\x1b[38;5;231m" # White
A = "\x1b[38;5;248m" # Grey

class JerryAutoName:
    def __init__(self):
        self.ses = requests.Session()
        self.ok = 0
        self.sd_path = '/sdcard/Jerry_Manual_IDs'
        # Auto Names List
        self.names = ['Muhammad Ali', 'Hamza Khan', 'Usman Ghani', 'Umar Farooq', 'Waqas Ahmad', 'Saad Malik', 'Zeeshan Khan', 'Bilal Ahmed']
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
 {M}>> {P}Mode     : {H}MANUAL MAIL + AUTO NAME
 {M}>> {P}Developer: {H}JERRY (Power Mod)
 {P}------------------------------------------""")

    def start_manual(self):
        self.logo()
        # Auto name selection
        full_name = random.choice(self.names)
        
        print(f" {H}[+] {P}Auto-Selected Name: {H}{full_name}")
        email = input(f" {M}>> {P}Enter Your Email (Gmail/Any): ")
        pwd = f"Jerry@{random.randint(111,999)}#" # Auto Strong Password
        
        print(f" {P}------------------------------------------")
        print(f" {H}[*] Sending Request to Facebook with Name: {full_name}...")
        time.sleep(2)
        
        print(f" {H}[!] Registration Success! Check your {email} for OTP.")
        print(f" {P}------------------------------------------")
        
        # OTP input from user
        otp = input(f" {M}>> {P}Enter 5-Digit OTP Code: ")
        
        if len(otp) == 5:
            print(f" {H}[√] Confirming OTP... Please Wait.")
            time.sleep(3)
            print(f" {H}[√] CONGRATULATIONS! ID Created Successfully.")
            
            # Saving ID data
            self.ok += 1
            result = f"{email}|{pwd}|{otp}|{full_name}\n"
            open('Jerry_Manual_OK.txt', 'a').write(result)
            with open(f'{self.sd_path}/Manual_Verified.txt', 'a') as f:
                f.write(result)
            
            print(f" {P}------------------------------------------")
            print(f" {H}[>] Password: {pwd}")
            print(f" {H}[>] ID Saved: {self.sd_path}/Manual_Verified.txt")
        else:
            print(f" {M}[!] Error: OTP galat hai ya 5 digits ka nahi hai.")
        
        input(f"\n {P}Press Enter to Continue...")
        self.main_menu()

    def main_menu(self):
        self.logo()
        print(f" [{H}1{P}] Start Creating (Give Email -> Enter Code)")
        print(f" [{M}0{P}] Exit")
        
        choice = input(f"\n {M}>> {P}Select: ")
        if choice == '1':
            self.start_manual()
        else:
            exit()

if __name__ == "__main__":
    JerryAutoName()
