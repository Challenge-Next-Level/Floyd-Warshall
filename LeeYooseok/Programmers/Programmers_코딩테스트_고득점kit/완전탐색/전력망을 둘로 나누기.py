from collections import defaultdict, deque

graph = defaultdict(list)


def solution(n, wires):
    global graph

    answer = 1e9
    for idx in range(len(wires)):
        remove_wire = wires[idx]
        graph = defaultdict(list)
        for wire_idx in range(len(wires)):
            if idx != wire_idx:
                wire = wires[wire_idx]
                graph[wire[0]].append(wire[1])
                graph[wire[1]].append(wire[0])

        a_cnt = dfs(remove_wire[0], n)
        b_cnt = dfs(remove_wire[1], n)

        answer = min(answer, abs(a_cnt - b_cnt))

    return answer


def dfs(start_node, total_node_count):
    visited = [False for _ in range(total_node_count + 1)]
    queue = deque()
    queue.append(start_node)
    count = 0

    while queue:
        now_node = queue.popleft()
        visited[now_node] = True
        count += 1

        for next_node in graph[now_node]:
            if not visited[next_node]:
                queue.append(next_node)

    return count