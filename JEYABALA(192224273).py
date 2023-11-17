from cryptography.fernet import Fernet
import getpass
import os

class FileEncryptor:
    def __init__(self, key=None):
        if key is None:
            key = Fernet.generate_key()
        self.key = key
        self.cipher_suite = Fernet(key)

    def encrypt(self, data):
        encrypted_data = self.cipher_suite.encrypt(data.encode())
        return encrypted_data

    def decrypt(self, encrypted_data):
        decrypted_data = self.cipher_suite.decrypt(encrypted_data)
        return decrypted_data.decode()

    def save_to_file(self, filename, data):
        encrypted_data = self.encrypt(data)
        with open(filename, 'wb') as file:
            file.write(encrypted_data)

    def read_from_file(self, filename):
        with open(filename, 'rb') as file:
            encrypted_data = file.read()
        return self.decrypt(encrypted_data)

def get_password():
    password = getpass.getpass("Enter password: ")
    return password

def main():
    filename = "secret_file.txt"

    password = get_password()
    key = Fernet.generate_key()

    encryptor = FileEncryptor(key)

    data = input("Enter the data to be saved in the file: ")

    encryptor.save_to_file(filename, data)
    print("File encrypted and saved successfully.")

    decrypted_data = encryptor.read_from_file(filename)
    print("Decrypted data from file:", decrypted_data)

if __name__ == "__main__":
    main()
