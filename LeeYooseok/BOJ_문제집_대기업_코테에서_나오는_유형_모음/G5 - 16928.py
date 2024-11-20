from collections import deque

N, M = map(int, input().split())

graph = [-1 for _ in range(101)]

for _ in range(N):
    x, y = map(int, input().split())
    graph[x] = y

for _ in range(M):
    u, v = map(int, input().split())
    graph[u] = v

visited = [False for _ in range(101)]
# [위치, 주사위 굴린 횟수]
deq = deque([[1, 0]])
visited[1] = True

while deq:
    now_loc, now_count = deq.popleft()

    if now_loc == 100:
        print(now_count)
        break

    for i in range(1, 7):
        next_loc = now_loc + i

        if not (next_loc <= 100):
            continue

        while graph[next_loc] != -1:
            next_loc = graph[next_loc]

        if visited[next_loc]:
            continue

        visited[next_loc] = True
        deq.append([next_loc, now_count + 1])
