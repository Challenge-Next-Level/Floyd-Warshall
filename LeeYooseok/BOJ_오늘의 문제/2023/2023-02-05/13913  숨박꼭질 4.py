from collections import deque

n, k = map(int, input().split())

visited = [0 for _ in range(100001)]
previous_node = [0 for i in range(100001)]

que = deque([n])
visited[n] = 1

def path(finish):
    node = finish
    answer = [node]
    for _ in range(visited[finish] - 1):
        node = previous_node[node]
        answer.append(node)
    print(*answer[::-1])


while que:
    now_idx = que.popleft()

    if now_idx == k:
        print(visited[now_idx] - 1)
        path(now_idx)
        exit()

    for next_idx in [now_idx - 1, now_idx + 1, now_idx * 2]:
        if not(0 <= next_idx <= 100000):
            continue
        if visited[next_idx] > 0:
            continue

        visited[next_idx] = visited[now_idx] + 1
        previous_node[next_idx] = now_idx
        que.append(next_idx)
