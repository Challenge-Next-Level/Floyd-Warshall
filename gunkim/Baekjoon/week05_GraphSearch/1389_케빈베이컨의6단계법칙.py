import sys
from collections import deque

N, M = map(int, sys.stdin.readline().split())
relation = [[] for _ in range(N + 1)]
answer = [0] * (N + 1)

for i in range(M): # node간 관계를 쌍방으로 저장한다
    a, b = map(int, sys.stdin.readline().split())
    if b not in relation[a]:
        relation[a].append(b)
    if a not in relation[b]:
        relation[b].append(a)


def bfs(node): # 깊이를 물어보는 문제이기 때문에 bfs탐색
    visit = [0] * (N + 1)
    cavin = deque([[node, 0]])
    total_depth = 0
    while cavin:
        num, depth = cavin.popleft()
        if visit[num] == 1:
            continue
        visit[num] = 1
        total_depth += depth
        for n in range(len(relation[num])):
            cavin.append([relation[num][n], depth + 1])
    return total_depth


for i in range(1, N + 1): # 각 node에 대해 케빈-베이컨 값 계산
    answer[i] = bfs(i)

answer[0] = float('inf') # index = 0은 사용하지 않는 것이기 때문에 infinity로 초기화
min_val = min(answer)
for i in range(1, N + 1):
    if answer[i] == min_val:
        print(i)
        break