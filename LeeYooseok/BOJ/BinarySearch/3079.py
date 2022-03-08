import sys

n, m = map(int, sys.stdin.readline().split())

check = [int(sys.stdin.readline()) for _ in range(n)]

check.sort()

left, right = check[0], m*check[-1]
mid = 0
answer = right


def possible(time):
    total = 0
    for i in range(n):
        total += time // check[i]

    if total >= m:
        return True
    else:
        return False


while left <= right:
    mid = (left + right) // 2

    if possible(mid):
        right = mid - 1
        answer = min(mid, answer)
    else:
        left = mid + 1

print(answer)
