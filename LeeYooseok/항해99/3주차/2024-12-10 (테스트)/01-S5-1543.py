import sys

input = sys.stdin.readline

D = input().rstrip()
W = input().rstrip()

idx = 0
answer = 0

while idx < len(D) - len(W) + 1:
    if D[idx: idx + len(W)] == W:
        answer += 1
        idx += len(W)
    else:
        idx += 1

print(answer)