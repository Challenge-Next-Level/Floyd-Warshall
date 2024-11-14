from collections import deque

N, K = map(int, input().split())

MAX = 10 ** 5
visited = [False for _ in range(MAX + 1)]

queue = deque(list())

queue.append([N, 0])
visited[N] = True

while queue:
    now_loc, time = queue.popleft()

    # 종료 조건
    if now_loc == K:
        print(time)
        exit()

    for next_loc in (now_loc + 1, now_loc - 1, now_loc * 2):
        if 0 <= next_loc <= MAX and not visited[next_loc]:
            visited[next_loc] = True
            queue.append([next_loc, time + 1])