import sys
from collections import deque

n, m = map(int, input().split())
myParent = {}
for _ in range(m):
    A, B = map(int, sys.stdin.readline().split())
    # A가 B를 신뢰
    if B not in myParent:
        myParent[B] = [A]
    else:
        myParent[B].append(A)


def bfs(node):
    count = 0
    visit = [False for _ in range(n+1)]
    dq = deque([node])
    visit[node] = True
    while dq:
        nd = dq.popleft()
        if nd in myParent:
            for ndParent in myParent[nd]:
                if visit[ndParent] is False:
                    count += 1
                    dq.append(ndParent)
                    visit[ndParent] = True
    return count


maxCnt = 0
answer = []
for num in range(n+1):
    # bfs
    cnt = bfs(num)
    if cnt > maxCnt:
        maxCnt = cnt
        answer = [num]
    elif cnt == maxCnt:
        answer.append(num)

answer.sort()
print(' '.join(list(map(str, answer))))