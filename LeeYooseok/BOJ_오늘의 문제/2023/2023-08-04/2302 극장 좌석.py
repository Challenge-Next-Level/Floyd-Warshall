N = int(input())

sit_list = [0 for _ in range(N + 1)] + [-1]

M = int(input())

for m in range(M):
    fixed_sit = int(input())

    sit_list[fixed_sit] = -1

sit_space_list = list()
start = 0
for i in range(1, N + 2):
    if sit_list[i] == -1:
        sit_space_list.append(i - start - 1)
        start = i

print(sit_space_list)

max_space = max(sit_space_list)

dp = [0 for _ in range(max_space + 1)]

dp[0] = 1
if max_space >= 1:
    dp[1] = 1
if max_space >= 2:
    dp[2] = 2

if max_space > 2:
    for i in range(3, max_space + 1):
        dp[i] = sum(dp[i-2:i])

answer = 1
for space in sit_space_list:
    answer *= dp[space]

print(answer)
