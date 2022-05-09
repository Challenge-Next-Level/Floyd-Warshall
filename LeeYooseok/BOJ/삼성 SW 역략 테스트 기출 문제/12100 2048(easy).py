# 모든 경우의 수 탐색
# https://cijbest.tistory.com/86
from copy import deepcopy

n = int(input())
board = [list(map(int, input().split())) for _ in range(n)]

result = 0

# 위로 이동
def up(board):
    for i in range(n):
        point = 0
        for j in range(1, n):
            # 해당 위치가 0이 아니면,
            if board[j][i]:
                tmp = board[j][i] # 현재 수 저장
                board[j][i] = 0

                # 포인터가 가리키는 수가 0일 때
                if board[point][i] == 0:
                    # 현재 수를 올려줌
                    board[point][i] = tmp
                # 포인터가 가리키는 수와 현재 위치의 수가 같을 때
                elif board[point][i] == tmp:
                    # 수 2배
                    board[point][i] = 2*tmp
                    point += 1
                # 포인터가 가리키는 수와 현재 위치의 수가 다를 때
                else:
                    # 다음 포인터에 현재 위치의 수 저장(?)
                    point += 1
                    board[point][i] = tmp
    return board

# 아래로 이동
def down(board):
    for i in range(n):
        point = n-1
        # 아래에서 위로 n-2 -> 0
        for j in range(n-2, -1, -1):
            if board[j][i]:
                tmp = board[j][i]
                board[j][i] = 0

                # 포인터가 가리키는 수가 0일 때
                if board[point][i] == 0:
                    # 현재 수를 내려줌
                    board[point][i] = tmp
                # 포인터가 가리키는 수와 현재 위치의 수가 같을 때
                elif board[point][i] == tmp:
                    board[point][i] = 2*tmp
                    point -= 1
                # 포인터가 가리키는 수와 현재 위치의 수가 다를 때
                else:
                    point -= 1
                    board[point][i] = tmp
    return board

# 왼쪽으로 이동
def left(board):
    for i in range(n):
        point = 0
        # 왼쪽에서 오른쪽으로
        for j in range(1, n):
            if board[i][j]:
                tmp = board[i][j]
                board[i][j] = 0

                # 포인터가 가리키는 수가 0일 때
                if board[i][point] == 0:
                    # 현재 수를 왼쪽으로 이동 시켜줌
                    board[i][point] = tmp
                # 포인터가 가리키는 수와 현재 위치의 수가 같을 때
                elif board[i][point] == tmp:
                    board[i][point] = 2*tmp
                    point += 1
                # 포인터가 가리키는 수와 현재 위치의 수가 다를 때
                else:
                    point += 1
                    board[i][point] = tmp
    return board

# 오른쪽으로 이동
def right(board):
    for i in range(n):
        point = n-1
        for j in range(n-1, -1, -1):
            if board[i][j]:
                tmp = board[i][j]
                board[i][j] = 0

                if board[i][point] == 0:
                    board[i][point] = tmp
                elif board[i][point] == tmp:
                    board[i][point] = tmp * 2
                    point -= 1
                else:
                    point -= 1
                    board[i][point] = tmp
    return board

def solution(board, cnt):
    if cnt == 5:
        return max(map(max, board))

    # 상, 하, 좌, 우로 움직여 리턴한 값들 중 가장 큰 값 반환
    # board를 꼭 deepcopy하여 함수를 거친 board값이 다음 함수에 들어가지 못하도록 해주어야 한다.
    return max(solution(up(deepcopy(board)), cnt + 1), solution(down(deepcopy(board)), cnt + 1), solution(left(deepcopy(board)), cnt + 1), solution(right(deepcopy(board)), cnt + 1))

print(solution(board, 0))