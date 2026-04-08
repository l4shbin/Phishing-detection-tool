import datetime

LOG_FILE = "scan_history.txt"

def save_log(url, status):
    timestamp = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    with open(LOG_FILE, "a") as f:
        f.write(f"[{timestamp}] URL: {url} | Result: {status}\n")
