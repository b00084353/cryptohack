from pwn import xor

key = "crypto{}"
enc = "0e0b213f26041e480b26217f27342e175d0e070a3c5b103e2526217f27342e175d0e077e263451150104"

enc1bytes = bytes.fromhex(enc)
print(enc1bytes)
print(len(enc1bytes))
print()
#From the clue given we can use crypto{} as a possible key
ans = xor(enc1bytes[:8], "crypto{}")
print(ans)

#ans returned "myXORke5" but this gave the wrong flag.
#changing ans to "myXORkey" and extending to the same length as the message(42) gave the correct flag

extans = "myXORkeymyXORkeymyXORkeymyXORkeymyXORkeymyX"

flag = xor(enc1bytes, extans)
print(flag)

