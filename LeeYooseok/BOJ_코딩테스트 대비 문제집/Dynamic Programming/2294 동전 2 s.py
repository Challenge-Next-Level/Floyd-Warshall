import sys

n, k = map(int, input().split())
coin_list = list()
# 인덱스 k 까지 생성
dp = [-1] * (k + 1)

for _ in range(n):
    coin = int(input())
    coin_list.append(coin)

    # dp 배열에 coin 을 만들 수 있는 동전의 최소 개수 : 1
    if coin <= k:
        dp[coin] = 1

# 1 부터 k 까지 최소 개수 구하기
for t in range(1, k+1):
    temp_min = sys.maxsize
    for c in coin_list:
        # c 로 t를 만들  수 있고, t-c 도 만들 수 있어야 한다.
        if c <= t and dp[t-c] != -1:
            temp_min = min(temp_min, dp[t-c] + 1)

    if temp_min != sys.maxsize:
        if dp[t] != -1:
            dp[t] = min(temp_min, dp[t])
        else:
            dp[t] = temp_min
print(dp[k])


