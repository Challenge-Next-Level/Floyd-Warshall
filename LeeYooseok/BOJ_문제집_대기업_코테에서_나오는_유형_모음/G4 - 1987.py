import sys
input = sys.stdin.readline

R, C = map(int, input().split())
board = list()
for _ in range(R):
    x_board = list(input().rstrip())
    new_x_board = list()
    for item in x_board:
        new_x_board.append(ord(item) - 65)
    board.append(new_x_board)

alphabet_visited = [False for _ in range(26)]

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

answer = 0


def DFS(move_count, now_x, now_y):
    global answer
    answer = max(answer, move_count)

    for i in range(4):
        new_x = now_x + dx[i]
        new_y = now_y + dy[i]

        if not (0 <= new_x < C) or not (0 <= new_y < R):
            continue

        now_alphabet = board[new_y][new_x]
        if alphabet_visited[now_alphabet]:
            continue

        alphabet_visited[now_alphabet] = True
        DFS(move_count + 1, new_x, new_y)
        alphabet_visited[now_alphabet] = False


alphabet_visited[board[0][0]] = True
DFS(1, 0, 0)

print(answer)