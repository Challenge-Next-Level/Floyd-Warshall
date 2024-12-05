import sys

input = sys.stdin.readline

N, M, B = map(int, input().split())

# 보드를 한줄로 입력
board = list()
for _ in range(N):
    board.extend(list(map(int, input().split())))

time = [0 for _ in range(257)]  # time[i] = i번째 높이로 만드는데 드는 최소 시간

answer = 0
for h in range(257):
    # 인벤토리에 남아있는 블록의 개수
    block = B

    for _y in board:
        # 목표 높이보다 현재 높이가 낮으면 -> 블럭 채워넣어야 함
        if _y <= h:
            time[h] += h - _y
            block -= (h - _y)
        # 목표 높이보다 현재 높이가 높으면 -> 블럭 제거
        else:
            time[h] += 2 * (_y - h)
            block += (_y - h)

    # block 개수가 음수이면 할 수 없음
    # 오름차순으로 순회하므로, 답이 여러 개 있을 때 그중에서 땅의 높이가 가장 높은 것을 저장하게 됨
    if block >= 0 and time[h] <= time[answer]:
        answer = h

print(time[answer], answer)