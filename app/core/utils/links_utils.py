import secrets
import string


def generate_link():
    symbols = string.digits + string.ascii_letters
    return ''.join(secrets.choice(symbols) for _ in range(8))
