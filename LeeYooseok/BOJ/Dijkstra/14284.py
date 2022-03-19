"""
문제 : s와 t가 연결이 되는 시점의 간선의 가중치의 합(s에서 t로 가는 거리)이 최소가 되도록, 추가하는 간선의 순서를 조정한다.
- 그때의 s에서 t로 가는 최소 가중치를 구하시오

즉, 모든 간선이 주어졌을때, s에서 t로 가는 최소 거리를 구하면 되는 것이었다.
"""

import sys
import heapq

input = sys.stdin.readline
INF = sys.maxsize

# 정점의 개수 n, 간선의 개수 m
n, m = map(int, input().split())
# 최소 힙
heap = []
# 가중치 테이블
dp = [INF] * (n + 1)
# 그래프
graph = [[] for _ in range(n+1)]

# Dijkstra
def Dijkstra(start):
    # 가중치 테이블에서 시작 정점에 해당하는 값을 0으로 초기화
    dp[start] = 0
    # 최소 힙에 (가중치, 시작 정점)를 넣어줍니다.
    heapq.heappush(heap, (0, start))

    # 최소 힙에 원소가 없을 때 까지 반복
    while heap:
        # 최소 힙에서 가장 가중치가 적은 노드를 선택합니다.
        weight, now = heapq.heappop(heap)

        # 현재 테이블과 비교하여 불필요한(더 가중치가 큰) 튜플이면 무시
        if dp[now] < weight:
            continue

        # now 가 시작 지점인 모든 간선을 확인
        for w, next_node in graph[now]:
            next_weight = weight + w

            # 다음 노드까지의 가중치(next_weight)가 현재 테이블(dp)에 기록된 값 보다 작으면
            if next_weight < dp[next_node]:
                dp[next_node] = next_weight

                heapq.heappush(heap, (next_weight, next_node))


# 초기화
edgeList = []
for _ in range(m):
    a, b, c = list(map(int, input().split()))
    # 무방향 그래프
    # (가중치, 목적지 노드) 형태로 최소 힙에 넣어줍니다.
    graph[a].append((c, b))
    graph[b].append((c, a))

# 시작 s, 끝 t
s, t = map(int, input().split())

Dijkstra(s)

print(dp[t])

