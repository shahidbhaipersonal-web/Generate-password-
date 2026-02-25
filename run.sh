#!/data/data/com.termux/files/usr/bin/bash

# COLORS
G="\e[1;32m"
R="\e[1;31m"
C="\e[1;36m"
Y="\e[1;33m"
N="\e[0m"

clear

# ===== BANNER =====
echo -e $G
echo " ███████╗ ███╗   ███╗ █████╗ ██████╗ ████████╗"
echo " ██╔════╝ ████╗ ████║██╔══██╗██╔══██╗╚══██╔══╝"
echo " ███████╗ ██╔████╔██║███████║██████╔╝   ██║   "
echo " ╚════██║ ██║╚██╔╝██║██╔══██║██╔══██╗   ██║   "
echo " ███████║ ██║ ╚═╝ ██║██║  ██║██║  ██║   ██║   "
echo " ╚══════╝ ╚═╝     ╚═╝╚═╝  ╚═╝╚═╝  ╚═╝   ╚═╝   "
echo -e $C
echo "        SMART PASSWORD TOOL"
echo -e $N

# ===== LOADING =====
echo -ne $Y"Loading "
for i in {1..5}
do
echo -n "."
sleep 0.4
done
echo -e "\n"$N

# ===== MENU LOOP =====
while true
do
echo -e $G
echo "================================="
echo "1. Generate Passwords"
echo "2. View Password List"
echo "3. Delete Password List"
echo "4. Exit"
echo "================================="
echo -e $N

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
echo -e $R"No password file found!"$N
sleep 2
fi
clear
;;

3)
rm -f passwords.txt
echo -e $C"Password list deleted ✅"$N
sleep 2
clear
;;

4)
echo -e $Y"Goodbye 👋"$N
exit
;;

*)
echo -e $R"Invalid option!"$N
sleep 2
clear
;;

esac
done
