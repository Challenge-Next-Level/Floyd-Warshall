import sys

input = sys.stdin.readline

N = int(input())
SCV_list = list(map(int, input().split()))
while len(SCV_list) < 3:
    SCV_list.append(0)

# 최대 체력 60
# dp[x][y][z] = SCV1 의 체력이 x, SCV2 의 체력이 y, SCV3 의 체력이 z 까지 도달할 때의 최소 횟수
dp = [[[0 for _ in range(61)] for _ in range(61)] for _ in range(61)]

# 공격 경우의 수
attack_list = [(-9, -3, -1), (-9, -1, -3), (-3, -9, -1), (-3, -1, -9), (-1, -9, -3), (-1, -3, -9)]


def dfs(scv1, scv2, scv3):
    if scv1 == 0 and scv2 == 0 and scv3 == 0:
        return 0

    # 이미 방문했다면
    if dp[scv1][scv2][scv3] != 0:
        return dp[scv1][scv2][scv3]

    next_dp = 1e9

    # 가능한 공격 경우의 수 중, 가장 최소의 공격 횟수를 찾는다.
    for attack in attack_list:
        next_dp = min(dfs(max(scv1 + attack[0], 0), max(scv2 + attack[1], 0), max(scv3 + attack[2], 0)), next_dp)

    # 공격을 한번 해주기 때문에 1 을 더해준다.
    dp[scv1][scv2][scv3] = 1 + next_dp
    return dp[scv1][scv2][scv3]


print(dfs(SCV_list[0], SCV_list[1], SCV_list[2]))
