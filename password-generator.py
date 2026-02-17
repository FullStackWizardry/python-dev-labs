"""
input : how many passwords? ex:3
output :
1 : ...
2 : ...
3 : ...
"""

import secrets
import string


def generate_password(length: int = 12) -> str:
    chars = string.ascii_letters + string.digits + string.punctuation
    return ''.join(secrets.choice(chars) for _ in range(length))


def generate_password_list(count: int, length: int = 12) -> list:
    passwords = []
    for _ in range(count):
        passwords.append(generate_password(length))
    return passwords


def main():
    try:
        count = int(input("How many passwords? "))
        if count <= 0:
            raise ValueError("Number must be > 0")

        passwords = generate_password_list(count)

        print("\nGenerated Passwords:")
        for i, pwd in enumerate(passwords, 1):
            print(f"{i}: {pwd}")

    except ValueError as e:
        print("Invalid input:", e)


if __name__ == "__main__":
    main()