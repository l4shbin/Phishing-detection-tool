# 🛡️ Phishing-detection-tool
**A professional heuristic-based URL analyzer built for Termux.**

[![Developer](https://img.shields.io/badge/Developer-l4shbin-green.svg)](https://github.com/l4shbin)
[![Language](https://img.shields.io/badge/Language-Python-blue.svg)](https://www.python.org/)
[![Platform](https://img.shields.io/badge/Platform-Termux-orange.svg)](https://termux.dev/)

This tool is designed to detect phishing indicators in URLs using modular heuristic analysis. Specifically optimized for efficiency within the Termux environment.

---

## 🚀 Key Features
* **Modular Architecture**: Separated into `scanner`, `database`, and `utils` for clean, maintainable code.
* **Heuristic Engine**: Detects common fraud patterns (URL masking, `@` symbols, sensitive keywords).
* **Automated Logging**: All scan results are automatically saved to `scan_history.txt`.
* **Developer-Friendly Setup**: Includes an automated setup script and command shortcuts.

---

## 📂 Repository Structure
```text
Phishing-detection-tool/
├── setup.sh             # Automated installation script
├── README.md            # Main documentation
├── .gitignore           # System ignore files
└── src/                 # Source code directory
    ├── main.py          # Application entry point
    ├── scanner.py       # Core phishing detection logic
    ├── database.py      # Log history management
    └── utils.py         # UI & Terminal formatting
