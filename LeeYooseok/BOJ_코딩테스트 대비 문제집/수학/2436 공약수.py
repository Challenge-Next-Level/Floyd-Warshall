# https://alpyrithm.tistory.com/148

import sys

input = sys.stdin.readline

# 최대 공약수
def gcd(a, b):
    while b:
        mod = b
        b = a % b
        a = mod
    return a


A, B = map(int, input().split())
num1xnum2 = B // A  # 최소 공배수 / 최대 공약수 == num1 * num2

a, b = 1, num1xnum2
for i in range(1, num1xnum2 // 2 + 1):
    if num1xnum2 % i == 0:
        num1 = i
        num2 = num1xnum2 // num1

        if gcd(num1, num2) != 1:
            continue

        if a + b > num1 + num2:
            a = num1
            b = num2

print(a * A, b * A)