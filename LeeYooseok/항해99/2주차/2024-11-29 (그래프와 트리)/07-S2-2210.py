board = [input().split() for _ in range(5)]

answer = set()

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

for _y in range(5):
    for _x in range(5):

        stack = [[_x, _y, board[_y][_x], 1]]
        while stack:
            now_x, now_y, now_value, now_cnt = stack.pop()
            if now_cnt == 6:
                answer.add(now_value)
                continue

            for i in range(4):
                new_x, new_y = now_x + dx[i], now_y + dy[i]

                if not (0 <= new_x < 5) or not (0 <= new_y < 5):
                    continue

                stack.append([new_x, new_y, now_value + board[new_y][new_x], now_cnt + 1])

print(len(answer))
