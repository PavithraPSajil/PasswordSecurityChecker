import re

common_passwords = [
    "password",
    "123456",
    "123456789",
    "qwerty",
    "abc123",
    "admin",
    "welcome",
    "letmein"
]

def check_password(password):

    score = 0

    has_upper = bool(re.search(r"[A-Z]", password))
    has_lower = bool(re.search(r"[a-z]", password))
    has_digit = bool(re.search(r"\d", password))
    has_special = bool(re.search(r"[!@#$%^&*(),.?\":{}|<>]", password))

    if len(password) >= 8:
        score += 1

    if has_upper:
        score += 1

    if has_lower:
        score += 1

    if has_digit:
        score += 1

    if has_special:
        score += 1

    common = password.lower() in common_passwords

    if common:
        strength = "Very Weak"

    elif score <= 2:
        strength = "Weak"

    elif score == 3:
        strength = "Medium"

    elif score == 4:
        strength = "Strong"

    else:
        strength = "Very Strong"

    return {
        "Length": len(password),
        "Uppercase": has_upper,
        "Lowercase": has_lower,
        "Digits": has_digit,
        "Special Characters": has_special,
        "Common Password": common,
        "Strength": strength
    }