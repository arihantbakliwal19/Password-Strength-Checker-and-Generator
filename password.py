import hashlib
import string
import random

def password_strength(password):
    # Define the criteria for password strength
    criteria = {
        "length": len(password) >= 8,
        "uppercase": any(c.isupper() for c in password),
        "lowercase": any(c.islower() for c in password),
        "digit": any(c.isdigit() for c in password),
        "special": any(c in string.punctuation for c in password)
    }

    # Define the time it would take to crack the password
    crack_time = {
        "very_weak": "less than a second",
        "weak": "a few minutes",
        "moderate": "a few hours",
        "strong": "several years",
        "very_strong": "more than a century"
    }

    # Calculate the strength of the password based on the criteria
    if all(criteria.values()):
        strength = "very_strong"
    elif criteria["length"] and sum(criteria.values()) >= 3:
        strength = "strong"
    elif criteria["length"]:
        strength = "moderate"
    elif criteria["lowercase"] or criteria["digit"]:
        strength = "weak"
    else:
        strength = "very_weak"

    return strength, crack_time[strength]


def generate_password(strength):
    # Define character sets
    lowercase = string.ascii_lowercase
    uppercase = string.ascii_uppercase
    digits = string.digits
    special = string.punctuation

    # Generate password based on strength
    if strength == "moderate":
        chars = lowercase + uppercase + digits
        length = 10
    elif strength == "strong":
        chars = lowercase + uppercase + digits + special
        length = 12
    else:  # very_strong or fallback
        chars = lowercase + uppercase + digits + special
        length = 16

    return ''.join(random.choices(chars, k=length))


def sha256_hash(password):
    return hashlib.sha256(password.encode('utf-8')).hexdigest()


if __name__ == "__main__":
    while True:
        option = input("\nChoose an option:\n1 - Check password strength\n2 - Generate a password\n3 - Exit\nYour choice: ")

        if option == "1":
            password = input("Enter the password to check its strength: ")
            strength, crack_time = password_strength(password)
            hashed_password = sha256_hash(password)

            print(f"Password strength: {strength}")
            print(f"Time to crack: {crack_time}")
            print(f"Hashed password (SHA256): {hashed_password}")

            if strength in ["very_weak", "weak"]:
                regenerate = input("Your password is weak. Generate a new one? (y/n): ")
                if regenerate.lower() == "y":
                    desired_strength = input("Enter desired strength (moderate, strong, very_strong): ")
                    new_password = generate_password(desired_strength)
                    print("New password:", new_password)
                    print("Hashed password (SHA256):", sha256_hash(new_password))

        elif option == "2":
            desired_strength = input("Enter desired strength (moderate, strong, very_strong): ")
            new_password = generate_password(desired_strength)
            print("Generated password:", new_password)

            if input("Do you want to hash it with SHA256? (y/n): ").lower() == "y":
                print("Hashed password:", sha256_hash(new_password))
            else:
                print("Hashing skipped.")

        elif option == "3":
            print("Goodbye!")
            break

        else:
            print("Invalid option. Please enter 1, 2, or 3.")
