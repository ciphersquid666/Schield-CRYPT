# Schield-CRYPT 🔐

**Schield-CRYPT** is a Python-based encryption tool that leverages **AES-GCM** for secure encryption and decryption of messages. It uses **PBKDF2** for key derivation, ensuring robust password-based encryption. The tool includes secure password validation, detailed logging, and supports storing encrypted data in files for convenient access.

---

## 🚀 Features

- **AES-GCM Encryption**: Provides AES encryption in GCM mode, ensuring both confidentiality and integrity.
- **PBKDF2 Key Derivation**: Implements strong password-based key derivation for generating secure AES keys.
- **Password Validation**: Enforces secure password requirements — at least 16 characters, including uppercase letters, numbers, and symbols.
- **File Saving**: Allows saving encrypted data and salt in JSON files for easy storage and retrieval.
- **Logging**: Captures detailed logs for encryption and decryption actions, including error handling.
- **Base64 Encoding**: Encodes encrypted data in Base64 format for simplified storage and sharing.

---

## 🖥️ Requirements

To use **Schield-CRYPT**, ensure you have Python 3.x installed, along with the following libraries:

- `pycryptodome`
- `termcolor`

Install the required dependencies using `pip`:

```bash
pip install pycryptodome termcolor
```

---

## 🔑 Usage

### Encrypting a Message

1. Run the script using the command:
   ```bash
   python encryption_tool.py
   ```

2. Select encryption mode when prompted.

3. Enter a strong password (at least 16 characters, including uppercase letters, numbers, and symbols).

4. Provide the text you want to encrypt.

5. The tool will generate the encrypted message and salt, with an option to save them to a file.

### Decrypting a Message

1. Run the script using the command:
   ```bash
   python encryption_tool.py
   ```

2. Select decryption mode when prompted.

3. Provide the encrypted text (Base64 encoded) and the salt (in hexadecimal format).

4. The decrypted message will be displayed if the process is successful.

---

## 🛡️ Password Requirements

For maximum security, passwords must meet the following criteria:

- At least 16 characters long.
- Includes at least one uppercase letter.
- Includes at least one number.
- Includes at least one special character, such as: `!@#$%^&*()_-+=<>?`.

---

## ⚠️ Error Handling

The tool uses custom exceptions to handle errors:

- **EncryptionError**: Raised in case of issues during encryption (e.g., key derivation failure).
- **DecryptionError**: Raised if the decryption process fails or authentication tags are invalid.

---

## 🎬 Example Output

### Encrypting Data

```plaintext
=== Welcome to the Encryption Tool ===
----------------------------------------
Do you want to Encrypt or Decrypt a message? (e/d): e
Enter your password (at least 16 characters, with uppercase, numbers, and symbols): P@ssw0rd123!
Enter the text to encrypt (or type 'exit' to quit): Hello, world!

Encrypted text (base64): <encrypted_base64_string>
Salt (hex): <salt_in_hex>
Do you want to save the encrypted data to a file? (y/n): y
Encrypted data saved to encrypted_data_<random_hex>.json
```

### Decrypting Data

```plaintext
=== Welcome to the Encryption Tool ===
----------------------------------------
Do you want to Encrypt or Decrypt a message? (e/d): d
Enter the encrypted text to decrypt: <encrypted_base64_string>
Enter the salt (hex format): <salt_in_hex>

Decrypted text: Hello, world!
```

---

## 📋 Logging

All encryption and decryption actions, as well as errors, are logged into the `encryption.log` file. This ensures transparency and helps track any issues encountered during the process.

---

## 🤝 Contributing

Contributions are highly encouraged! To contribute:

1. Fork the repository.
2. Create a new branch for your changes.
3. Submit a pull request with a detailed explanation of your changes.

Ensure your contributions follow best practices for security and clean code.

---

## 📜 License

This project is licensed under the MIT License. See the `LICENSE` file for more details.