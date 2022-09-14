# visit를 2억 크기의 리스트로 처음에 만들어서 '메모리 초과'를 받음 -> 당연한 결과
# dict 간단히 해결
from collections import deque

n, k = map(int, input().split()) # 우물, 집 갯수
loc = list(map(int, input().split()))

visit = dict()
go = [1, -1]


def bfs():
    count = 0
    answer = 0
    dq = deque([])
    for lo in loc:
        dq.append([lo, 1])
        visit[lo] = True
    while dq:
        cur, num = dq.popleft()
        if count >= k:
            break
        for step in go:
            next = cur + step
            if next not in visit and count < k:
                visit[next] = True
                dq.append([next, num+1])
                count += 1
                answer += num
    return answer


print(bfs())