import hashlib
import os

salt = os.urandom(32)
password = input("Enter string data: ")

key = hashlib.pbkdf2_hmac('sha256',password.encode(),salt,1000)
# hash digest algorithm, UTF-8 form, salt, 1000 iterations

print("\nDone salting with a 1000 iterations")
