# 각 케이스 마다 tree를 만들고 bfs 탐색을 통해 한 번에 모든 노드를 방문할 수 있는지 체크하려 했음
# 결론은 '시간초과'
# 단절선, 단절점이 어떤 조건에서 가능할까? 만 알면 간단하게 풀 수 있었음
import sys

n = int(input())
node = [[] for _ in range(n+1)]
for _ in range(n-1): # node의 연결관계 만들기
    start, end = map(int, sys.stdin.readline().split())
    node[start].append(end)
    node[end].append(start)

m = int(input())
for _ in range(m):
    t, k = map(int, sys.stdin.readline().split())
    if t == 1: # 한 노드에 연결된 간선이 2개 이상일 때 단절점이 된다.
        if len(node[k]) == 1:
            print("no")
        else:
            print("yes")
    else: # 사이클이 존재하지 않는 트리에서 모든 간선은 단절선이 된다.
        print("yes")