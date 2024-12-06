import sys

input = sys.stdin.readline

N, M = map(int, input().split())

board = [list(map(int, input().split())) for _ in range(N)]

for _y in range(N):
    # 첫번째 행일 경우
    if _y == 0:
        # 왼쪽에서 오른쪽으로 가는 경우만 고려한다.
        for _x in range(1, M):
            board[_y][_x] += board[_y][_x - 1]

    # 두번째 행 ~ 마지막 행
    else:
        # 왼쪽에서 오른쪽으로 가는 경우
        left_to_right = board[_y][:]
        for _x in range(M):
            # 첫번째 열 : 위에서 내려오는 경우밖에 없음
            if _x == 0:
                left_to_right[_x] += board[_y - 1][_x]
            else:
                left_to_right[_x] += max(board[_y - 1][_x], left_to_right[_x - 1])

        # 오른쪽에서 왼쪽으로 가는 경우
        right_to_left = board[_y][:]
        for _x in range(M - 1, -1, -1):
            # 마지막 열 : 위에서 내려오는 경우밖에 없음
            if _x == M - 1:
                right_to_left[_x] += board[_y - 1][_x]
            else:
                right_to_left[_x] += max(board[_y - 1][_x], right_to_left[_x + 1])

        # 두 경우를 비교해서 최대값
        for _x in range(M):
            board[_y][_x] = max(left_to_right[_x], right_to_left[_x])

print(board[-1][-1])
