import sys

input = sys.stdin.readline

T = int(input())

for _ in range(T):
    N = int(input())
    graph = [[] for _ in range(N+1)]

    for _ in range(N-1):
        A, B = map(int, input().split())
        graph[B].append(A)

    node_1, node_2 = map(int, input().split())

    node_1_parent = [node_1]
    node_2_parent = [node_2]

    now_node = node_1
    while True:
        if graph[now_node]:
            node_1_parent.append(graph[now_node][0])
        else:
            break
        now_node = graph[now_node][0]

    now_node = node_2
    while True:
        if graph[now_node]:
            node_2_parent.append(graph[now_node][0])
        else:
            break
        now_node = graph[now_node][0]


    flag = False
    for n1p in node_1_parent:
        if flag:
            break
        for n2p in node_2_parent:
            if n1p == n2p:
                print(n1p)
                flag = True
                break

