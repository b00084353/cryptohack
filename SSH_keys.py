from Crypto.PublicKey import RSA

pubfile = open("bruce_rsa_6e7ecd53b443a97013397b1a1ea30e14.pub", "r")
key = RSA.importKey(pubfile.read())
#print(key.publickey)

print(key)
print(type("key"))
print(f"Modulus: {key.publickey}")

