import copy
from collections import deque

n = int(input())

k = int(input())

apples = list()

for _ in range(k):
    apples.append(list(map(int, input().split())))

l = int(input())

rotation = list()

for _ in range(l):
    x, c = input().split()
    x = int(x)
    rotation.append([x, c])

# FIFO - DEQUE 사용 - 맨 앞이 머리, 뒤가 꼬리
snake = deque()
# (y,x)
snake.append([1,1])

# 현재 방향
d = 0
# 우, 하, 좌, 상
dx = [1, 0, -1, 0]
dy = [0, 1, 0, -1]

# 현재 시각
t = 0

while True:
    t += 1
    # 이동한 머리
    new_head = copy.deepcopy(snake[0])
    new_head[0] += dy[d]
    new_head[1] += dx[d]

    # 새로운 머리가 벽에 부딪히면 break
    if not (1 <= new_head[0] <= n) or not (1 <= new_head[1] <= n):
        break

    # 자기 자신과 부딪혔는지 확인
    if new_head in snake:
        break

    # 연장한 머리 추가
    snake.appendleft(new_head)

    # 사과 확인
    if new_head in apples:
        apples.remove(new_head)
    else:
        snake.pop()

    # 방향 전환
    if len(rotation) > 0:
        if t == rotation[0][0]:
            if rotation[0][1] == "D":
                d = (d + 1) % 4
            elif rotation[0][1] == "L":
                d = (d - 1) % 4

            rotation.pop(0)

print(t)