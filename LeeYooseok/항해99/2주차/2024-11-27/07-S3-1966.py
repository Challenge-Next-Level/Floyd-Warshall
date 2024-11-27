from collections import deque

T = int(input())
for _ in range(T):
    N, M = map(int, input().split())
    priority_list = list(map(int, input().split()))
    # [idx, 우선 순위]
    priority_list = [[i, priority_list[i]] for i in range(N)]
    priority_list = deque(priority_list)

    answer = 0
    while priority_list:
        # queue 의 앞에서부터 처리한다.
        now_idx, now_priority = priority_list.popleft()

        printable = True
        if priority_list:
            # 남아 있는 문서들 중 가장 높은 우선 순위
            highest_priority = max([priority[1] for priority in priority_list])

            # 현재 문서의 우선 순위 < 남아 있는 문서들 중 가장 높은 우선 순위
            if now_priority < highest_priority:
                # queue 의 가장 뒤에 현재 문서를 추가한다.
                priority_list.append([now_idx, now_priority])
                priority_list.append([now_idx, now_priority])
                printable = False

        # 출력이 가능하면
        if printable:
            # 출력 순서 + 1
            answer += 1
            # 찾고자 하는 문서
            if now_idx == M:
                print(answer)