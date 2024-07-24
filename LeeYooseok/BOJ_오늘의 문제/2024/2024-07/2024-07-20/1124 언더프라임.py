# 어떤 수 X를 소인수분해 해서 구한 소수의 목록의 길이가 소수이면, 그 수를 언더프라임
# 1은 소수가 아님
import math

A, B = map(int, input().split())

is_prime = [True for _ in range(B + 1)]
is_prime[1] = False

for i in range(2, B + 1):
    if not is_prime[i]:
        continue

    for j in range(i * 2, B + 1, i):
        is_prime[j] = False


# 소인수 분해 -> 소인수 개수 확인
def count_prime(n):
    cnt = 0

    for k in range(2, int(math.sqrt(n) + 1)):
        while n % k == 0:  # 2 부터 차례로 나누다가, 나누어 떨어지면 그 수가 어차피 약수임
            cnt += 1
            n //= k

    if n != 1:  # 1은 소수가 아니므로, 1이 아닌 다른 수 이면, 소인수 1개 더 있음
        cnt += 1

    return cnt


answer = 0

for num in range(A, B + 1):
    if is_prime[count_prime(num)]:
        answer += 1

print(answer)
