# 유클리드 호제법 사용하여 최대 공약수 확인
def gcd(a, b):
    while b:
        mod = b
        b = a % b
        a = mod
    return a

N = int(input())
n_list = list(map(str, input().split()))

n = int(eval('*'.join(n_list)))


M = int(input())
m_list = list(map(str, input().split()))

m = int(eval('*'.join(m_list)))

print(str(gcd(n, m))[-9:])

