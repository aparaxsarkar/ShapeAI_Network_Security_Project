import hashlib
text = input("Enter string data: ")
md5_hash = hashlib.md5(text.encode()).hexdigest()
print ("MD5: " + md5_hash)
