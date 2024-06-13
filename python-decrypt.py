from cryptography.hazmat.primitives.ciphers import Cipher, algorithms, modes
from cryptography.hazmat.backends import default_backend
from cryptography.hazmat.primitives import hashes
from cryptography.hazmat.primitives.kdf.pbkdf2 import PBKDF2HMAC
import base64
import pyperclip
# import sys
from getpass import getpass
import re

# spam = pyperclip.paste()
# print('1.spam:', spam)

completed = "8Drk6Sf7lqGBzb3vviMccA==mVW11IWfiksmtBT0o0O1FQ=="

# Decoded base64 IV and ciphertext
# Qitado el b'
base64_iv = "DH9kNHdUHIxkDRbdoK3Uag=="
base64_ciphertext = "3Ub+2QFHGJ+QObZz4eUGJHi9z7l8VmYlUxc1bYuZ6g/vFzMLebztsSaUbSPxmj0Yh+HYn5Y+Gyv6tYIEfYUskW2s4o/BPR8K1Kb7/buy4jg="


# base64_iv = "8Drk6Sf7lqGBzb3vviMccA=="
# base64_ciphertext = "hYXTgWS4cnRDgwMLmrez3XFrfYmKiQX+3J8+wZZfJFiQJxlUBdSQ4Ql6D78KNl/M3/6HY95GxKtGxusHRt9DBd4ysJRmCWJmAaEj7I7sKCM="
# completed = "8Drk6Sf7lqGBzb3vviMccA==hYXTgWS4cnRDgwMLmrez3XFrfYmKiQX+3J8+wZZfJFiQJxlUBdSQ4Ql6D78KNl/M3/6HY95GxKtGxusHRt9DBd4ysJRmCWJmAaEj7I7sKCM="

# base64_iv = "8Drk6Sf7lqGBzb3vviMccA=="

# {
# while len(base64_ciphertext) % 4 != 0:
#     base64_ciphertext += '='
# }
# print("base64_ciphertext:", base64_ciphertext)

# Decode base64 strings back to binary data
iv = base64.b64decode(base64_iv)
ciphertext = base64.b64decode(base64_ciphertext)
# print("ciphertext:" + str(ciphertext))

# Your passphrase
# passphrase = b'admin'
passphrase = bytes(getpass(), "utf-8")
print(passphrase)

# Generate a salt (usually done once and stored securely)
salt = b'\xc3\x17\xfe/7\x1a\xf0\xfa\x1d\xdb\x99V\xdbp\x84\x81'
# convert string to bytes

# Derive the key using PBKDF2 with the specified passphrase and salt
kdf = PBKDF2HMAC(
    algorithm=hashes.SHA256(),
    length=12,  # 12 bytes key length (same as used during encryption)
    salt=salt,
    iterations=100000,  # Same number of iterations used during encryption
    backend=default_backend()
)
key = base64.urlsafe_b64encode(kdf.derive(passphrase))

# Decrypt the ciphertext using AES-256-CBC
cipher = Cipher(algorithms.AES(key), modes.CBC(iv), backend=default_backend())
decryptor = cipher.decryptor()
decrypted_data = decryptor.update(ciphertext) + decryptor.finalize()
print("decrypted_data:", decrypted_data)

# unpadded_data = unpad_data(decrypted_data)
pad_length = decrypted_data[-1]
data = re.sub("^b'|'", "", decrypted_data.decode()).replace("\\r\\n", "\n")
unpadded_data = data[:-pad_length]

# Unpad the decrypted data
# print('unpadded_data:', unpadded_data)
pyperclip.copy(unpadded_data)
spam = pyperclip.paste()
# print('spam:', spam)
print("File content encrypt, you can paste the resutl in a new file")
