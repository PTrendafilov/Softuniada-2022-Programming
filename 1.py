import math

def find_gcd_lcm_sum(n, m):
    gcd = math.gcd(n, m)
    lcm = (n * m) // gcd
    return gcd + lcm

n = int(input())
m = int(input())
result = find_gcd_lcm_sum(n, m)
print(result)
