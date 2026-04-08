# Phishing-detection-tool

A lightweight, terminal-based heuristic engine for detecting phishing attempts via URL analysis. Built specifically for the **Termux** environment.

## ⚙️ How it Works
`Phishing-detection-tool` evaluates URLs against known social engineering patterns, including:
* **Obfuscation Detection**: Identifies URL shorteners used to hide the final destination.
* **Redirection Analysis**: Detects the `@` symbol used to bypass browser address bars.
* **Insecure Protocol Audit**: Flags unencrypted HTTP connections.
* **Keyword Matching**: Scans for credential-harvesting triggers (e.g., *login*, *verify*, *banking*).

## 🚀 Installation

```bash
# Update environment
pkg update && pkg upgrade -y

# Install dependencies
pkg install python git -y

# Clone and run
git clone [https://github.com/l4shbin/Phishing-detection-tool](https://github.com/l4shbin/Phishing-detection-tool)
cd Phishing-detection-tool
python src/main.py
