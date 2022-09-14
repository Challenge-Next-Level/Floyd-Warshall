# stack을 이용하면 visit 관리가 제대로 이루어지지 않는 것 같음, '틀렸습니다'를 항상 받음.
# 재귀 함수로 구현하는게 내게 더 좋고 직관적인 풀이인 것 같음.
import sys

n, m = map(int, input().split())
node = [[] for _ in range(n)]
for _ in range(m):
    start, end = map(int, sys.stdin.readline().split())
    node[start].append(end)
    node[end].append(start)
visit = [False] * n


def dfs(start, depth):
    if depth >= 5:
        print(1)
        exit()
    for nxt in node[start]:
        if visit[nxt] is False:
            visit[nxt] = True
            dfs(nxt, depth+1)
            visit[nxt] = False
    return


for i in range(n):
    visit[i] = True
    dfs(i, 1)
    visit[i] = False

print(0)