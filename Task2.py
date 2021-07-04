import hashlib

# asking for input string
text = input("Enter string data: ")

# using SHA-256 algorithm after converting to UTF-8
sha256_hash = hashlib.sha256(text.encode()).hexdigest()
print ("\nSHA-256: " + sha256_hash + "\n")

# using SHA-3-256 algorithm after converting to UTF-8
sha3_256_hash = hashlib.sha3_256(text.encode()).hexdigest()
print ("SHA-3-256: " + sha3_256_hash + "\n")

# using BLAKE2B algorithm after converting to UTF-8
blake2b_hash = hashlib.blake2b(text.encode()).hexdigest()
print ("BLAKE2B: " + blake2b_hash + "\n")
