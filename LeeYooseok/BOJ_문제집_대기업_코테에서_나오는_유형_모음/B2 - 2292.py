# 1 -> 2 -> 3 -> 4
# 1 -> 7 -> 19 -> 37
#   6 -> 12 -> 18

N = int(input())

dp = [0, 1]
add_num = 6
answer = 1
while True:
    if dp[-1] >= N:
        break

    dp.append(dp[-1] + add_num)
    add_num += 6
    answer += 1

print(answer)
