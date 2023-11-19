N, K = map(int, input().split())

stone_list = list(map(int, input().split()))

dp = [True]

for j in range(1, N):
    for i in range(j):
        # i 번째 돌을 갈 수 있다면, -> i 번째 돌에서 시작할 수 있다면,
        if dp[i]:
            need_power = (j - i) * (1 + abs(stone_list[i] - stone_list[j]))
            if need_power <= K:
                dp.append(True)
                break
    if len(dp) != j + 1:
        dp.append(False)
if dp[-1]:
    print("YES")
else:
    print("NO")