from collections import deque

def solution(numbers, target):
    answer = 0

    queue = deque()
    queue.append([0, 0])

    while queue:
        now_number, now_idx = queue.popleft()
        if now_idx == len(numbers):
            if now_number == target:
                answer += 1
            continue

        queue.append([now_number + numbers[now_idx], now_idx + 1])
        queue.append([now_number - numbers[now_idx], now_idx + 1])

    return answer