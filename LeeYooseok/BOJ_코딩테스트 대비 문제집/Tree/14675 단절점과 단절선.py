import sys

input = sys.stdin.readline

N = int(input())

graph = [[] for _ in range(N+1)]

for _ in range(N-1):
    a, b = map(int, input().split())

    graph[a].append(b)
    graph[b].append(a)

q = int(input())

for _ in range(q):
    t, k = map(int, input().split())

    if t == 1:
        # 단절점인지 확인 - 연결된 간선이 2개 이상이면 단절점이다.
        if len(graph[k]) >= 2:
            print("yes")
        else:
            print("no")
    else:
        # 단절선인지 확인 - 무조건 단절 선 이다.
        print("yes")