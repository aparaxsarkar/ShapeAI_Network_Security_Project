import hashlib
text = input("Enter string data: ")
hash_text = hashlib.md5(text.encode()).hexdigest()
print ("MD5: " + hash_text)
