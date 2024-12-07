import heapq

N = int(input())
class_list = list()
for _ in range(N):
    idx, S, T = map(int, input().split())
    class_list.append([S, T])

# 수업이 빨리 시작하는 순서대로 정렬
class_list.sort()

min_heap = list()

# 가장 빨리 시작하는 수업의 종료 시각
heapq.heappush(min_heap, class_list[0][1])
answer = 1

for i in range(1, N):
    # i번째로 빨리 시작하는 수업
    next_start = class_list[i]

    # i번째로 빨리 시작하는 수업의 시작 시각 < 현재 가장 빨리 시작하는 수업의 종료 시각
    if next_start[0] < min_heap[0]:
        # 두 수업은 동시에 진행되어야 함
        answer += 1
        heapq.heappush(min_heap, next_start[1])
    # i번째로 빨리 시작하는 수업의 시작 시각 >= 현재 가장 빨리 시작하는 수업의 종료시각
    else:
        # 현재 가장 빨리 끝나는 수업이 종료된다.
        heapq.heappop(min_heap)
        # i번째로 빨리 시작하는 수업이 시작한다.
        heapq.heappush(min_heap, next_start[1])

print(answer)