import heapq

T = int(input())

for _ in range(T):
    max_que = list()
    min_que = list()

    Q = int(input())

    visited = [False] * Q

    for q in range(Q):
        cmd, param = input().split()

        if cmd == 'I':
            heapq.heappush(min_que, (int(param), q))
            heapq.heappush(max_que, (-1 * int(param), q))
            # 숫자 존재 시, True
            visited[q] = True
        else:
            if param == '1':
                # max_que 가 존재하고, max_que 의 맨 앞 원소의 visited 가 False 이면 pop
                while max_que and not visited[max_que[0][1]]:
                    heapq.heappop(max_que)

                if max_que:
                    # 숫자 제거 하면 False
                    visited[max_que[0][1]] = False
                    heapq.heappop(max_que)
            else:
                while min_que and not visited[min_que[0][1]]:
                    heapq.heappop(min_que)
                if min_que:
                    visited[min_que[0][1]] = False
                    heapq.heappop(min_que)

    # 마지막으로 min_que 와 max_que 의 상태를 맞춰줌
    while min_que and not visited[min_que[0][1]]:
        heapq.heappop(min_que)
    while max_que and not visited[max_que[0][1]]:
        heapq.heappop(max_que)

    if not min_que or not max_que:
        print("EMPTY")
    else:
        _max = -max_que[0][0]
        _min = min_que[0][0]
        print(_max, _min)
