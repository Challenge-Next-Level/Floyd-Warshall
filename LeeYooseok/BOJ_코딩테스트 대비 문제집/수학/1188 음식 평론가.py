def gcd(a,b):
    while b:
        mod = b
        b = a % b
        a = mod
    return a

N, M = map(int, input().split())

