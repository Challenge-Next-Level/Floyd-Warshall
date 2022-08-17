# 통과 - 가장 많이 탐험할 수 있는 던전의 개수 - dp?
import sys


def s(k, num, visited, dungeons):
    global answer
    chk = False
    for idx in range(len(dungeons)):
        if not visited[idx]:
            _d = dungeons[idx]
            if _d[0] <= k:
                visited[idx] = True
                s(k - _d[1], num + 1, visited, dungeons)
                visited[idx] = False
                chk = True
    if not chk:
        answer = max(answer, num)
        return


def solution(k, dungeons):
    global answer
    answer = 0
    s(k, 0, [False for _ in range(len(dungeons))], dungeons)
    return answer


print(solution(80, [[80, 20], [50, 40], [30, 10]]))

def new_solution(k, dungeons):
    n = len(dungeons)

    dp = [[sys.maxsize for _ in range(k+1)] for _ in range(n)]

    for i in range(n):
        for j in range(1, k+1):
            min_health = dungeons[i][0]
            health = dungeons[i][1]

            # 현재 체력 < 현재 던전의 최소 필요 체력
            if j < min_health:
                dp[i][j] = dp[i][j-1]
            else:
                dp[i][j] = min(dp[i][j-1], dp[i][j-health] + health)
