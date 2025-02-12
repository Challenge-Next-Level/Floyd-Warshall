T = int(input())

for _ in range(T):

    # 갤럭시를 가동시키는데 쓰이는 최대 능력치 계산
    def check(agent_list, now_power):
        global answer
        # 종료 조건 : 3개의 능력 (힘, 지능, 민첩)을 한번씩 사용함
        if len(agent_list) == 3:
            # 사용 안한 요원들의 최대 능력을 now_power 에 더해줌.
            for j in range(n):
                if not visited[j]:
                    now_power += graph[j][3]
            # 갤럭시를 가동시키는데 쓰이는 최대 능력치 갱신 후, 함수 종료
            answer = max(answer, now_power)
            return

        # back tracking : 현재 상황에서 최대로 힘을 만들 수 있어도, 현재의 answer 보다 작다면 더 탐색할 가치가 없음. -> 종료
        possible_max = now_power + max_total
        for k in range(len(agent_list)):
            possible_max -= graph[agent_list[k]][k]
            if possible_max <= answer:
                return

        # 다음 요원 선택
        for next_agent in range(n):
            # next_agent 를 사용하지 않았다면,
            if not visited[next_agent]:
                visited[next_agent] = True
                # agent_list 에 추가 후, 다음 힘 계산
                # 다음 힘 : now_power + agent_list 의 len(agent_list) - 1 번째 능력의 힘
                agent_list.append(next_agent)
                check(agent_list, now_power + graph[next_agent][len(agent_list) - 1])
                # agent_list 및 visited 복구
                agent_list.pop()
                visited[next_agent] = False


    # 입력
    n = int(input())

    graph = list()
    total = 0  # 전체 power 합
    max_total = 0  # 각 요원의 최대 power 들의 합
    for _ in range(n):
        a, b, c = map(int, input().split())
        power_list = [a, b, c]
        max_power = max(power_list)

        graph.append([a, b, c, max_power])

        total += sum(power_list)
        max_total += max_power

    # n < 3 이면, 갤럭시 가동 못시킴 -> return -1
    if n < 3:
        print(-1)
        continue

    answer = -1e9  # 갤럭시를 가동시키는데 쓰이는 최대 능력치
    visited = [False for _ in range(n)]  # agent 사용했는지 확인

    # i 번째 agent 의 첫번째 능력을 사용 하는 상태에서 함수 시작
    for i in range(n):
        visited[i] = True
        check([i], graph[i][0])
        visited[i] = False  # visited 복구

    print(total - answer)
