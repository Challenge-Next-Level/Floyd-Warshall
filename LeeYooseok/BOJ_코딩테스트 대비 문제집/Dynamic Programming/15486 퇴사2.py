d = int(input())
time = [0]
price = [0]
for _ in range(d):
    t, p = map(int, input().split())
    time.append(t)
    price.append(p)

dp = [0 for _ in range(d + 1)]

# i 번째 날까지 가장 많이 벌 수 있는 금액
k = 0
for i in range(d):
    # i 번째 날까지 가장 많이 벌 수 있는 금액 갱신
    k = max(k, dp[i])
    # 현재 상담 종료 일이 d를 넘어가면 continue
    if i + time[i] > d:
        continue

    # 상담 종료일 : i + time[i]
    # 상담 종료일에 가장 많이 벌 수 있는 금액 : k + 현재 상담 시작 or 기존 상담 종료일에 가장 많이 벌 수 있는 금액
    dp[i + time[i]] = max(k + price[i], dp[i + time[i]])

print(max(dp))