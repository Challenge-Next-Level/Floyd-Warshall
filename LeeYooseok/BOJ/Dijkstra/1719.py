"""
안풀림 - 틀렸습니다.
"""

import sys
import heapq

input = sys.stdin.readline
INF = sys.maxsize

n, m = map(int, input().split())

graph = [[] for _ in range(n+1)]
result = [['-'] * (n+1) for _ in range(n+1)] # 각 지점으로 갈 때 최초로 거치는 노드 저장

def Dijkstra(start):
    heap = []
    dp = [INF] * (n+1)

    dp[start] = 0
    heapq.heappush(heap, (0, start))

    while heap:
        weight, now = heapq.heappop(heap)

        if weight > dp[now]:
            continue

        for w, next_node in graph[now]:
            next_weight = weight + w

            if dp[next_node] > next_weight:
                dp[next_node] = next_weight
                heapq.heappush(heap, (next_weight, next_node))
                # 예를 들어 1에서 6으로 이동할 때 6전에 5를 마지막으로 거쳐 이동한다면
                # 6에서 1로 이동할 때 처음으로 거치는 노드는 5가 된다.
                # 따라서 아래와 같이 반대로 이동할 때의 경우에 정답 저장
                result[next_node][start] = now

# 초기화
for _ in range(m):
    a, b, c = map(int, input().split())

    # 양방향 그래프
    graph[a].append((c, b))
    graph[b].append((c, a))

for i in range(1, n+1):
    Dijkstra(i)

for i in range(1, n+1):
    print(' '.join(map(str, result[i][1:])))