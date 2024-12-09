import sys

input = sys.stdin.readline

def solve():
    for i in range(N):
        for j in range(len(edge_list)):
            start, end, time = edge_list[j]
            if distance_list[end] > distance_list[start] + time:
                distance_list[end] = distance_list[start] + time
                if i == N - 1:
                    return True

    return False


TC = int(input())
for _ in range(TC):
    N, M, W = map(int, input().split())

    edge_list = list()
    distance_list = [1e9 for _ in range(N + 1)]

    for _ in range(M):
        S, E, T = map(int, input().split())
        edge_list.append([S, E, T])
        edge_list.append([E, S, T])

    for _ in range(W):
        S, E, T = map(int, input().split())
        edge_list.append([S, E, -T])
    if solve():
        print("YES")
    else:
        print("NO")