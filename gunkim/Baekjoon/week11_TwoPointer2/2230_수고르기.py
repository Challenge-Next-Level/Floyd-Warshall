import sys

N, M = map(int, sys.stdin.readline().split())
A = [0] * N
for i in range(N):
    A[i] = int(sys.stdin.readline())
A.sort()
answer = float('inf')

left, right = 0, 1 # 초기 index 설정 생각이 너무 어렵다...
while left <= right < N:
    diff = A[right] - A[left]
    if diff < M:
        right += 1
        continue
    left += 1
    answer = min(answer, diff)
print(answer)