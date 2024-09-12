from collections import deque

def solution(priorities, location):
    queue = deque()
    for idx in range(len(priorities)):
        queue.append([priorities[idx], idx])

    answer = 1
    while queue:
        now_job = queue.popleft()
        executable = True
        for job in queue:
            if job[0] > now_job[0]:
                executable = False
                break

        if executable:
            if now_job[1] == location:
                return answer
            answer += 1
        else:
            queue.append(now_job)