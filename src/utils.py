import os

G = "\033[1;32m"
R = "\033[1;31m"
Y = "\033[1;33m"
C = "\033[1;36m"
W = "\033[0m"

def clear():
    os.system('clear' if os.name == 'posix' else 'cls')

def header():
    print(f"""{G}
  _  _         _     _     _        
 | || |  ___  | |__ (_)   | |__   
 | || |_/ __| | '_ \| |   | '_ \  
 |__   _\__ \ | |_) | |   | | | | 
    |_| |___/|_.__/|_|   |_| |_| 
    {W}Modular Phishing Detector | {C}l4shbin{W}
    """)
