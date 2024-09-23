from collections import deque

def solution(people, limit):
    people.sort()
    answer = 0

    queue = deque(people)
    while queue:
        if len(queue) >= 2:
            if queue[0] + queue[-1] <= limit:
                queue.popleft()
                queue.pop()
                answer += 1
            else:
                queue.pop()
                answer += 1
        else:
            queue.pop()
            answer += 1

    return answer