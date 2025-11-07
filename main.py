import os
import sys
import getpass
import hmac
import hashlib
from typing import Tuple

# Defaults (override via environment variables APP_USERNAME and APP_PASSWORD_HASH)
DEFAULT_USERNAME = "admin"
DEFAULT_PASSWORD_HASH = hashlib.sha256(b"secret").hexdigest()

USERNAME_SYSTEM = os.getenv("APP_USERNAME", DEFAULT_USERNAME)
PASSWORD_HASH_SYSTEM = os.getenv("APP_PASSWORD_HASH", DEFAULT_PASSWORD_HASH)

MAX_ATTEMPTS = 3


def hash_password(password: str) -> str:
    return hashlib.sha256(password.encode("utf-8")).hexdigest()


def login(username: str, password: str) -> bool:
    """Return True if credentials match (uses timing-safe comparison)."""
    user_ok = hmac.compare_digest(username, USERNAME_SYSTEM)
    pass_ok = hmac.compare_digest(hash_password(password), PASSWORD_HASH_SYSTEM)
    return user_ok and pass_ok


def prompt_credentials() -> Tuple[str, str]:
    username = input("Enter username: ").strip()
    password = getpass.getpass("Enter password: ")
    return username, password


def main() -> None:
    for attempt in range(1, MAX_ATTEMPTS + 1):
        username, password = prompt_credentials()
        if login(username, password):
            print("Login successful!")
            sys.exit(0)
        else:
            remaining = MAX_ATTEMPTS - attempt
            print(f"Login failed! Attempts remaining: {remaining}")
    print("Maximum attempts exceeded. Exiting.")
    sys.exit(1)


if __name__ == "__main__":
    main()
