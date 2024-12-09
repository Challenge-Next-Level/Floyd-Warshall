N, M = map(int, input().split())
edge_list = list()
distance = [1e9 for _ in range(N + 1)]

for _ in range(M):
    A, B, C = map(int, input().split())
    edge_list.append([A, B, C])

def solve(start_node):
    # 시작 노드에 대해서 초기화
    distance[start_node] = 0

    # 전체 노드에 대해서 반복
    for i in range(N):
        # 매 반복마다 '모든 간선'을 확인한다.
        for j in range(M):
            start, end, time = edge_list[j]

            # 현재 간선을 거쳐서 다른 노드로 이동하는 거리가 더 짧은 경우
            if distance[start] != 1e9 and distance[end] > distance[start] + time:
                distance[end] = distance[start] + time
                # 마지막 노드에서도 값이 갱신된다면 음수 순환이 존재
                if i == N - 1:
                    return True

    return False

negative_cycle = solve(1)

if negative_cycle:
    print("-1")
else:
    for i in range(2, N + 1):
        if distance[i] == 1e9:
            print("-1")
        else:
            print(distance[i])