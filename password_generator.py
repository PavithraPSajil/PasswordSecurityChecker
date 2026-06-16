import random
import string

def generate_password(length=14):
    password = [
        random.choice(string.ascii_uppercase),
        random.choice(string.ascii_lowercase),
        random.choice(string.digits),
        random.choice("!@#$%^&*")
    ]

    characters = string.ascii_letters + string.digits + "!@#$%^&*"

    while len(password) < length:
        password.append(random.choice(characters))

    random.shuffle(password)

    return "".join(password)