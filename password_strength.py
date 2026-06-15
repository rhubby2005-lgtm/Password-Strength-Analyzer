import re

print("===== Password Strength Analyzer =====")

password = input("Enter a password: ")

strength_score = 0

if len(password) >= 8:
    print("✓ Length Check: Passed")
    strength_score += 1
else:
    print("✗ Length Check: Password should be at least 8 characters long")

if re.search(r"[A-Z]", password):
    print("✓ Uppercase Letter Check: Passed")
    strength_score += 1
else:
    print("✗ Uppercase Letter Check: Missing")

if re.search(r"[a-z]", password):
    print("✓ Lowercase Letter Check: Passed")
    strength_score += 1
else:
    print("✗ Lowercase Letter Check: Missing")

if re.search(r"[0-9]", password):
    print("✓ Number Check: Passed")
    strength_score += 1
else:
    print("✗ Number Check: Missing")

if re.search(r"[!@#$%^&*(),.?\":{}|<>]", password):
    print("✓ Special Character Check: Passed")
    strength_score += 1
else:
    print("✗ Special Character Check: Missing")

print("\n===== Result =====")

if strength_score <= 2:
    print("Password Strength: WEAK")
elif strength_score <= 4:
    print("Password Strength: MEDIUM")
else:
    print("Password Strength: STRONG")
