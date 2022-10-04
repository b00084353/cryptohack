from pwn import xor

key = "crypto{}"
enc = "0e0b213f26041e480b26217f27342e175d0e070a3c5b103e2526217f27342e175d0e077e263451150104"

enc1bytes = bytes.fromhex(enc)
print(enc1bytes)
print()
ans = xor(enc1bytes[:8], "crypto{}")
print(ans)

