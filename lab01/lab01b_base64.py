import base64

str = "cryptol"
str_bytes = str.encode("ascii")

base64_bytes = base64.b64encode(str_bytes)
base64_string = base64_bytes.decode("ascii")

#print(str_bytes)
#print(base64_bytes)
print(base64_string)