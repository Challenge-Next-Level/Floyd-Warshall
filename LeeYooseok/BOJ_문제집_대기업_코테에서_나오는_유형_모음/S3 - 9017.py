# 한 팀은 여섯 명의 선수로 구성되며, 팀 점수는 상위 네 명의 주자의 점수를 합하여 계산
# 가장 낮은 점수를 얻는 팀이 우승
# 여섯 명의 주자가 참가하지 못한 팀은 점수 계산에서 제외
# 동점의 경우에는 다섯 번째 주자가 가장 빨리 들어온 팀이 우승

import sys

input = sys.stdin.readline

T = int(input())
for _ in range(T):
    N = int(input())
    player_rank = list(map(int, input().split()))

    M = max(player_rank)
    team_player = [0 for _ in range(M + 1)]

    # 각 팀의 선수 수
    for team in player_rank:
        team_player[team] += 1

    # 점수, 다섯번째 주자의 순위, 들어온 선수의 수, 팀 번호
    team_score = [[0, 0, 0, i] for i in range(M + 1)]

    now_rank = 1
    for i in range(N):
        team = player_rank[i]

        if team_player[team] < 6:
            continue

        if team_score[team][2] < 4:
            team_score[team][0] += now_rank
        team_score[team][2] += 1

        if team_score[team][2] == 5:
            team_score[team][1] = now_rank

        now_rank += 1

    team_score.sort()

    for i in range(1, M + 1):
        if team_score[i][0] != 0:
            print(team_score[i][3])
            break