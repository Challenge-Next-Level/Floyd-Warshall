# 최소 비용 경로는 여러가지가 있을 수 있음. 예제의 답이랑 다르게 나와도 된다.
# 처음에 그래서 틀린줄 알았네..;;
import sys
import heapq

n = int(sys.stdin.readline())
m = int(sys.stdin.readline())

graph = [[] for _ in range(n + 1)]
for _ in range(m):
    a, b, cost = map(int, sys.stdin.readline().split())
    graph[a].append([b, cost])
start, end = map(int, sys.stdin.readline().split())

heap = []
dp = [float('inf')] * (n + 1)
before_node = [float('inf')] * (n + 1) # 최종 목적지 방문 바로 전 노드를 따로 저장


def dijkstra(start_node):
    dp[start_node] = 0
    heapq.heappush(heap, [0, start_node])
    while heap:
        cur_weight, cur_node = heapq.heappop(heap)
        if dp[cur_node] < cur_weight:
            continue
        for moved_node, weight in graph[cur_node]:
            total_weight = cur_weight + weight
            if dp[moved_node] > total_weight:
                dp[moved_node] = total_weight
                heapq.heappush(heap, [total_weight, moved_node])
                before_node[moved_node] = cur_node # 이 한 줄만 추가하면 된다


dijkstra(start)
print(dp[end]) # 최소 비용 출력
answer = [end]
node = before_node[end]
while node != float('inf'):
    answer.append(node)
    node = before_node[node]
print(len(answer)) # 경로 길이 출력
for _ in range(len(answer)): # 경로 출력
    print(answer.pop(), end=' ')
