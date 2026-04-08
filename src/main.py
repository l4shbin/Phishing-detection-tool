import os
import sys
import time

# --- [ COLOR CONFIGURATION ] ---
G = "\033[1;32m" # Green (Success)
R = "\033[1;31m" # Red (Danger)
Y = "\033[1;33m" # Yellow (Warning)
B = "\033[1;34m" # Blue (Info)
C = "\033[1;36m" # Cyan (Process)
W = "\033[0m"    # White (Reset)

# --- [ UI COMPONENTS ] ---
def l4sh_header():
    os.system('clear' if os.name == 'posix' else 'cls')
    print(f"""{G}
  _  _         _     _     _        
 | || |  ___  | |__ (_)   | |__   
 | || |_/ __| | '_ \| |   | '_ \  
 |__   _\__ \ | |_) | |   | | | | 
    |_| |___/ |_.__/|_|   |_| |_| 
                                    
 {W}Repository : {C}Phishing-detection-tool{W}
 Author     : {C}l4shbin{W}
 Status     : {G}Stable / Execution Ready{W}
    """)

def analyze_logic(url):
    print(f"{C}[*]{W} Initializing heuristic scan...")
    time.sleep(1.2)
    print(f"{C}[*]{W} Target: {url}\n")
    
    risk_score = 0
    detections = []

    # 1. Protocol Security Audit
    if url.startswith("http://"):
        risk_score += 2
        detections.append("Insecure Protocol (HTTP detected)")
    
    # 2. Domain Masking Check
    shorteners = ['bit.ly', 't.co', 'tinyurl', 'is.gd', 'cutt.ly', 's.id']
    if any(s in url.lower() for s in shorteners):
        risk_score += 2
        detections.append("URL Masking detected (Shortener service)")

    # 3. Redirect Character Analysis
    if "@" in url:
        risk_score += 3
        detections.append("Bypass character '@' found (High Risk)")

    # 4. Social Engineering Keyword Match
    keywords = ['login', 'verify', 'account', 'secure', 'banking', 'update', 'claim', 'gift']
    if any(k in url.lower() for k in keywords):
        risk_score += 1
        detections.append("Credential-harvesting keywords found")

    # --- [ DISPLAY RESULTS ] ---
    print(f"{W}┌" + "─"*40)
    
    if risk_score >= 4:
        print(f"{W}│ {R}[STATUS] RESULT: HIGH RISK / PHISHING{W}")
    elif 1 <= risk_score < 4:
        print(f"{W}│ {Y}[STATUS] RESULT: SUSPICIOUS / CAUTION{W}")
    else:
        print(f"{W}│ {G}[STATUS] RESULT: CLEAN / NO THREAT{W}")
    
    print(f"{W}├" + "─"*40)
    
    if not detections:
        print(f"{W}│ {G}» No malicious patterns identified.{W}")
    else:
        for report in detections:
            print(f"{W}│ {R}» {W}{report}")
            
    print(f"{W}└" + "─"*40 + "\n")

# --- [ MAIN EXECUTION ] ---
def run():
    l4sh_header()
    try:
        target_url = input(f"{G}l4shbin{W}@{G}terminal{W}:~# ")
        if not target_url:
            print(f"{R}[!] Error: Target URL cannot be empty.{W}")
            return
        
        analyze_logic(target_url)
        
    except KeyboardInterrupt:
        print(f"\n{R}[!] Execution halted by user.{W}")
        sys.exit()

if __name__ == "__main__":
    run()
