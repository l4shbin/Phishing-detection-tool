import json
import csv
import datetime

LOG_FILE = "scan_history.txt"
JSON_FILE = "scan_history.json"
CSV_FILE = "scan_history.csv"

def save_log(url, verdict, reasons, score, conf):
    timestamp = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    entry = f"[{timestamp}] URL: {url} | Verdict: {verdict} | Score: {score} | Conf: {conf} | Reasons: {', '.join(reasons)}"
    
    # TXT log
    with open(LOG_FILE, "a") as f:
        f.write(entry + "\n")
    
    # JSON
    try:
        data = []
        try:
            with open(JSON_FILE, "r") as f:
                data = json.load(f)
        except:
            pass
        data.append({"timestamp": timestamp, "url": url, "verdict": verdict, "score": score, "confidence": conf, "reasons": reasons})
        with open(JSON_FILE, "w") as f:
            json.dump(data, f, indent=2)
    except:
        pass
    
    # CSV
    try:
        file_exists = os.path.exists(CSV_FILE)
        with open(CSV_FILE, "a", newline='') as f:
            writer = csv.writer(f)
            if not file_exists:
                writer.writerow(["Timestamp", "URL", "Verdict", "Score", "Confidence", "Reasons"])
            writer.writerow([timestamp, url, verdict, score, conf, "; ".join(reasons)])
    except:
        pass
