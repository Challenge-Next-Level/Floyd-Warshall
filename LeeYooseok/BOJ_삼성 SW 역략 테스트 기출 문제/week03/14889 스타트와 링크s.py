# 시간초과 안뜨게

import sys

input = sys.stdin.readline

n = int(input())
div_n = int(n//2)
nums = [i for i in range(n)]

skills = [list(map(int, input().split())) for _ in range(n)]

result = sys.maxsize

team = [0] * (n // 2)

power_start = 0
power_link = 0

checked_teams = list()


def makeTeam(level, begin):
    global result, power_start, power_link
    if level == div_n:

        if team not in checked_teams:
            start = team
            link = list(set(nums) - set(team))

            power_start, power_link = 0, 0

            check(start, 0, 0, 's')
            check(link, 0, 0, 'l')

            checked_teams.append([item for item in start])
            checked_teams.append([item for item in link])

            result = min(result, abs(power_start - power_link))

        return

    for i in range(begin, n):
        team[level] = i
        makeTeam(level + 1, i + 1)


pair = [0] * 2


def check(team, begin, idx, t):
    global power_start, power_link
    if idx == 2:
        temp = 0
        temp += skills[pair[0]][pair[1]]
        temp += skills[pair[1]][pair[0]]
        if t == 's':
            power_start += temp
        else:
            power_link += temp
        return

    for i in range(begin, len(team)):
        pair[idx] = team[i]
        check(team, i + 1, idx + 1, t)


makeTeam(0, 0)

print(result)
