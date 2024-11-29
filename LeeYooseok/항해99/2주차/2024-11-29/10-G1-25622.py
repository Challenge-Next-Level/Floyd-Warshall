import sys

input = sys.stdin.readline

from collections import defaultdict

N = int(input())
graph = defaultdict(list)
for _ in range(N - 1):
    u, v = map(int, input().split())
    graph[u].append(v)
    graph[v].append(u)

visited = [False for _ in range(N + 1)]
visited_set = set()

answer = False
answer_group = list()


def DFS(now_group, node_group, cnt):
    global answer, answer_group
    # 종료 조건
    # 모든 node를 방문했고, 3개로 나눌 수 있다면 -> True
    if len(node_group) == ((N // 3) - 1) and len(now_group) == 3 and cnt == N:
        print("S")
        for group in node_group:
            print(*group)
        print(*now_group)
        exit()

    if len(now_group) == 3:
        # 3개 그룹 방문 처리
        if tuple(now_group) in visited_set:
            return
        visited_set.add(tuple(now_group))

    for now_node in now_group:
        for next_node in graph[now_node]:
            if visited[next_node]:
                continue

            visited[next_node] = True
            # 3개가 완성 되었으면
            if len(now_group) == 3:
                DFS([next_node], node_group + [now_group], cnt + 1)
            else:
                DFS(now_group + [next_node], node_group, cnt + 1)
            visited[next_node] = False


for start_node in range(1, N + 1):
    visited[start_node] = True
    DFS([start_node], list(), 1)
    visited[start_node] = False

print("U")
