import sys

input = sys.stdin.readline

import heapq

N, M, B = map(int, input().split())

# 보드를 한줄로 입력
board = list()
for _ in range(N):
    board.extend(list(map(int, input().split())))

# 시간, 보드, 현재 남은 블럭의 개수
min_heap = [[0, board, B]]

answer_time = -1
answer_height = 0

while min_heap:
    now_time, now_board, now_block = heapq.heappop(min_heap)
    print(now_time, now_board)

    # 종료 조건 확인
    now_height = now_board[0]
    is_answer = True
    for i in range(1, N * M):
        if now_height != now_board[i]:
            is_answer = False
            break

    if is_answer:
        # 최초 정답 조건
        if answer_time == -1:
            answer_time = now_time
            answer_height = now_height
        # 시간이 최소가 되어야 한다.
        else:
            if answer_time == now_time:
                answer_height = max(answer_height, now_height)
            # 현재 최소 시간에 대해서, 모든 탐색이 끝났으므로 프로그램 종료
            elif answer_time < now_time:
                print(answer_time, answer_height)
                exit()

    # 다음 탐색 수행
    # 블럭을 제거한다.
    for j in range(N * M):
        # 땅의 높이는 음수가 될 수 없다.
        if now_board[j] >= 1:
            copy_board = now_board[:]
            copy_block = now_block
            copy_board[j] -= 1
            heapq.heappush(min_heap, [now_time + 2, copy_board, copy_block + 1])

    # 블럭을 놓는다.
    if now_block >= 1:
        for j in range(N * M):
            # 땅의 높이는 최대 256이다.
            if now_board[j] < 256:
                copy_board = now_board[:]
                copy_block = now_block
                copy_board[j] += 1
                heapq.heappush(min_heap, [now_time + 1, copy_board, copy_block - 1])

