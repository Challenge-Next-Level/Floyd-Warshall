import sys
import heapq

input = sys.stdin.readline
INF = sys.maxsize

# 정점의 개수 V, 간선의 개수 E
V, E = map(int, input().split())
# 시작점 K
K = int(input())
# 가중치 테이블
dp = [INF] * (V + 1)
# 최소 힙
heap = []
# 그래프
graph = [[] for _ in range(V + 1)]


# Dijkstra Algorithm
def Dijkstra(start):
    # 가중치 테이블에서 시작 정점에 해당하는 가중치를 0으로 초기화
    dp[start] = 0
    # 최소 힙에 (가중치, 시작 정점)를 넣어줍니다.
    heapq.heappush(heap, (0, start))

    # 최소 힙에 원소가 없을 때 까지 반복
    while heap:
        # 최소 힙에서 가장 가중치가 적은 노드를 선택합니다.
        weight, now = heapq.heappop(heap)

        # 현재 테이블과 비교하여 불필요한(더 가중치가 큰) 튜플이면 무시.
        if dp[now] < weight:
            continue

        # now 가 시작 지점인 모든 간선을 확인합니다.
        for w, next_node in graph[now]:
            # 현재 정점 까지의 최소 가중치 weight + 현재 정점에서 다음 정점(next_node)까지의 가중치 w
            # = 다음 노드까지의 가중치 (next_weight)
            next_weight = weight + w

            # 다음 노드까지의 가중치(next_weight)가 현재 테이블(dp)에 기록된 값 보다 작으면
            if next_weight < dp[next_node]:
                # 계산했던 다음 노드의 가중치(next_weight)로 테이블(dp)을 갱신합니다.
                dp[next_node] = next_weight

                # 다음 정점 까지의 가중치와 다음 정점에 대한 정보를 최소 힙에 넣어줍니다.
                heapq.heappush(heap, (next_weight, next_node))


# 초기화
for _ in range(E):
    # u에서 v로 가는 가중치 w인 간선
    u, v, w = map(int, input().split())
    # (가중치, 목적지 노드) 형태로 저장
    graph[u].append((w, v))

# Dijkstra Algorithm 수행
Dijkstra(K)

# 출력
for i in range(1, V + 1):
    if dp[i] == INF:
        print("INF")
    else:
        print(dp[i])
