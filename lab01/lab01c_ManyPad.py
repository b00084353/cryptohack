import base64

str = "0f381a39fe6f41bd57c44646eacc3ecb2b695ae729ee174ac650ab0c92547a73b19ca7a24d40162bea9c0d1c2c1395678f6dec2ae8b4eaa449b1511507c3e06dd6c9c02c69c5eca4241d3f3585f44440ad011078381bacc075e4c3"
str_bytes = str.encode("ascii")

base64_bytes = base64.b64encode(str_bytes)
base64_string = base64_bytes.decode("ascii")

#print(str_bytes)
#print(base64_bytes)
#print(base64_string)
print(f"Encoded string: {base64_string}")
