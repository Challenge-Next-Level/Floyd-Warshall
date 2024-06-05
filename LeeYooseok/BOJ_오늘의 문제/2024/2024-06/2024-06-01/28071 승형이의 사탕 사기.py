# 최대 M 개의 사탕 상자를 가져가서 K의 배수를 만들어야 함.
# 이때, 가져간 사탕의 개수가 최대가 되도록 해야함.

N, M, K = map(int, input().split())
candy_cnt = list(map(int, input().split()))

dp = [1e9 for _ in range(90001)]  # 90000 : 만들 수 있는 최대 사탕 개수
# dp[i] = 사탕을 총 i개 가져가기 위한 총 상자 개수
# dp[j] = min(dp[j], dp[j - N_j] + 1)
dp[0] = 0

for i in range(N):
    candy = candy_cnt[i]
    # j 개의 사탕을 만드는 방법 : j-candy 개의 사탕을 만드는 방법 + candy 개의 사탕 박스 한개 선택
    for j in range(candy, 90001):
        dp[j] = min(dp[j], dp[j - candy] + 1)

for k in range(90000, -1, -1):
    if k % K == 0 and dp[k] <= M:
        print(k)
        exit()

