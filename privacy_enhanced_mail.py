from Crypto.PublicKey import RSA

pemfile = open("privacy_enhanced_mail.pem", "r")
key = RSA.importKey(pemfile.read())
#key_decimal = int(key)
#print(key_decimal)
#key_der = key.publickey().exportKey("Der")

print(key)
print(type("key"))
print(f"RSA certificate modulus: {key.publickey}")

