# smart_wordlist_generator.py
# Educational / password strength testing only

import random
import string

print("=== Smart Password Generator ===")

# -------- USER PROFILE INPUT --------
name = input("Enter Name: ").lower()
nickname = input("Enter Nickname: ").lower()
birthyear = input("Enter Birth Year: ")
city = input("Enter City: ").lower()
fav = input("Enter Favourite word: ").lower()

TOTAL_PASSWORDS = int(input("How many passwords generate? (example 1000000): "))

OUTPUT_FILE = "smart_wordlist.txt"

# -------- WORD BASE --------
base_words = [name, nickname, city, fav, "admin", "user", "india"]

letters = string.ascii_lowercase
LETTERS = string.ascii_uppercase
digits = string.digits
symbols = "@#$!_."

all_chars = letters + LETTERS + digits + symbols

def random_tail():
    length = random.randint(2,5)
    return ''.join(random.choice(all_chars) for _ in range(length))

print("\nGenerating passwords...")

with open(OUTPUT_FILE, "w") as f:
    for i in range(TOTAL_PASSWORDS):

        word = random.choice(base_words)

        pattern = random.choice([
            word + birthyear,
            word.capitalize() + birthyear,
            word + random_tail(),
            word + random.choice(symbols) + birthyear,
            word.capitalize() + random_tail(),
            word + birthyear + random.choice(symbols)
        ])

        f.write(pattern + "\n")

        if i % 100000 == 0 and i != 0:
            print(f"{i} passwords generated...")

print(f"\n✅ Done! Saved in {OUTPUT_FILE}")
