import hashlib

# asking for input string
text = input("Enter string data: ")

# using MD5 algorithm after converting to UTF-8
md5_hash = hashlib.md5(text.encode()).hexdigest()
print ("MD5: " + md5_hash)
