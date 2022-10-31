import sys

n, m = map(int, sys.stdin.readline().split()) # 스태프 수, 풍선 수
staff = list(map(int, sys.stdin.readline().split()))

answer = float('inf')
left, right = 1, min(staff)*m
while left <= right:
    mid = (left + right) // 2
    total = 0
    for i in range(n):
        total += mid//staff[i]
    if total < m:
        left = mid + 1
    else:
        right = mid - 1
        answer = min(answer, mid)

print(answer)