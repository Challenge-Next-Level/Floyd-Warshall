# 플로이드 와샬 알고리즘을 이용한 사람들의 풀이가 보였다. 하지만 참고는 하지 않았다
# 다익스트라로 풀이한 사람의 코드가 너무 간결 해서 볼 필요가 없었다
# 다익스트라 기본 틀에서 아이디어 하나(이걸 예외 처리라고 해야 할까)를 첨가 하면 됐다
import sys
import heapq

n, m = map(int, sys.stdin.readline().split())
graph = [[] for _ in range(n + 1)]
for _ in range(m):
    a, b, cost = map(int, sys.stdin.readline().split())
    graph[a].append([b, cost])
    graph[b].append([a, cost])

heap = []
dp = [[float('inf')] * (n + 1) for _ in range(n + 1)] # 각 지점으로 갈 수 있는 최소 비용을 저장
answer = [['-'] * (n + 1) for _ in range(n + 1)] # 각 지점으로 갈 때 최초로 거치는 노드 저장


def dijkstra(start_node): # 기본적인 다익스트라 틀과 완벽히 똑같다.
    dp[start_node][start_node] = 0
    heapq.heappush(heap, [0, start_node])

    while heap:
        cur_weight, cur_node = heapq.heappop(heap)
        if dp[start_node][cur_node] < cur_weight:
            continue
        for moved_node, weight in graph[cur_node]:
            total_weight = cur_weight + weight
            if total_weight < dp[start_node][moved_node]:
                dp[start_node][moved_node] = total_weight
                heapq.heappush(heap, [total_weight, moved_node])
                # 마지막 이곳에서 정답 저장을 한 줄로 끝낼 수 있다. 이해를 위한 설명.
                # 예를 들어 1에서 6으로 이동할 때 6전에 5를 마지막으로 거쳐 이동한다면
                # 6에서 1로 이동할 때 처음으로 거치는 노드는 5가 된다.
                # 따라서 아래와 같이 반대로 이동할 때 경우에 정답을 저장할 수 있다.
                answer[moved_node][start_node] = cur_node


for i in range(1, n + 1):
    dijkstra(i)
for i in range(1, n + 1):
    print(' '.join(map(str, answer[i][1:])))
