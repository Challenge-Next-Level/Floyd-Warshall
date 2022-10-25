# 만들 수 있는 모든 팀의 경우의 수를 makeTeam() 으로 구현을 한게 정말 좋은 아이디어
import sys

n = int(input())
S = []
for _ in range(n):
    S.append(list(map(int, sys.stdin.readline().split())))
visit = [False for _ in range(n)]
answer = float('inf')


def calculate():
    teamA, teamB = 0, 0
    for i in range(n):
        for j in range(n):
            if visit[i] and visit[j]:
                teamA += S[i][j]
            elif not visit[i] and not visit[j]:
                teamB += S[i][j]
    global answer
    answer = min(answer, abs(teamA-teamB))
    return


def makeTeam(index):
    if index >= n:
        calculate()
        return
    visit[index] = True
    makeTeam(index+1)
    visit[index] = False
    makeTeam(index+1)


makeTeam(0)
print(answer)