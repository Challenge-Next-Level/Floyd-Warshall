from collections import deque, defaultdict

T = int(input())
for _ in range(T):
    K, M, P = map(int, input().split())

    graph = defaultdict(list)
    # 진입차수
    indegree = [0] * (M + 1)

    for _ in range(P):
        a, b = map(int, input().split())
        graph[a].append(b) # 정점 a에서 정점 b로 이동 가능
        indegree[b] += 1

    # 위상정렬 함수
    def topology_sort():
        dq = deque()
        strahler_list = [[] for _ in range(M + 1)]

        # 처음 시작할 때는 진입차수가 0인 노드를 큐에 삽입
        for i in range(1, M + 1):
            if indegree[i] == 0:
                dq.append([i, 1])
                strahler_list[i].append(1)

        while dq:
            now_node, now_num = dq.popleft()

            # 해당 원소와 연결된 노드들의 진입차수에서 1 빼기
            for i in graph[now_node]:
                indegree[i] -= 1
                strahler_list[i].append(now_num)

                # 새롭게 진입차수가 0이 되는 노드를 큐에 삽입
                if indegree[i] == 0:
                    max_strahler_num = max(strahler_list[i])
                    max_strahler_num_cnt = strahler_list[i].count(max_strahler_num)
                    if max_strahler_num_cnt >= 2:
                        max_strahler_num += 1
                    strahler_list[i] = max_strahler_num
                    dq.append([i, max_strahler_num])
        return strahler_list[M]
    print(K, topology_sort())
