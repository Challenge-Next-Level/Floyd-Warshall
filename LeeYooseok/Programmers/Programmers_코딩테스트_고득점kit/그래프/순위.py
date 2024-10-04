def solution(n, results):
    answer = 0

    chart = [[0 for _ in range(n)] for _ in range(n)]
    for win, lose in results:
        chart[win - 1][lose - 1] = 1
        chart[lose - 1][win - 1] = -1

    # 모든 선수에 대해서
    for i in range(n):
        # i 번째 선수가 이긴 선수들
        loser_list = list()
        for j in range(n):
            if chart[i][j] == 1:
                loser_list.append(j)

        # j가 이긴 선수는 i 가 다 이길 수 있음
        while loser_list:
            loser = loser_list.pop()
            for next_j in range(n):
                if chart[loser][next_j] == 1 and chart[i][next_j] == 0:
                    chart[i][next_j], chart[next_j][i] = 1, -1
                    loser_list.append(next_j)

    for c in chart:
        # 0(자기 자신) 이 1개라면, 순위가 확실한 선수
        if c.count(0) == 1:
            answer += 1

    return answer