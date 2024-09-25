from collections import deque


def solution(rectangle, characterX, characterY, itemX, itemY):
    # 사각형 외각 - 1, 사각형 내부 - 2, 비어있는 공간 - 0
    board = [[0 for _ in range(101)] for _ in range(101)]

    for start_x, start_y, end_x, end_y in rectangle:
        start_x, start_y, end_x, end_y = start_x * 2, start_y * 2, end_x * 2, end_y * 2
        start_y, end_y = (100 - end_y), (100 - start_y)

        for _y in range(start_y, end_y + 1):
            for _x in range(start_x, end_x + 1):
                # 사각형 외각
                if _y == start_y or _y == end_y or _x == start_x or _x == end_x:
                    # 다른 사각형의 내부
                    if board[_y][_x] != 0 and board[_y][_x] == 2:
                        continue
                    elif board[_y][_x] == 0:
                        board[_y][_x] = 1
                # 사각형의 내부
                else:
                    board[_y][_x] = 2

    characterX, characterY, itemX, itemY = characterX * 2, characterY * 2, itemX * 2, itemY * 2
    characterY, itemY = (100 - characterY), (100 - itemY)

    dx = [1, -1, 0, 0]
    dy = [0, 0, 1, -1]

    visited = [[False for _ in range(101)] for _ in range(101)]

    answer = 1e9

    queue = deque()
    queue.append([characterX, characterY, 0])
    visited[characterY][characterX] = True

    while queue:
        now_x, now_y, moving_cnt = queue.popleft()

        if now_x == itemX and now_y == itemY:
            answer = min(answer, moving_cnt)
            continue

        for i in range(4):
            new_x, new_y = now_x + dx[i], now_y + dy[i]

            if not (0 <= new_x < 101) or not (0 <= new_y < 101):
                continue

            if board[new_y][new_x] != 1:
                continue

            if visited[new_y][new_x]:
                continue

            queue.append([new_x, new_y, moving_cnt + 1])
            visited[new_y][new_x] = True

    return answer // 2