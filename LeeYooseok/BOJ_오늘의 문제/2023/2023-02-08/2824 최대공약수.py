# 최대 공약수 확인
def gcd(a, b):
    while b > 0:
        a, b = b, a % b
    return a


N = int(input())
A_nums = list(input().split())
A = int(eval("*".join(A_nums)))

M = int(input())
B_nums = list(input().split())
B = int(eval("*".join(B_nums)))

print(str(gcd(A, B))[-9:])