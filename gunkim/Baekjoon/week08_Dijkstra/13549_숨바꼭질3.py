# 대부분 BFS로 푸는 것 같음. 다익스트라 문제로 인식해서 푸니까 생각을 아예 못함.
# 다익스트라로 접근해서 어느 정도 풀었는데 한가지 예외 처리를 못함. 실수도 있었음.
import sys
import heapq

N, K = map(int, sys.stdin.readline().split())
INF = float('inf')
dp = [INF for _ in range(100001)] # 간과했던 실수. 입력값이 작아 시간초과 걱정 할 필요가 없었음.
heap = []


def dijkstra(start):
    if K <= start: # 간과했던 예외 처리. 좌표 좌측 이동은 -1로 밖에 할 수 없었다.
        return start - K

    heapq.heappush(heap, (0, start))

    while heap:
        time, node = heapq.heappop(heap)
        for moved_node in [node * 2, node - 1, node + 1]: # 3가지 이동 가능 경우
            if 0 <= moved_node <= 100000 and dp[moved_node] == INF:
                if moved_node == node * 2:
                    heapq.heappush(heap, (time, moved_node))
                    dp[moved_node] = time
                else:
                    heapq.heappush(heap, (time + 1, moved_node))
                    dp[moved_node] = time + 1
    return dp[K]


print(dijkstra(N))