import sys
from collections import deque

N = int(sys.stdin.readline())
nums = deque() # 메모리 초과가 발생하여 숫자를 넣고, 빼기 쉬운 deque을 활용
answer = 0
total = 0
for i in range(1, N + 1):
    while total > N:
        total -= nums.popleft()
    if total == N:
        answer += 1
    total += i
    nums.append(i)
print(answer + 1) # 본인 숫자 하나의 경우도 포함