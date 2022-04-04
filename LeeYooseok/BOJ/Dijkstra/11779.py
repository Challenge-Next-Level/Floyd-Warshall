"""
스페셜 저지 : 답이 여러가지일 수 있음 즉 예제랑 내 답이 다를 수 있음
"""

import sys, heapq

input = sys.stdin.readline
INF = sys.maxsize

n = int(input())
m = int(input())

heap = []

graph = [[] for _ in range(n + 1)]

dp = [[INF, []]] * (n + 1)


def Dijkstra(start):
    dp[start] = [0, [start]]
    # 시간, 현재 위치, 현재위치까지 왔던 경로
    heapq.heappush(heap, (0, start, [start]))

    while heap:
        now_weight, now_node, now_path = heapq.heappop(heap)

        if dp[now_node][0] < now_weight:
            continue

        for w, next_node in graph[now_node]:
            next_weight = now_weight + w
            if dp[next_node][0] > next_weight:
                dp[next_node] = [next_weight, now_path + [next_node]]
                heapq.heappush(heap, (next_weight, next_node, now_path + [next_node]))


for _ in range(m):
    a, b, c = map(int, input().split())

    graph[a].append([c, b])

s, e = map(int, input().split())

Dijkstra(s)

print(dp[e][0])
print(len(dp[e][1]))
print(' '.join(map(str,dp[e][1])))
