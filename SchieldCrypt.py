import base64
import logging
import os
import json
from typing import Tuple
from Crypto.Cipher import AES
from Crypto.Protocol.KDF import PBKDF2
from Crypto.Util.Padding import unpad
from Crypto.Random import get_random_bytes
from termcolor import colored
import secrets

logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s',
    handlers=[
        logging.FileHandler("encryption.log"),
        logging.StreamHandler()
    ]
)

AES_KEY_SIZE = 32
KDF_ITERATIONS = 600000
NONCE_SIZE = 12
MIN_PASSWORD_LENGTH = 16

class EncryptionError(Exception):
    pass

class DecryptionError(Exception):
    pass

class EncryptionTool:
    def __init__(self, password: str, salt: bytes = None):
        self._validate_password(password)
        self.password = password.encode('utf-8')
        self.salt = salt or secrets.token_bytes(16)
        self.key = self._derive_key()

    def _validate_password(self, password: str):
        if len(password) < MIN_PASSWORD_LENGTH:
            raise ValueError(f"Password must be at least {MIN_PASSWORD_LENGTH} characters long.")
        
        if not any(c.isupper() for c in password):
            raise ValueError("Password should contain at least one uppercase letter.")
        
        if not any(c.isdigit() for c in password):
            raise ValueError("Password should contain at least one number.")
        
        if not any(c in "!@#$%^&*()_-+=<>?" for c in password):
            raise ValueError("Password should contain at least one symbol for better security.")

    def _derive_key(self) -> bytes:
        try:
            key = PBKDF2(self.password, self.salt, dkLen=AES_KEY_SIZE, count=KDF_ITERATIONS)
            return key
        except Exception as e:
            logging.error(f"Error in key derivation: {e}")
            raise EncryptionError("Error in key derivation.")

    def encrypt_string(self, plaintext: str) -> Tuple[str, bytes]:
        try:
            plaintext_bytes = plaintext.encode('utf-8')
            nonce = secrets.token_bytes(NONCE_SIZE)
            cipher = AES.new(self.key, AES.MODE_GCM, nonce=nonce)
            ciphertext, tag = cipher.encrypt_and_digest(plaintext_bytes)

            encrypted_data = nonce + tag + ciphertext
            encrypted_b64 = base64.b64encode(encrypted_data).decode('utf-8')
            return encrypted_b64, self.salt
        except Exception as e:
            logging.error(f"Error in string encryption: {e}")
            raise EncryptionError("Error in string encryption.")

    def decrypt_string(self, encrypted_data: str, salt: bytes) -> str:
        try:
            self.salt = salt
            self.key = self._derive_key()

            encrypted_data = base64.b64decode(encrypted_data)

            nonce = encrypted_data[:NONCE_SIZE]
            tag = encrypted_data[NONCE_SIZE:NONCE_SIZE + 16]
            ciphertext = encrypted_data[NONCE_SIZE + 16:]

            cipher = AES.new(self.key, AES.MODE_GCM, nonce=nonce)
            plaintext_bytes = cipher.decrypt_and_verify(ciphertext, tag)

            plaintext = plaintext_bytes.decode('utf-8')
            return plaintext
        except ValueError as e:
            logging.error("Error: invalid authentication tag or decryption failure. Data might have been tampered with.")
            raise DecryptionError("Invalid authentication tag or decryption failure.")
        except Exception as e:
            logging.error(f"Error in string decryption: {e}")
            raise DecryptionError("Error in string decryption.")

def choose_action():
    while True:
        action = input(colored("Do you want to Encrypt or Decrypt a message? (e/d): ", "yellow")).strip().lower()
        if action in ['e', 'encrypt']:
            return 'encrypt'
        elif action in ['d', 'decrypt']:
            return 'decrypt'
        else:
            print(colored("Invalid input. Please enter 'e' for Encrypt or 'd' for Decrypt.", "red"))

def get_password() -> str:
    while True:
        password = input(colored("Enter your password (at least 16 characters, with uppercase, numbers, and symbols): ", "yellow")).strip()
        try:
            tool = EncryptionTool(password=password)
            return password
        except ValueError as e:
            print(colored(f"Error: {e}", "red"))
            continue

def print_separator():
    print(colored("=" * 40, "cyan"))

def get_valid_response(prompt: str) -> str:
    while True:
        response = input(colored(prompt, "yellow")).strip().lower()
        if response in ['y', 'yes', 'n', 'no']:
            return response
        else:
            print(colored("Invalid input. Please enter 'y' for Yes or 'n' for No.", "red"))

def save_encrypted_data_to_file(encrypted_data: str, salt: bytes):
    save_choice = get_valid_response("\nDo you want to save the encrypted data to a file? (y/n): ")
    if save_choice in ['y', 'yes']:
        filename = f"encrypted_data_{secrets.token_hex(8)}.json"
        with open(filename, "w") as f:
            json.dump({"encrypted_text": encrypted_data, "salt": salt.hex()}, f)
        print(f"Encrypted data saved to {filename}")
    else:
        print(colored("Encrypted data was not saved.", "red"))

def print_triangle():
    print(colored("""
       /\\
      /  \\    𝘾𝙞𝙥𝙝𝙚𝙧 
     /    \\
    /______\\
   /\\      /\\   𝙎𝙦𝙪𝙞𝙙
  /  \\    /  \\
 /    \\  /    \\
/______\\/______\\
""", "green"))

def main():
    print(colored("=====================================", 'cyan'))
    print(colored("[×] SHIELD-CRYPT Tool by 𝘾𝙞𝙥𝙝𝙚𝙧 𝙎𝙦𝙪𝙞𝙙 ", 'red'))
    print(colored("[×] Use responsibly!", 'yellow'))
    print(colored("=====================================", 'cyan'))

    print(colored("=== Welcome to the Encryption Tool ===", "green"))
    print_triangle()  # Display the ASCII triangle
    print_separator()
    
    action = choose_action()
    
    password = get_password()
    tool = EncryptionTool(password=password)
    
    if action == 'encrypt':
        while True:
            text = input(colored("Enter the text to encrypt (or type 'exit' to quit): ", "yellow")).strip()
            if text.lower() == 'exit':
                print(colored("Exiting the Encryption Tool. Goodbye!", "red"))
                break
            
            try:
                encrypted_text, salt = tool.encrypt_string(text)
                print(f"\n{colored('Encrypted text (base64):', 'blue')} {colored(encrypted_text, 'yellow')}")
                print(f"{colored('Salt (hex):', 'blue')} {colored(salt.hex(), 'yellow')}")
                
                save_encrypted_data_to_file(encrypted_text, salt)
                
            except EncryptionError as e:
                print(colored(f"Error: {e}", "red"))
    elif action == 'decrypt':
        encrypted_text = input(colored("Enter the encrypted text to decrypt: ", "yellow")).strip()
        salt_hex = input(colored("Enter the salt (hex format): ", "yellow")).strip()
        salt = bytes.fromhex(salt_hex)
        
        try:
            decrypted_text = tool.decrypt_string(encrypted_text, salt)
            print(f"{colored('Decrypted text:', 'green')} {decrypted_text}")
        except DecryptionError as e:
            print(colored(f"Error: {e}", "red"))

if __name__ == "__main__":
    main()