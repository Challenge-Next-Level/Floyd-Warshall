import sys
from collections import deque

N = int(sys.stdin.readline().split()[0])
targetA, targetB = map(int, sys.stdin.readline().split())
M = int(sys.stdin.readline().split()[0])
relation = [[] for _ in range(N + 1)] # 부모, 자식 관계 쌍방 연결
for i in range(M):
    a, b = map(int, sys.stdin.readline().split())
    if a not in relation[b]:
        relation[b].append(a)
    if b not in relation[a]:
        relation[a].append(b)

visit = [0] * (N + 1) # 방문 노드인지 체크


def bfs(node): # 가장 가까운 촌수를 계산해야 하니 너비 탐색
    route = deque([[node, 0]])
    while route:
        n, depth = route.popleft()
        if visit[n] == 1:
            continue
        if n == targetB: # 목표 타겟을 찾으면 depth 반환
            return depth
        visit[n] = 1
        for conn in relation[n]:
            route.append([conn, depth + 1])
    return -1 # 못하면 -1 반환


answer = bfs(targetA)
print(answer)