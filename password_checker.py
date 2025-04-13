import re

used_passwords = []

def check_strength(password):
    length = len(password) >= 8
    digit = re.search(r"\d", password)
    upper = re.search(r"[A-Z]", password)
    lower = re.search(r"[a-z]", password)
    symbol = re.search(r"[!@#$%^&*(),.?\":{}|<>]", password)
    
    score = sum([length, bool(digit), bool(upper), bool(lower), bool(symbol)])
    
    if score <= 2:
        return "Weak"
    elif score == 3 or score == 4:
        return "Medium"
    else:
        return "Strong"

while True:
    pwd = input("Enter a password (or 'exit' to quit): ")
    if pwd == "exit":
        break
    if pwd in used_passwords:
        print("You already used this password.")
        continue
    strength = check_strength(pwd)
    print("Password strength:", strength)
    used_passwords.append(pwd)
