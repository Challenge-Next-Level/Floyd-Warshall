import sys

case = int(input())
for _ in range(case):
    player = []
    for _ in range(11):
        player.append(list(map(int, sys.stdin.readline().split())))
    visit = [False] * 11  # 포지션 visit
    answer = 0

    def dfs(count, total):
        if count >= 11: # 11명 포지션 완성시
            global answer
            answer = max(answer, total)
        for i in range(11):
            if visit[i]:
                continue
            if player[count][i] != 0:
                visit[i] = True
                dfs(count+1, total+player[count][i])
                visit[i] = False
        return


    # 첫 번째 선수 기준으로 스쿼드 설정
    for i in range(11): # 11개의 포지션
        if player[0][i] != 0:
            visit[i] = True
            dfs(1, player[0][i])
            visit[i] = False

    print(answer)
