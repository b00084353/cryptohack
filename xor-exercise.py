from codecs import unicode_escape_encode


lst = []
cypher = []
rot = 13
input = "label"
for c in input:
    x=ord(c)
    lst.append(x)
    #print(ord(c), sep='', end=' ', flush=True)
print(lst)

for e in lst:
    cypher.append(e ^ rot)
print(cypher)

for m in cypher:
    print(chr(m), sep='', end='', flush=True)
