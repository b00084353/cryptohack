import binascii
import base64

hexval = "72bca9b68fc16ac7beeb8f849dca1d8a783e8acf9679bf9269f7bf"
byteval = bytes.fromhex(hexval)
baseval= base64.b64encode(byteval)

print(baseval)