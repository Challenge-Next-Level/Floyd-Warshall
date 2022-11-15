C = int(input())


def solve(n, power):  # n번째 포지션의 선수를 정함, 이전까지의 능력치는 power 였음.
    global answer
    # 이전에 마지막 선수를 정하였다면 return
    if n == 11:
        answer = max(answer, power)
        return

    for p in range(11):
        if not player_use[p] and skill_position[p][n] > 0:
            player_use[p] = True
            solve(n + 1, power + skill_position[p][n])
            player_use[p] = False


position = [-1 for _ in range(11)]
for _ in range(C):
    answer = 0
    skill_position = [list(map(int, input().split())) for _ in range(11)]
    player_use = [False for _ in range(11)]

    solve(0, 0)

    print(answer)
