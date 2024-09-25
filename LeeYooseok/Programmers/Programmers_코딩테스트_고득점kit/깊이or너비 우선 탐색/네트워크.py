from collections import defaultdict, deque


def solution(n, computers):
    graph = defaultdict(list)
    for i in range(n):
        for j in range(i + 1, n):
            if computers[i][j] == 1:
                graph[i].append(j)
                graph[j].append(i)

    answer = 0

    visited = [False for _ in range(n)]

    for i in range(n):
        if not visited[i]:

            queue = deque()
            queue.append(i)
            visited[i] = True

            while queue:
                now_node = queue.popleft()

                for next_node in graph[now_node]:
                    if visited[next_node]:
                        continue

                    queue.append(next_node)
                    visited[next_node] = True
            answer += 1

    return answer
