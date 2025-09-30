from cryptography.fernet import Fernet
key = Fernet.generate_key()
cipher = Fernet(key)
encrypted = cipher.encrypt(b"My secret password")
print(f"Зашифровано: {encrypted}")
