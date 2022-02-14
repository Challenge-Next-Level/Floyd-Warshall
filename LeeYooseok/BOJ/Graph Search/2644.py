n = int(input())
target_x, target_y = map(int, input().split())
m = int(input())
graph = [[] for _ in range(n + 1)]
visited = [0]*(n+1)
finish = False

for _ in range(m):
    input_x, input_y = map(int, input().split())

    if input_y not in graph[input_x]:
        graph[input_x].append(input_y)

    if input_x not in graph[input_y]:
        graph[input_y].append(input_x)

# 탐색
temp = list()
temp.append([target_x, 0])

while temp:
    x, curr = temp.pop(0)
    visited[x] = 1

    if x == target_y:
        print(curr)
        finish = True
        break

    for i in range(len(graph[x])):
        if visited[graph[x][i]] != 1:
            temp.append([graph[x][i], curr + 1])

if not finish:
    print(-1)