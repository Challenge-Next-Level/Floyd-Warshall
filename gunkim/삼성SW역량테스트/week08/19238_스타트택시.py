# 시간초과 때문에 조금 해맨 문제
# 해결: bfs탐색시 백트래킹 조건을 하나 넣어줌
import sys
from collections import deque

n, m, fuel = map(int, sys.stdin.readline().split())
board = []
for i in range(n):
    board.append(list(map(int, sys.stdin.readline().split())))


b, a = map(int, sys.stdin.readline().split())
car = [b - 1, a - 1]
guest = []
for i in range(m):
    sy, sx, dy, dx = map(int, sys.stdin.readline().split())
    guest.append([sy-1, sx-1, dy-1, dx-1, 1]) # 맨 뒤 값은 alive 여부

count_guest = 0
dir = [[0,1], [1,0], [-1,0], [0,-1]]


def bfs(y, x, gy, gx, backtracking): # 내 위치, 게스트 위치, 앞에서 계산한 최소거리(백트래킹 조건)
    visit = [[0 for _ in range(n)] for _ in range(n)] # deepcopy로 복사해서 사용하지 않고 새로 그냥 만듦
    if y == gy and x == gx:
        return 0
    queue = deque([[y, x, 0]])

    while queue:
        qy, qx, dist = queue.popleft()
        if visit[qy][qx] == 1:
            continue
        if qy == gy and qx == gx:
            return dist
        if dist > backtracking: # 백트래킹 조건(시간초과 해결!)
            return dist
        visit[qy][qx] = 1
        for dy, dx in dir:
            ny, nx = qy + dy, qx + dx
            if 0 <= ny < n and 0 <= nx < n and board[ny][nx] != 1:
                queue.append([ny, nx, dist + 1])
    return None


while True:
    if count_guest == m:
        break
    # 최단거리의 손님 찾기 및 이동
    min_guest = [float('inf'), -1] # 거리, 손님index
    for i in range(m):
        if guest[i][-1] == 0: # 이미 태운 승객은 탐색할 필요 x
            continue
        to_guest = bfs(car[0], car[1], guest[i][0], guest[i][1], min_guest[0]) # 손님까지 최단거리
        if to_guest is None: # 벽에 막혀 못가는 경우
            fuel = -1
            break
        if min_guest[0] >= to_guest: # 최단거리가 같은 손님 처리
            if min_guest[0] > to_guest:
                min_guest = [to_guest, i]
            else:
                cur_guest = guest[min_guest[1]]
                if cur_guest[0] > guest[i][0]:
                    min_guest = [to_guest, i]
                elif cur_guest[0] == guest[i][0]:
                    if cur_guest[1] > guest[i][1]:
                        min_guest = [to_guest, i]
    fuel -= min_guest[0]
    if fuel < 0: # 손님에게 갈 수 없는 경우
        break
    # 최단거리로 도착지까지 이동
    this_guest = guest[min_guest[1]]
    to_dest = bfs(this_guest[0], this_guest[1], this_guest[2], this_guest[3], float('inf')) # 도착지까지 최단거리
    if to_dest is None: # 벽에 막혀 못가는 경우
        fuel = -1
        break
    fuel -= to_dest
    if fuel < 0: # 도착지에 갈 수 없는 경우
        break
    # 연료충전 및 손님 카운트
    fuel += to_dest * 2
    count_guest += 1
    car = [this_guest[2], this_guest[3]]
    this_guest[4] = 0

if fuel > 0:
    print(fuel)
else:
    print(-1)