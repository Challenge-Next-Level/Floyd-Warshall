import heapq

N, K = map(int, input().split())

position_list = [list() for _ in range(12)]
for _ in range(N):
    P, W = map(int, input().split())

    heapq.heappush(position_list[P], -1 * W)

for _ in range(K):
    for idx in range(12):
        if position_list[idx]:
            weight = heapq.heappop(position_list[idx])
            new_weight = weight + 1
            if new_weight == 1:
                new_weight = 0
            heapq.heappush(position_list[idx], new_weight)

answer = 0
for idx in range(12):
    if position_list[idx]:
        weight = heapq.heappop(position_list[idx])
        answer += (-1 * weight)

print(answer)