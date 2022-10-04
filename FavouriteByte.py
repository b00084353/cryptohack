KEY1 = "73626960647f6b206821204f21254f7d694f7624662065622127234f726927756d"

key1bytes = bytes.fromhex(KEY1)

for i in range(256):
    answer = [i ^ j for j in key1bytes]
    check = "".join(chr(o) for o in answer)
    if check.startswith("cry"):
        break
print(check)
