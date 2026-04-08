def check_url(url):
    score = 0
    reasons = []

    # Heuristics
    if url.startswith("http://"):
        score += 2
        reasons.append("Insecure Protocol (HTTP)")
    
    if "@" in url:
        score += 3
        reasons.append("Redirect symbol '@' detected")

    shorteners = ['bit.ly', 't.co', 'tinyurl', 'is.gd', 's.id']
    if any(s in url.lower() for s in shorteners):
        score += 2
        reasons.append("URL Shortener masking")

    keywords = ['login', 'verify', 'update', 'banking', 'secure']
    if any(k in url.lower() for k in keywords):
        score += 1
        reasons.append("Phishing keywords identified")

    # Final Verdict
    if score >= 4: return "HIGH RISK", reasons
    if 1 <= score < 4: return "SUSPICIOUS", reasons
    return "CLEAN", reasons
