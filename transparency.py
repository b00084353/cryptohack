from Crypto.PublicKey import RSA

pubfile = open("transparency.pem", "r")
key = RSA.importKey(pubfile.read())

print(key)
print(type("key"))
print(f"Modulus: {key.exportKey(format='OpenSSH')}")

