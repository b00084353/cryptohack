import binascii
from binascii import hexlify
from Crypto.Util.number import *

key1 = "73626960647f6b206821204f21254f7d694f7624662065622127234f726927756d"
str1 = "StringOfText"
intval = 83116114105103


#Convert hex string to ascii characters
key1bytes = bytes.fromhex(key1)
print("HEX string in bytes", key1bytes)
#Converts hex string to array of ascii decimal values
key1array = [o for o in bytes.fromhex(key1)]
print("HEX string as decimal array", key1array)

#Convert string to ascii hex values is a 2 step process.
#1. use .encode to get byte representation of string
#2. use  .hex() to get ascii hex values
strhex = str1.encode('utf-8')
print("BYTE representation of string", strhex)
print("Decimal representation of string", strhex.hex())

intvalasbyte = (long_to_bytes(intval))
print(intvalasbyte)
