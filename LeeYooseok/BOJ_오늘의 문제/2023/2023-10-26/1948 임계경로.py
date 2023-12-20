from collections import defaultdict, deque

n = int(input())
m = int(input())

time = [0 for _ in range(n + 1)]
# 위상정렬을 통해 모든 사람이 도착하는 시간 구함
graph = defaultdict(list)
# backward of graph
back_graph = defaultdict(list)

# 진입 차수
in_degree = [0 for _ in range(n + 1)]
for _ in range(m):
    s, d, c = map(int, input().split())
    graph[s].append([d, c])
    back_graph[d].append([s, c])
    in_degree[d] += 1

# 출발, 도착
start, end = map(int, input().split())

queue = deque([start])

while queue:
    now_node = queue.popleft()

    for next_node, cost in graph[now_node]:
        in_degree[next_node] -= 1

        time[next_node] = max(time[next_node], time[now_node] + cost)

        # 선행 도로를 모두 지나갔을 때
        if in_degree[next_node] == 0:
            queue.append(next_node)

# back tracking
queue = deque([end])
visited = [False for _ in range(n + 1)]
cnt = 0
while queue: # 도착점에서 시작점으로
    now_node = queue.popleft()
    for prior_node, cost in back_graph[now_node]:
        # 도착점 까지의 비용에서 시작점의 비용을 뺐을 때 그 간선 비용과 같다면
        if time[now_node] - time[prior_node] == cost:
            cnt += 1
            # 중복 방문 제거
            if not visited[prior_node]:
                queue.append(prior_node)
                visited[prior_node] = True

print(time[end])
print(cnt)