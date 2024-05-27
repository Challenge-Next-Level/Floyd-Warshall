import sys

input = sys.stdin.readline

N, L = map(int, input().split())
alcohol_list = list(map(int, input().split()))

answer = 0
C = 0
for alcohol in alcohol_list[:L]:
    C += alcohol
    if 129 <= C <= 138:
        answer += 1

for i in range(1, N - L + 1):
    C -= alcohol_list[i - 1]
    C += alcohol_list[i + L - 1]

    if 129 <= C <= 138:
        answer += 1

print(answer)