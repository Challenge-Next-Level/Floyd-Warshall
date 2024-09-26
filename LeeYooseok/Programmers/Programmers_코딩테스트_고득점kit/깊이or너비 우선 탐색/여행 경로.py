# 모든 티켓을 사용하지 못했다면, 다른 경로 탐색 필요 -> dfs

from collections import defaultdict

answer = []

def solution(tickets):

    graph = defaultdict(list)
    for ticket_idx in range(len(tickets)):
        start, end = tickets[ticket_idx]
        graph[start].append([end, ticket_idx])

    for key, values in graph.items():
        values.sort()

    def dfs(path, used_tickets_cnt, visited):
        global answer

        if answer:
            return
        if used_tickets_cnt == len(tickets):
            answer = path
            return

        for next_airport, next_ticket_idx in graph[path[-1]]:
            if visited[next_ticket_idx]:
                continue

            visited[next_ticket_idx] = True
            dfs(path + [next_airport], used_tickets_cnt + 1, visited)
            visited[next_ticket_idx] = False


    dfs(["ICN"], 0, [False for _ in range(len(tickets))])

    return answer
