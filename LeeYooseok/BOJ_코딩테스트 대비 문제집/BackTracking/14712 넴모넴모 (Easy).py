N, M = map(int, input().split())
board = [[False for _ in range(M)] for _ in range(N)]
answer = 0

def solve(_x, _y):
    global answer
    # 종료 조건 - 네모가 없는 상태에서 가장 끝으로 갔을 경우
    if (_x, _y) == (0, N):
        answer += 1
        return

    # 오른쪽으로 한칸씩 가다가, 마지막 닿으면 다음줄 넘어감
    if _x == M-1:
        nx, ny = 0, _y + 1
    else:
        nx, ny = _x + 1, _y

    # x, y 에 네모를 놓지 않는 경우
    solve(nx, ny)

    # x, y 에 네모를 놓을 수 있고, 놓는 경우
    if not board[_y - 1][_x] or not board[_y - 1][_x - 1] or not board[_y][_x - 1]:
        board[_y][_x] = True
        solve(nx, ny)
        board[_y][_x] = False

solve(0, 0)
print(answer)