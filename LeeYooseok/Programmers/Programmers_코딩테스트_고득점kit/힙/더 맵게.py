import heapq

def solution(scoville_list, K):
    heapq.heapify(scoville_list)

    answer = 0
    while len(scoville_list) >= 2:
        scoville_1 = heapq.heappop(scoville_list)
        if scoville_1 >= K:
            heapq.heappush(scoville_list, scoville_1)
            break
        scoville_2 = heapq.heappop(scoville_list)

        new_scoville = scoville_1 + 2 * scoville_2

        heapq.heappush(scoville_list, new_scoville)
        answer += 1

    if scoville_list[0] < K:
        return -1
    return answer

print(solution([1, 2, 3, 9, 10, 12], 7))