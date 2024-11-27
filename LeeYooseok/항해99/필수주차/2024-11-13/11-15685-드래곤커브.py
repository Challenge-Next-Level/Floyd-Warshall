import sys

input = sys.stdin.readline

N = int(input())
board = [[0 for _ in range(101)] for _ in range(101)]

# 동, 북, 서, 남
dx = [1, 0, -1, 0]
dy = [0, -1, 0, 1]

for _ in range(N):
    x, y, d, g = map(int, input().split())
    board[y][x] = 1

    curve_list = [d]
    for _ in range(g):
        # 문제 풀이 구현대로 끝 점에서부터 시작점 방향으로 추가함
        for k in range(len(curve_list) - 1, -1, -1):
            curve_list.append((curve_list[k] + 1) % 4)  # 시계 방향으로 90도 회전

    # 드래곤 커브 만들기
    for i in range(len(curve_list)):
        now_d = curve_list[i]
        x += dx[now_d]
        y += dy[now_d]

        if not(0 <= x < 101 and 0 <= y < 101):
            continue

        board[y][x] = 1

# 정답 확인
answer = 0
for _y in range(100):
    for _x in range(100):
        if board[_y][_x] == 1 and board[_y + 1][_x] == 1 and board[_y][_x + 1] == 1 and board[_y + 1][_x + 1] == 1:
            answer += 1

print(answer)
