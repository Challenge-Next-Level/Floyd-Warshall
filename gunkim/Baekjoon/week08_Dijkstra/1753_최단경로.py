import sys
import heapq


V, E = map(int, sys.stdin.readline().split()) # 정점, 간선 갯수
K = int(sys.stdin.readline()) # 시작 정점

INF = float('inf')
dp = [INF] * (V + 1) # 가중치 테이블 dp
heap = []
graph = [[] for _ in range(V + 1)]


def Dijkstra(start):
    dp[start] = 0
    heapq.heappush(heap, (0, start)) # 기본적으로 최소힙으로 만들어짐

    # 힙에 원소가 없을 때 까지 반복.
    while heap:
        cur_weight, cur_node = heapq.heappop(heap) # 가장 작은 원소(아마 root)가 삭제
        if dp[cur_node] < cur_weight: # 비용이 더 적다면 dp 갱신, 아니면 continue
            continue
        for weight, node in graph[cur_node]: # 현재 노드에서 갈 수 있는 간선 탐색 후 dp 갱신 및 heapq에 추가
            total_weight = weight + cur_weight
            if total_weight < dp[node]:
                dp[node] = total_weight
                heapq.heappush(heap, (total_weight, node))


for _ in range(E):
    u, v, w = map(int, sys.stdin.readline().split())
    graph[u].append([w, v]) # 간선 저장
Dijkstra(K)
for i in range(1, V + 1):
    print("INF" if dp[i] == INF else dp[i])
