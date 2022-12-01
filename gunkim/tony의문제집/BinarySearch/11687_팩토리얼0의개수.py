# 수학적 규칙을 찾아내는 것이 더 핵심인 문제 같음, 어려웠음
m = int(input())

left, right = 1, m*5


def divide_five(num):
    result = 0
    while num // 5:
        result += num // 5
        num //= 5
    return result


answer = -1
while left <= right:
    mid = (left + right) // 2
    countFive = divide_five(mid)
    if countFive < m:
        left = mid + 1
    else:
        right = mid - 1
        answer = mid

if divide_five(answer) == m:
    print(answer)
else:
    print(-1)