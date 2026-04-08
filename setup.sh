#!/bin/bash
echo "Installing l4shbin Phishing Tool..."
pkg update && pkg upgrade -y
pkg install python -y
echo "Installation Complete. Run 'python src/main.py' to start."
