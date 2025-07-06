# Password-Strength-Checker-and-Generator

A Python-based tool built in Visual Studio Code (VS Code) that checks password strength, generates secure passwords, and applies hashing algorithms (like SHA-256) to securely transform passwords for storage or validation.

This project promotes password security best practices by:

Encouraging users to choose stronger passwords

Demonstrating how passwords can be safely hashed before storage

✅ Key Features
🔍 Password Strength Checker
Checks for:

✅ Minimum length

✅ Uppercase & lowercase letters

✅ Digits

✅ Special symbols

Categorizes strength as: Weak, Medium, or Strong

🔐 Secure Password Generator
Generates random passwords with:

Custom length

Toggle options: letters, numbers, symbols

Strong entropy

🔒 Password Hashing
Uses Python’s hashlib module to hash passwords using:

SHA-256 (default)

Demonstrates how to:

Safely store passwords in a hashed format

Avoid storing plaintext passwords

🧰 Tech Stack
Language: Python 3.x

Editor: Visual Studio Code

Libraries Used:

hashlib – for hashing passwords

random, string – for generation
