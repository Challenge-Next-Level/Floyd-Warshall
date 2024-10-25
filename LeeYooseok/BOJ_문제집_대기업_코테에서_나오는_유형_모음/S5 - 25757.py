import sys

input = sys.stdin.readline

game_info = {"Y": 2, "F": 3, "O": 4}

N, game = input().split()

N = int(N)
player_set = set()
for _ in range(N):
    player_set.add(input())

print(len(player_set) // (game_info[game] - 1))

