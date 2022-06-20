from itertools import combinations
import sys

n = int(input())
nums = [i for i in range(n)]

skills = [list(map(int, input().split())) for _ in range(n)]

result = sys.maxsize

team = list(combinations(nums, n // 2))

def check(team):
    temp = 0
    pairs = list(combinations(team, 2))
    for p in pairs:
        temp += skills[p[0]][p[1]]
        temp += skills[p[1]][p[0]]
    return temp


checked_teams = list()

for t in team:
    start = t
    link = [x for x in nums if x not in start]

    if start in checked_teams or link in checked_teams:
        continue
    else:
        checked_teams.append(start)
        checked_teams.append(link)

        power_start = check(start)
        power_link = check(link)

        result = min(result, abs(power_start - power_link))

print(result)
