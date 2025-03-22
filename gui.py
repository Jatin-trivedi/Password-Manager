import os
import json
from cryptography.fernet import Fernet
from PyQt6.QtWidgets import (
    QApplication, QWidget, QVBoxLayout, QPushButton, QLineEdit,
    QTextEdit, QMessageBox, QInputDialog
)

class PasswordManager(QWidget):
    def __init__(self):
        super().__init__()
        self.init_ui()
        if not os.path.exists("secret.key"):
            self.generate_key()

    def init_ui(self):
        self.setWindowTitle("Password Manager")
        self.setGeometry(100, 100, 600, 500)
        layout = QVBoxLayout()

        self.service_input = QLineEdit(self)
        self.service_input.setPlaceholderText("Enter Service Name")
        self.service_input.setFixedHeight(40)
        layout.addWidget(self.service_input)

        self.username_input = QLineEdit(self)
        self.username_input.setPlaceholderText("Enter Username")
        self.username_input.setFixedHeight(40)
        layout.addWidget(self.username_input)

        self.password_input = QLineEdit(self)
        self.password_input.setPlaceholderText("Enter Password")
        self.password_input.setEchoMode(QLineEdit.EchoMode.Password)
        self.password_input.setFixedHeight(40)
        layout.addWidget(self.password_input)

        self.save_button = QPushButton("Save Password")
        self.save_button.setFixedHeight(40)
        self.save_button.clicked.connect(self.save_password)
        layout.addWidget(self.save_button)

        self.list_button = QPushButton("List Stored Services")
        self.list_button.setFixedHeight(40)
        self.list_button.clicked.connect(self.list_services)
        layout.addWidget(self.list_button)

        self.retrieve_button = QPushButton("Retrieve Password")
        self.retrieve_button.setFixedHeight(40)
        self.retrieve_button.clicked.connect(self.retrieve_password)
        layout.addWidget(self.retrieve_button)

        self.delete_button = QPushButton("Delete Password")
        self.delete_button.setFixedHeight(40)
        self.delete_button.clicked.connect(self.delete_password)
        layout.addWidget(self.delete_button)

        self.output = QTextEdit()
        self.output.setReadOnly(True)
        self.output.setMinimumHeight(150)
        layout.addWidget(self.output)

        self.setLayout(layout)

    def generate_key(self):
        key = Fernet.generate_key()
        with open("secret.key", "wb") as key_file:
            key_file.write(key)

    def load_key(self):
        return open("secret.key", "rb").read()

    def encrypt_password(self, password, key):
        return Fernet(key).encrypt(password.encode())

    def decrypt_password(self, encrypted_password, key):
        return Fernet(key).decrypt(encrypted_password).decode()

    def save_password(self):
        service = self.service_input.text()
        username = self.username_input.text()
        password = self.password_input.text()

        if not service or not username or not password:
            QMessageBox.warning(self, "Warning", "All fields are required!")
            return

        key = self.load_key()
        encrypted_password = self.encrypt_password(password, key)
        data = {service: {"username": username, "password": encrypted_password.decode()}}

        if os.path.exists("passwords.json"):
            with open("passwords.json", "r") as file:
                try:
                    passwords = json.load(file)
                except json.JSONDecodeError:
                    passwords = {}
            passwords.update(data)
        else:
            passwords = data

        with open("passwords.json", "w") as file:
            json.dump(passwords, file, indent=4)
        QMessageBox.information(self, "Success", "Password saved successfully!")

if __name__ == "__main__":
    app = QApplication([])
    window = PasswordManager()
    window.show()
    app.exec()
