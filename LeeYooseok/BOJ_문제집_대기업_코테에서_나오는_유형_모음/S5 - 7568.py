import sys

input = sys.stdin.readline

N = int(input())

player_list = list()
for _ in range(N):
    player_list.append(list(map(int, input().split())))

player_win_lose = [[0 for _ in range(N)] for _ in range(N)]

for player_1_idx in range(N):
    player_1 = player_list[player_1_idx]
    for player_2_idx in range(player_1_idx + 1, N):
        player_2 = player_list[player_2_idx]

        if player_1[0] < player_2[0] and player_1[1] < player_2[1]:
            player_win_lose[player_1_idx][player_2_idx] = 1
        elif player_1[0] > player_2[0] and player_1[1] > player_2[1]:
            player_win_lose[player_2_idx][player_1_idx] = 1

answer = list()
for i in range(N):
    answer.append(sum(player_win_lose[i]) + 1)

print(*answer)

