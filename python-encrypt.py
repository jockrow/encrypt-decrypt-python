# TIP: Forma sencilla
# https://www.reddit.com/r/neovim/comments/1c67gbv/decrypting_editing_and_encrypting_again_a_text/?%24deep_link=true&correlation_id=b1979da9-a76a-43c2-adbc-7bd7d5f79597&post_fullname=t3_1c67gbv&post_index=0&ref=email_digest&ref_campaign=email_digest&ref_source=email&utm_content=post_title&%243p=e_as&_branch_match_id=1251507120854258061&utm_medium=Email+Amazon+SES&_branch_referrer=H4sIAAAAAAAAA22Q0WrDMAxFvyZ7S7LGbU0GZQzGfsMotpqKObJxlKb7%2Bynr1qeBja%2FO5UrCF5E8v7RtwRBIGsi5icSfrcmvVbc3%2BYQO5ieVqdBIDNEtJZ4uW6oyb1X3oWdd1%2BY379OkoOhlTFfaCkUTsswqd%2F5ox%2BGqKqAvX1mIR4ea217g4JAfGEYgduAEb%2BLOFLdRRqcdun1AzG7bsjLvUhasuqNPpWAEocSOgvJh19s%2BQF%2BDPUK9N76rIQy%2BtkOw4XC2%2FaG3mstp1u5LjAwTbu2Meyx5N4kD3tR5VlDwrAonoOgCjTjLHToPUwYa%2BX93Tkvx%2BOcpXGRyPrHotyj9GSMkEb8B667PkY0BAAA%3D
from cryptography.hazmat.primitives.ciphers import Cipher, algorithms, modes
from cryptography.hazmat.backends import default_backend
from cryptography.hazmat.primitives import hashes
from cryptography.hazmat.primitives.kdf.pbkdf2 import PBKDF2HMAC
import base64
import os
import pyperclip
from getpass import getpass
# import re


def pad_data(data, block_size):
    pad_length = block_size - (len(data) % block_size)
    padding = bytes([pad_length] * pad_length)
    return data + padding


# Your passphrase and data to encrypt (multiple lines)
# passphrase = b'any_password'
# passphrase = input("Enter password: ")
passphrase = bytes(getpass(), "utf-8")
# data = 'any code'
data = """Line 1 of the data.
    Line 2 of the data.
    Line 3 of the data.
"""
# file_path = './testToEncrypt.txt'
# with open(file_path, 'rb') as file:
#     data = str(file.read())
# # data = data.replace("\\r\\n", "\n")
# # print("typedata:", type(data))
# # print("data:" + data)
# # # data = re.sub("^b'|'", "", data)
# # # data = str(data).encode()
# # # data = data.()
# data = pyperclip.paste()
print("data:", data)

# Generate a random 16-byte IV
iv = os.urandom(16)

# Pad the data to be a multiple of the block size
padded_data = pad_data(data.encode("utf-8"), 16)

# Generate a salt (usually done once and stored securely)
salt = b"\xc3\x17\xfe/7\x1a\xf0\xfa\x1d\xdb\x99V\xdbp\x84\x81"
# # Generate a salt (usually done once and stored securely)
# salt = os.urandom(16)
# print salt

# Derive a key using PBKDF2 with the specified passphrase and salt
kdf = PBKDF2HMAC(
    algorithm=hashes.SHA256(),
    length=12,  # 12 bytes key length
    salt=salt,
    iterations=100000,  # You can adjust the number of iterations for security
    backend=default_backend(),
)
key = base64.urlsafe_b64encode(kdf.derive(passphrase))

# Encrypt the data using AES-256-CBC
cipher = Cipher(algorithms.AES(key), modes.CBC(iv), backend=default_backend())
encryptor = cipher.encryptor()
ciphertext = encryptor.update(padded_data) + encryptor.finalize()

# Base64 encode the IV and ciphertext for easy transmission/storage
# base64_iv = base64.b64encode(iv).decode('utf-8')
base64_iv = "8Drk6Sf7lqGBzb3vviMccA=="
base64_ciphertext = base64.b64encode(ciphertext).decode("utf-8")

# print('base64_iv = "' + base64_iv + '"')
# print('base64_ciphertext = "' + base64_ciphertext + '"')
pyperclip.copy(base64_iv + base64_ciphertext)
completed = pyperclip.paste()
# print('completed = "' + completed + '"')
print("File content encrypt, you can paste the resutl in a new file")
