a = 66528
b = 52920

factorsa = []
factorsb = []

for i in range(1, int(a/2) + 1):
    if a % i == 0:
        factorsa.append(i)

for i in range(1, int(b/2) + 1):
    if b % i == 0:
        factorsb.append(i)

print("Factors of a are ", factorsa)
print("Factors of B are", factorsb)

GCD = max(set(factorsa).intersection(factorsb))
print("GCD of A and B is", GCD)

