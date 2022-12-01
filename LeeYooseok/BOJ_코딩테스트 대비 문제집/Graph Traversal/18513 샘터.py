from collections import deque

N, K = map(int, input().split())
lake_location_list = list(map(int, input().split()))

visited = set()

answer = 0
now_built = 0

que = deque()
# 샘터를 기준으로 시작
for lake in lake_location_list:
    # 위치, 불행도
    que.append((lake, 0))
    visited.add(lake)

while que:
    now, p = que.popleft()

    for d in [-1, 1]:
        new = now + d
        new_p = p + 1

        # 방문 여부 체크
        if new in visited:
            continue

        visited.add(new)
        answer += new_p
        now_built += 1
        que.append((new, new_p))
        if now_built == K:
            que = list()
            break

print(answer)