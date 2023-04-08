# 위상 정렬
from collections import defaultdict, deque

N, M = map(int, input().split())

graph = defaultdict(list)
indegree = [0] * (N + 1)

for _ in range(M):
    singer_list = list(map(int, input().split()))
    for i in range(1, singer_list[0]):
        graph[singer_list[i]].append(singer_list[i + 1])
        indegree[singer_list[i + 1]] += 1

q = deque()
ans = list()
for i in range(1, N + 1):
    if indegree[i] == 0:
        q.append(i)

while q:
    num = q.popleft()
    ans.append(num)
    for i in graph[num]:
        indegree[i] -= 1

        if indegree[i] == 0:
            q.append(i)

if len(ans) != N:
    print(0)
else:
    for a in ans:
        print(a)

