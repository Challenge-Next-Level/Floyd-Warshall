from collections import defaultdict, deque

T = int(input())

def BFS(x):
    queue = deque([x])
    visited[x] = True
    cnt = 0
    while queue:
        now_idx = queue.popleft()

        for next_idx in graph[now_idx]:
            if visited[next_idx]:
                continue

            cnt += 1
            visited[next_idx] = True
            queue.append(next_idx)

    return cnt


for _ in range(T):
    N, M = map(int, input().split())

    graph = defaultdict(list)

    for _ in range(M):
        a, b = map(int, input().split())
        graph[a].append(b)
        graph[b].append(a)

    visited = [False for _ in range(N + 1)]

    answer = 0

    answer += BFS(1)

    print(answer)
