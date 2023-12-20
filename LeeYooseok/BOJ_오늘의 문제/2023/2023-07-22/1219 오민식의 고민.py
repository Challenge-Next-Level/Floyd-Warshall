from collections import defaultdict, deque

N, S, E, M = map(int, input().split())

edge_list = list()
for _ in range(M):
    edge_list.append(list(map(int, input().split())))

profit_list = list(map(int, input().split()))

# 각 노드까지의 수익 최대값 리스트
result = [-1e9 for _ in range(N)]
# 시작 노드의 수익 최대값
result[S] = profit_list[S]

# edge 에 profit 반영해서 업데이트
for edge_idx in range(M):
    s, e, c = edge_list[edge_idx]
    edge_list[edge_idx][2] = profit_list[e] - c

# 벨만 포드 수행
for _ in range(N - 1):
    for s, e, c in edge_list:
        # edge 의 시작 노드에 방문할 수 있고, 수익을 더 높일 수 있으면
        if result[s] != -1e9 and result[e] < result[s] + c:
            result[e] = result[s] + c

# 양수 사이클에 종료 노드가 포함되어 있는지 확인
def bfs(start, end):
    dq = deque()
    dq.append(start)

    visited = [False for _ in range(N)]
    visited[start] = True

    while dq:
        now_node = dq.popleft()
        # 현재 탐색하는 노드가 종료 노드이면,
        # 양수 사이클에 종료 노드가 포함된다는 의미
        if now_node == end:
            return True
        for s, e, c in edge_list:
            if s == now_node:
                if not visited[e]:
                    visited[e] = True
                    dq.append(e)

    return False

isPositiveCycle = False
for s, e, c in edge_list:
    # 양수 사이클 존재 시,
    if result[s] != -1e9 and result[e] < result[s] + c:
        if bfs(s, E):
            isPositiveCycle = True
            break

if result[E] == -1e9:
    print("gg") # 종료 노드에 도달 할 수 없음
else:
    if isPositiveCycle:
        print("Gee") # 무한 금액 벌 수 있음
    else:
        print(result[E])

