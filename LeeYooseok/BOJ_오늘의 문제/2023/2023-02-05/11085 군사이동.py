import sys
from collections import defaultdict
import heapq

p, w = map(int, input().split())
c, v = map(int, input().split())
graph = defaultdict(list)

for _ in range(w):
    start, end, width = map(int, input().split())
    graph[start].append([end, width])
    graph[end].append([start, width])

visited = [False] * p
heap = []
heapq.heappush(heap, [-1 * sys.maxsize, c])
answer = sys.maxsize # 최소값 찾기

while heap:
    now_cost, now_node = heapq.heappop(heap)
    now_cost *= -1

    if visited[now_node]:
        continue
    visited[now_node] = True

    answer = min(answer, now_cost)
    # 최대 힙을 사용하기 때문에 종료조건을 가장 먼저 만족하는 루트가 최대 비용이 드는 경로 이다.
    if now_node == v:
        print(answer)
        exit()

    for next_node, next_cost in graph[now_node]:
        heapq.heappush(heap, [-1 * next_cost, next_node])

