N, M, K = map(int, input().split())
# 와우도 : N + 1
graph = dict()

road_list = list(map(int, input().split()))

graph[N+1] = list()

for i in range(len(road_list)):
    graph[i+1] = [[N+1, road_list[i]]]
    graph[N+1].append([i+1, road_list[i]])

