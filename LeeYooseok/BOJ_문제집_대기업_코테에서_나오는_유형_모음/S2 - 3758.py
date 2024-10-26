import sys

input = sys.stdin.readline

T = int(input())

for _ in range(T):
    # n : 팀의 개수, k : 문제 개수, t : 자신 팀의 id, m : 제출 횟수
    n, k, t, m = map(int, input().split())

    team_solve = [[0 for _ in range(k + 1)] for _ in range(n + 1)]
    team_dict = {}
    for team_id in range(n + 1):
        # 전체 점수, 제출 횟수, 마지막 제출 시각
        team_dict[team_id] = [0, 0, m + 1]

    for idx in range(m):
        # i : 팀의 id, j : 문제 id, s : 획득 점수
        i, j, s = map(int, input().split())
        if team_solve[i][j] == 0:
            team_dict[i][0] += s
            team_solve[i][j] = s
        else:
            if team_solve[i][j] <= s:
                team_dict[i][0] -= team_solve[i][j]
                team_dict[i][0] += s
                team_solve[i][j] = s
        team_dict[i][2] = idx
        team_dict[i][1] += 1

    answer = 1
    my_team = team_dict[t]
    for i in range(1, n + 1):
        if i != t:
            other_team = team_dict[i]
            if other_team[0] > my_team[0]:
                answer += 1
            elif other_team[0] == my_team[0]:
                if other_team[1] < my_team[1]:
                    answer += 1
                elif other_team[1] == my_team[1]:
                    if other_team[2] < my_team[2]:
                        answer += 1

    print(answer)

