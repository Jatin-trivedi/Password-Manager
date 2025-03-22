# Password-Manager

**📌 Overview**

This is a secure password manager built with Python and PyQt6. It allows users to store, retrieve, list, and delete passwords securely using encryption with cryptography.fernet. The project features a modern and intuitive Graphical User Interface (GUI) using PyQt6, providing a seamless user experience.

**✨ Features**

**🔐 Secure Encryption:** Uses Fernet encryption to protect stored passwords.

**💾 Save Passwords:** Store credentials securely in an encrypted JSON file.

**🔍 Retrieve Passwords:** Decrypt and view saved credentials.

**📜 List Stored Services:** Display all stored accounts.

**❌ Delete Passwords:** Remove credentials for a specific service.

**🖥️ Modern GUI:** Interactive and sleek UI built with PyQt6.

**🛠 Cross-Platform Compatibility:** Works on Windows, macOS, and Linux.

### 📂 Project Structure

📦 Password-Manager
 ├── 📜 main.py           # Main application file
 ├── 📜 gui.py            # GUI implementation
 ├── 📜 secret.key       # Encryption key (Generated at runtime)
 ├── 📜 passwords.json   # Stored passwords (Encrypted)
 ├── 📜 README.md        # Project Documentation

### 🚀 Installation

**Prerequisites**

- **Python 3.x** installed

- `pip` installed

**Install Dependencies**

Run the following command to install required libraries:

`pip install PyQt6`

`pip install cryptography`

`pip install rich`


🎮 **Usage**

Run the password manager:

`python main.py`

### GUI Options

1. **Save Password:** Enter a service, username, and password to store securely.

2. **Retrieve Password:** Select a service to view stored credentials.

3. **List Services:** View all stored services in a table format.

4. **Delete Password:** Remove a saved password.

5. **Exit:** Close the application.

**🔒 Security Notes**

- The **encryption key** (`secret.key`) is auto-generated if not found.

- Deleting `secret.key` will make decryption of stored passwords **impossible.**

- Never share the `secret.key` file with anyone.

- Passwords are stored in an encrypted format, making them unreadable without decryption.

📜 **License**

This project is open-source and available under the **MIT License.**

🙌 **Contributing**

Pull requests and suggestions are welcome! Feel free to fork this project and enhance it. 🎉

📞 **Contact**

For any queries, reach out via [GitHub Issues](https://github.com/your-username/password-manager/issues).

> Write something...
