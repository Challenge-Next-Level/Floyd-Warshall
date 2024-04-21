# 전체 이동 횟수 : edge 개수 * 2 - 오른쪽으로만 이동하는 edge 개수
from collections import defaultdict, deque

N = int(input())

tree = defaultdict(list)
for _ in range(N):
    a, b, c = map(int, input().split())
    tree[a] = [b, c]

# 전체 edge 개수 확인
count_all = 0
visited = [False for _ in range(N + 1)]
queue = deque([1])
while queue:
    now_node = queue.pop()

    for next_node in tree[now_node]:
        if next_node == -1:
            continue

        if visited[next_node]:
            continue

        visited[next_node] = True
        queue.append(next_node)
        count_all += 1

# 오른쪽으로만 가능 edge 개수 확인
count_right = 0
visited = [False for _ in range(N + 1)]
queue = deque([1])
while queue:
    now_node = queue.pop()

    next_node = tree[now_node][1]

    if next_node == -1:
        continue

    if visited[next_node]:
        continue

    visited[next_node] = True
    queue.append(next_node)
    count_right += 1

print(count_all * 2 - count_right)