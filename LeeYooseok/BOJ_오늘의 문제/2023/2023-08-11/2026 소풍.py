from collections import defaultdict

K, N, F = map(int, input().split())

graph = defaultdict(list)
count = [1 for _ in range(N + 1)]

for _ in range(F):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)
    count[a] += 1
    count[b] += 1

def dfs(idx, cnt):
    if cnt == K:
        for v in range(1, N + 1):
            if visited[v]:
                print(v)
        exit()

    for i in range(idx + 1, N + 1):
        # i 번째 친구와 현재 visited 한 친구가 모두 친구인지 확인
        chk = True
        for v_i in range(N):
            if visited[v_i]:
                if i not in graph[v_i]:
                    chk = False
                    continue
        if chk:
            visited[i] = True
            dfs(i, cnt + 1)
            visited[i] = False


visited = [False for _ in range(N + 1)]
for i in range(1, N + 1):
    if count[i] >= K:
        visited[i] = True
        dfs(i, 1)
        visited[i] = False

print(-1)