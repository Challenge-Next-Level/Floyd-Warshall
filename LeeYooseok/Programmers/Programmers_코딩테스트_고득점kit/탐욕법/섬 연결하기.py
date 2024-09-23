def solution(n, costs):
    answer = 0
    costs.sort(key=lambda x: x[2])  # 비용을 기준으로 오름차순 정렬
    connect = set([costs[0][0]])  # 간선 연결 정보를 담는 set
    while len(connect) != n:
        for cost in costs:
            if cost[0] in connect and cost[1] in connect:  # 사이클 형성을 막음
                continue
            if cost[0] in connect or cost[1] in connect:  # 기존 간선과 이어져야 함
                connect.update([cost[0], cost[1]])
                answer += cost[2]
                break

    return answer