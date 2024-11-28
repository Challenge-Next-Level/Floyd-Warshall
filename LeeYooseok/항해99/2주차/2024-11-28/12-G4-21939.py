import sys

input = sys.stdin.readline

import heapq

N = int(input())

min_heap = list()
max_heap = list()

for _ in range(N):
    P, L = map(int, input().split())

    heapq.heappush(min_heap, [L, P])
    heapq.heappush(max_heap, [-L, -P])

solved = [[0, 0] for _ in range(100_001)]
M = int(input())
for _ in range(M):
    user_input = list(input().split())

    command = user_input[0]

    if command == "recommend":
        x = user_input[1]

        if x == "1":
            # 푼 문제는 추천 리스트에서 삭제된다.
            while solved[-max_heap[0][1]][0] != 0:
                solved[-max_heap[0][1]][0] -= 1
                heapq.heappop(max_heap)
            print(-max_heap[0][1])
        else:
            while solved[min_heap[0][1]][1] != 0:
                solved[min_heap[0][1]][1] -= 1
                heapq.heappop(min_heap)
            print(min_heap[0][1])
    elif command == "add":
        P, L = int(user_input[1]), int(user_input[2])

        heapq.heappush(min_heap, [L, P])
        heapq.heappush(max_heap, [-L, -P])
    elif command == "solved":
        P = int(user_input[1])

        solved[P][0] += 1
        solved[P][1] += 1
