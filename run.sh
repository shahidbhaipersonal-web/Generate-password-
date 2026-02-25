#!/data/data/com.termux/files/usr/bin/bash

clear

while true
do
echo -e "\e[1;32m"
echo "================================="
echo "     SMART PASSWORD TOOL"
echo "================================="
echo "1. Generate Passwords"
echo "2. View Password List"
echo "3. Delete Password List"
echo "4. Exit"
echo "================================="
echo -e "\e[0m"

read -p "Select Option: " choice

case $choice in

1)
python generator.py
read -p "Press Enter to continue..."
clear
;;

2)
if [ -f passwords.txt ]; then
less passwords.txt
else
echo "No password file found!"
sleep 2
fi
clear
;;

3)
rm -f passwords.txt
echo "Password list deleted ✅"
sleep 2
clear
;;

4)
echo "Goodbye 👋"
exit
;;

*)
echo "Invalid option!"
sleep 2
clear
;;

esac
done
