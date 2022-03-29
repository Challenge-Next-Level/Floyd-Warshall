import sys

n = int(sys.stdin.readline())
solution = list(map(int, sys.stdin.readline().split()))

answer = [float('inf'), 0, 0]
left, right = 0, n - 1
# 어떤 조건에 어떤 인덱스를 움직여야 하는지 답을 보면 쉽지만 생각보다 너무 어렵다
while left < right:
    total = solution[left] + solution[right]
    if abs(total) < answer[0]:
        answer[0] = abs(total)
        answer[1], answer[2] = solution[left], solution[right]
    if total > 0:
        right -= 1
    else:
        left += 1
print(' '.join(map(str, answer[1:])))
