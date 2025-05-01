# Schield-CRYPT 🔐

**Schield-CRYPT** is a Python-based encryption tool that leverages **AES-GCM** for encrypting and decrypting messages. It uses **PBKDF2** for key derivation, ensuring strong password-based encryption. The tool features secure password validation, logging, and supports storing encrypted data in files for easy access.

## 🚀 Features

- **AES-GCM Encryption**: AES encryption in GCM mode, ensuring both confidentiality and integrity.
- **PBKDF2 Key Derivation**: Strong password-based key derivation to generate AES keys.
- **Password Validation**: Secure password requirements — at least 16 characters, including uppercase, digits, and symbols.
- **File Saving**: Option to save encrypted data and salt to a JSON file.
- **Logging**: Detailed logs for encryption/decryption actions, including error handling.
- **Base64 Encoding**: Encrypted data is base64 encoded for easier storage and sharing.

## 🖥️ Requirements

To use **Schield-CRYPT**, you'll need Python 3.x and the following libraries:

- `pycryptodome`
- `termcolor`

Install the dependencies using `pip`:

```bash
pip install pycryptodome termcolor

🔑 Usage

Encrypting a Message

1. Run the script:

python encryption_tool.py


2. Choose to encrypt a message when prompted.


3. Enter a strong password (at least 16 characters, with uppercase, numbers, and symbols).


4. Input the text you want to encrypt.


5. The encrypted message and salt will be displayed, with the option to save them to a file.



Decrypting a Message

1. Run the script:

python encryption_tool.py


2. Choose to decrypt a message when prompted.


3. Enter the encrypted text (base64 encoded) and the salt (in hex format).


4. The decrypted message will be displayed if the decryption is successful.



🛡️ Password Requirements

For maximum security, the password must meet the following criteria:

At least 16 characters long.

Contains at least one uppercase letter.

Contains at least one number.

Contains at least one special character from !@#$%^&*()_-+=<>?.


⚠️ Error Handling

The script uses custom exceptions for encryption and decryption errors:

EncryptionError: Raised if there is an issue during encryption (e.g., key derivation failure).

DecryptionError: Raised if the decryption process fails or if the authentication tag is invalid.


🎬 Example Output

Encrypting Data

=== Welcome to the Encryption Tool ===
----------------------------------------
Do you want to Encrypt or Decrypt a message? (e/d): e
Enter your password (at least 16 characters, with uppercase, numbers, and symbols): P@ssw0rd123!
Enter the text to encrypt (or type 'exit' to quit): Hello, world!

Encrypted text (base64): <encrypted_base64_string>
Salt (hex): <salt_in_hex>
Do you want to save the encrypted data to a file? (y/n): y
Encrypted data saved to encrypted_data_<random_hex>.json

Decrypting Data

=== Welcome to the Encryption Tool ===
----------------------------------------
Do you want to Encrypt or Decrypt a message? (e/d): d
Enter the encrypted text to decrypt: <encrypted_base64_string>
Enter the salt (hex format): <salt_in_hex>

Decrypted text: Hello, world!

📋 Logging

All encryption and decryption actions, as well as errors, are logged into the encryption.log file. This provides transparency and helps track any issues during the process.

🤝 Contributing

Contributions are welcome! Please fork the repository and submit a pull request with your changes. Make sure to follow best practices for security and clean code.

📜 License

This project is licensed under the MIT License - see the LICENSE file for details.

### Key Changes:
- Added relevant **emojis** for sections like features, error handling, contributing, and logging.
- Structured the content clearly and professionally to ensure easy readability on GitHub.
- **Formatting** is consistent with GitHub markdown standards.
