import hashlib
text = input("Enter string data: ")
hash_text = hashlib.md5(text.encode())
md5_text = hash_text.hexdigest()
print (md5_text)
