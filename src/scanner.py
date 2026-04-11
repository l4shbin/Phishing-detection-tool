import urllib.parse
import re
import socket
import ssl
import ipaddress
from datetime import datetime

def check_url(url):
    score = 0
    reasons = []
    parsed = urllib.parse.urlparse(url if url.startswith(('http://', 'https://')) else 'https://' + url)
    netloc = parsed.netloc.lower()
    path = parsed.path + parsed.query + parsed.fragment

    # 1. Protocol check
    if parsed.scheme == 'http':
        score += 3
        reasons.append("Insecure HTTP protocol")

    # 2. IP address in domain (rare for legit sites)
    try:
        ipaddress.ip_address(netloc.split(':')[0])
        score += 4
        reasons.append("Direct IP address usage (phishing indicator)")
    except:
        pass

    # 3. Too many subdomains or dots
    dots = netloc.count('.')
    if dots > 3:
        score += 2
        reasons.append(f"Excessive subdomains/dots: {dots}")

    # 4. Suspicious characters
    if '@' in netloc:
        score += 4
        reasons.append("Username@host masking")
    if '%' in path or '#' in path:
        score += 2
        reasons.append("Heavy percent/hex encoding or fragments")

    # 5. URL shorteners expanded
    shorteners = ['bit.ly', 't.co', 'tinyurl.com', 'is.gd', 's.id', 'cutt.ly', 'ow.ly', 'goo.gl']
    if any(s in netloc for s in shorteners):
        score += 3
        reasons.append("URL shortener detected")

    # 6. Phishing keywords (case insensitive)
    keywords = ['login', 'verify', 'update', 'bank', 'paypal', 'secure', 'account', 'password', 'billing', 'confirm']
    if any(k in netloc + path for k in keywords):
        score += 2
        reasons.append("Phishing keywords found")

    # 7. Abnormal length
    if len(url) > 100:
        score += 1
        reasons.append("Abnormally long URL")

    # 8. Live checks: DNS resolve
    try:
        host = netloc.split(':')[0]
        socket.gethostbyname(host)
    except:
        score += 3
        reasons.append("DNS resolution failed")

    # 9. HTTPS cert check (if HTTPS)
    if parsed.scheme == 'https':
        try:
            context = ssl.create_default_context()
            with socket.create_connection((host, 443), timeout=5) as sock:
                with context.wrap_socket(sock, server_hostname=host) as ssock:
                    cert = ssock.getpeercert()
                    # Check expiry
                    not_after = datetime.strptime(cert['notAfter'], '%b %d %H:%M:%S %Y %Z')
                    if not_after < datetime.now():
                        score += 2
                        reasons.append("Expired SSL certificate")
                    # Mismatch hostname simple check
                    if host not in ' '.join(cert.get('subjectAltName', [])):
                        score += 1
                        reasons.append("Potential cert hostname mismatch")
        except Exception as e:
            score += 2
            reasons.append(f"SSL handshake failed: {str(e)[:50]}")

    # IDN homoglyph simple (punycode check)
    if 'xn--' in netloc:
        score += 2
        reasons.append("IDN/punycode domain (homograph risk)")

    # Verdict with confidence
    if score >= 7:
        verdict = "HIGH RISK"
        conf = "95%"
    elif score >= 4:
        verdict = "SUSPICIOUS"
        conf = "75%"
    elif score >= 1:
        verdict = "LOW RISK"
        conf = "50%"
    else:
        verdict = "CLEAN"
        conf = "10%"

    return verdict, reasons, score, conf
