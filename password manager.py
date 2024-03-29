import json, hashlib, getpass, os, pyperclip, sys
from cryptography.fernet import Fernet

# Function for Hashing the Master Password.
def hash_password(password):
   sha256 = hashlib.sha256()
   sha256.update(password.encode())
   return sha256.digest()

# Function for Generating a Key using Master Password and Salt.
def generate_key(password, salt):
   return hash_password(password + salt)

# Function for Encrypting a Password using a Key.
def encrypt_password(password, key):
   f = Fernet(key)
   return f.encrypt(password.encode()).decode()

# Function for Decrypting a Password using a Key.
def decrypt_password(password, key):
   f = Fernet(key)
   return f.decrypt(password.encode()).decode()

# Function for