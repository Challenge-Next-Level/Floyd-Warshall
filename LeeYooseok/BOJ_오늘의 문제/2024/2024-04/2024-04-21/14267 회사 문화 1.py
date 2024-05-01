import sys

input = sys.stdin.readline

n, m = map(int, input().split())

tree_list = list(map(int, input().split()))

answer = [0 for _ in range(n)]

for _ in range(m):
    i, w = map(int, input().split())
    answer[i - 1] += w # 자기 자신의 점수를 더해준다.

# 직속 상사의 값을 더해준다.
for i in range(1, n):
    answer[i] += answer[tree_list[i] - 1]

print(*answer)