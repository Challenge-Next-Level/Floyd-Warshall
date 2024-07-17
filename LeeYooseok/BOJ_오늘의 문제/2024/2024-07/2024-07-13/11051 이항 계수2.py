import sys

def factorial(x):  # 팩토리얼
    res = 1
    for i in range(1, x+1):
        res *= i
    return res

input = sys.stdin.readline

N, K = map(int, input().split())

result = factorial(N) // (factorial(K) * factorial(N-K))
total = result % 10007

print(total)