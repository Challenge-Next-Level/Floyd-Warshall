import sys

n, k = map(int, sys.stdin.readline().split())
level = []
for _ in range(n):
    level.append(int(sys.stdin.readline().split()[0]))

left, right = min(level), max(level) + k
answer = 0
while left <= right:
    mid = (left+ right) // 2
    needs = 0
    for i in range(n):
        if mid > level[i]:
            needs += mid - level[i]
    if needs > k:
        right = mid - 1
    else:
        left = mid + 1
        answer = max(answer, mid)
print(answer)