import math
from egcd import egcd

p = 26513
q = 32321

gcd = math.gcd(p,q)
print("GCD of p and q is ", gcd)

extended = egcd(p,q)
print("The GCD, and multipliers for the extended algorithim are ", extended)
