import os
import sys
import time
import argparse
from src.scanner import check_url
from src.database import save_log

# Colors
G = "\033[1;32m"  # Green
R = "\033[1;31m"  # Red
Y = "\033[1;33m"  # Yellow
B = "\033[1;34m"  # Blue
C = "\033[1;36m"  # Cyan
W = "\033[0m"    # Reset

def header():
    os.system('clear' if os.name == 'posix' else 'cls')
    print(f"""
{G}

██╗░░░░░░░██╗██╗░██████╗██╗░░██╗
██║░░░░░░██╔╝██║██╔════╝██║░░██║
██║░░░░░██╔╝░██║╚█████╗░███████║
██║░░░░░███████║░╚═══██╗██╔══██║
███████╗╚════██║██████╔╝██║░░██║
╚══════╝░░░░░╚═╝╚═════╝░╚═╝░░╚═╝
{W}Repo: {C}Phishing-detection-tool (Advanced Edition){W}
Author: {C}l4shbin{W}
Status: {G}Production Ready | HTTPS/HTTP/Batch Support{W}
    """)

def print_result(url, verdict, reasons, score, conf):
    print(f"{C}[*] {W}Target: {url}")
    print(f"{W}┌" + "─" * 60)
    color = R if "HIGH" in verdict else Y if "SUSPICIOUS" in verdict else G
    print(f"{W}│ {color}[VERDICT] {verdict} (Score: {score}/10 | Confidence: {conf}){W}")
    print(f"{W}├" + "─" * 60)
    if reasons:
        for reason in reasons:
            print(f"{W}│ {R}› {reason}{W}")
    else:
        print(f"{W}│ {G}› No threats detected.{W}")
    print(f"{W}└" + "─" * 60 + "\n")

def batch_scan(file_path):
    try:
        with open(file_path, 'r') as f:
            urls = [line.strip() for line in f if line.strip()]
        print(f"{C}[*] Batch scanning {len(urls)} URLs...\n")
        for url in urls:
            verdict, reasons, score, conf = check_url(url)
            print_result(url, verdict, reasons, score, conf)
            save_log(url, verdict, reasons, score, conf)
            time.sleep(0.5)  # Rate limit
    except FileNotFoundError:
        print(f"{R}[!] File not found: {file_path}")

def main():
    header()
    parser = argparse.ArgumentParser(description="Advanced Phishing Detector")
    parser.add_argument("url", nargs="?", help="Single URL to scan")
    parser.add_argument("-f", "--file", help="File with list of URLs")
    args = parser.parse_args()

    if args.file:
        batch_scan(args.file)
    elif args.url:
        verdict, reasons, score, conf = check_url(args.url)
        print_result(args.url, verdict, reasons, score, conf)
        save_log(args.url, verdict, reasons, score, conf)
    else:
        print(f"{Y}[?] Usage: python3 main.py <url> or python3 main.py -f urls.txt{W}")
        url = input(f"{G}Enter URL: {W}")
        if url:
            verdict, reasons, score, conf = check_url(url)
            print_result(url, verdict, reasons, score, conf)
            save_log(url, verdict, reasons, score, conf)

    input("\nPress Enter to exit...")

if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        print(f"\n{R}[!] Stopped by user.{W}")
        sys.exit(0)
