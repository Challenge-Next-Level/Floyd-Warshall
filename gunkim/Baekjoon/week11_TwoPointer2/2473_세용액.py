# python3 역시 시간초과 발생, pypy3로 채점해야한다
import sys


N = int(sys.stdin.readline())
liquid = list(map(int, sys.stdin.readline().split()))
liquid.sort()

answer = float('inf')
result = []
for i in range(N): # 용액 하나를 미리 정한다
    left, right = 0, N - 1 # 나머지 용액 2개를 투 포인터로 정한다
    while left < right:
        if left == i:
            left += 1
            continue
        if right == i:
            right -= 1
            continue
        total = liquid[i] + liquid[left] + liquid[right]
        if answer >= abs(total):
            answer = abs(total)
            result = [liquid[i], liquid[left], liquid[right]]
        if total > 0:
            right -= 1
        else:
            left += 1
result.sort()
print(' '.join(map(str, result)))