import sys

n = int(input())
egg = []
for _ in range(n):
    hp, attack = map(int, sys.stdin.readline().split())
    egg.append([hp, attack])

answer = 0


def egg_break(eggs, breaked, index):
    global answer
    idx = -1
    while index < n and eggs[index][0] <= 0:
        index += 1
    if index >= n:
        answer = max(answer, breaked)
        return
    else:
        idx = index # 손에 쥔 계란
    for i in range(n): # 부딪힐 계란
        if i == idx or eggs[i][0] <= 0:
            continue
        count = 0
        leftEggHp, leftEggAttack = eggs[idx] # 손에 쥔 계란
        rightEggHp, rightEggAttack = eggs[i] # 부딪힐 계란
        eggs[idx][0] -= rightEggAttack
        eggs[i][0] -= leftEggAttack
        if eggs[idx][0] <= 0:
            count += 1
        if eggs[i][0] <= 0:
            count += 1
        egg_break(eggs, breaked + count, idx + 1) # dfs 탐색
        eggs[idx][0] += rightEggAttack
        eggs[i][0] += leftEggAttack
    answer = max(answer, breaked)
    return


egg_break(egg, 0, 0)
print(answer)