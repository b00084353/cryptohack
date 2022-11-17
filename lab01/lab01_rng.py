a = 2175143
x = 3553
c = 10653
m = 1000000

for i in range(0,5):
    seq = (a*x+c) % m
    x = seq
    print(seq)
