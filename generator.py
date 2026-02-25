import random
import string

print("=== Smart Progressive Password Generator ===")

name = input("Enter Name: ").strip()
total = int(input("How many passwords generate: "))

symbols = "@#$!_."
letters = string.ascii_letters   # small + CAPITAL
digits = string.digits

passwords = set()   # no duplicate

# random number generator
def rand_num():
    return ''.join(random.choice(digits)
                   for _ in range(random.randint(1,4)))

# random mixed part
def random_mix(length):
    chars = letters + digits + symbols
    return ''.join(random.choice(chars) for _ in range(length))

# -------- SIMPLE → HARD PROGRESSION --------
level = 1

while len(passwords) < total:

    # Level 1 (simple)
    if level == 1:
        pwd = name + rand_num()

    # Level 2 (lowercase mix)
    elif level == 2:
        pwd = name.lower() + rand_num()

    # Level 3 (symbol added)
    elif level == 3:
        pwd = name + rand_num() + random.choice(symbols)

    # Level 4 (random alphabet insert)
    elif level == 4:
        pwd = name + random.choice(letters) + rand_num()

    # Level 5 (hard mix)
    else:
        pwd = name + random_mix(random.randint(3,7))

    passwords.add(pwd)

    # difficulty gradually increase
    if len(passwords) % (total//5 if total>=5 else 1) == 0:
        level += 1
        if level > 5:
            level = 5

# save file
with open("passwords.txt","w") as f:
    for p in passwords:
        f.write(p + "\n")

print("\n✅ Passwords generated (No duplicates)")
print("📄 Saved in passwords.txt")
