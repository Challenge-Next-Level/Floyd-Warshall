import sys

input = sys.stdin.readline

N, M = map(int, input().split())
board = [list(map(int, input().split())) for _ in range(N)]

# 첫번째 행일 경우 -> 왼쪽에서 오른쪽으로 가는 경우밖에 없음
for _x in range(M - 1):
    board[0][_x + 1] += board[0][_x]

# 나머지 행
for _y in range(1, N):
    # 왼쪽에서 오른쪽으로 가는 배열
    left_to_right = board[_y][:]
    # 오른쪽에서 왼쪽으로 가는 배열
    right_to_left = board[_y][:]

    # 왼쪽에서 오른쪽으로 가는 경우
    for _x in range(M):
        # 첫번째 열일 경우 -> 위에서 내려오는 경우 밖에 없음
        if _x == 0:
            left_to_right[_x] += board[_y - 1][_x]
        # 나머지 열일 경우 -> 위에서 내려오는 경우와 왼쪽에서 오는 경우 비교
        else:
            left_to_right[_x] += max(board[_y - 1][_x], left_to_right[_x - 1])

    # 오른쪽에서 왼쪽으로 가는 경우
    for _x in range(M - 1, -1, -1):
        # 마지막 열일 경우 -> 위에서 내려오는 경우 밖에 없음
        if _x == M - 1:
            right_to_left[_x] += board[_y - 1][_x]
        # 나머지 열일 경우 -> 위에서 내려오는 경우와 오른쪽에서 오는 경우 비교
        else:
            right_to_left[_x] += max(board[_y - 1][_x], right_to_left[_x + 1])

    # 각 좌표값 최대값 확인
    for _x in range(M):
        board[_y][_x] = max(left_to_right[_x], right_to_left[_x])

print(board[-1][-1])
