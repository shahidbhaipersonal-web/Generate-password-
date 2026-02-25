#!/data/data/com.termux/files/usr/bin/bash

clear
echo "Installing Smart Generator Tool..."

pkg update -y
pkg install python -y

chmod +x run.sh

echo ""
echo "✅ Installation Complete"
echo "Type: ./run.sh"
