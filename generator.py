import random
import string

print("=== Smart Password Generator ===")

name = input("Enter Name: ").lower()
year = input("Enter Birth Year: ")
city = input("Enter City: ").lower()

total = int(input("How many passwords generate: "))

words = [name, city, "admin", "user", "india"]
symbols = "@#$!_."
chars = string.ascii_letters + string.digits + symbols

def make_pass():
    word = random.choice(words)
    tail = ''.join(random.choice(chars) for _ in range(3))
    return word + year + tail

with open("passwords.txt","w") as f:
    for i in range(total):
        f.write(make_pass()+"\n")

print("\n✅ Password list saved in passwords.txt")
