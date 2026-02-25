import random
import string

print("=== Smart Sequential Password Generator ===")

name = input("Enter Name: ").strip()
nickname = input("Enter Nickname: ").strip()
year = input("Enter Birth Year: ")

total = int(input("How many passwords generate: "))

# character sets
lower = string.ascii_lowercase
upper = string.ascii_uppercase
digits = string.digits
symbols = "@#$!_."

def strong_tail():
    # ensure all types included
    part = [
        random.choice(lower),
        random.choice(upper),
        random.choice(digits),
        random.choice(symbols)
    ]
    extra = ''.join(random.choice(lower+upper+digits+symbols)
                    for _ in range(3))
    random.shuffle(part)
    return ''.join(part) + extra

passwords = []

half = total // 2

# ---- NAME BASE PASSWORDS ----
for _ in range(half):
    pwd = name + year + strong_tail()
    passwords.append(pwd)

# ---- NICKNAME BASE PASSWORDS ----
for _ in range(total - half):
    pwd = nickname + year + strong_tail()
    passwords.append(pwd)

# save file
with open("passwords.txt", "w") as f:
    for p in passwords:
        f.write(p + "\n")

print("\n✅ Passwords generated successfully!")
print("📄 Saved in passwords.txt")
