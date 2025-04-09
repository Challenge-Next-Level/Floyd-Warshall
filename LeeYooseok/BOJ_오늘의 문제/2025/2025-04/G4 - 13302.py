N, M = map(int, input().split())
disable_day_list = list()
if M != 0:
    disable_day_list = list(map(int, input().split()))

# 최대 여름방학 일수(100 일) + 5일 : 105, 최대 쿠폰 발행 갯수 : 40
dp = [[-1 for _ in range(40)] for _ in range(106)]


def solve(now_day, coupon_count):
    # 일수 초과 시, return
    if now_day > N:
        return 0

    # 이전에 이미 방문한 경우, 이미 최소값으로 갱신되어 있기 때문에 반환
    if dp[now_day][coupon_count] != -1:
        return dp[now_day][coupon_count]

    # 방문하지 않아도 되는 날은, 다음날로 넘긴다.
    if now_day in disable_day_list:
        dp[now_day][coupon_count] = solve(now_day + 1, coupon_count)
        return dp[now_day][coupon_count]

    # 1일권, 3일권, 5일권 중 가장 값이 싼 금액으로 갱신한다.
    dp[now_day][coupon_count] = min(solve(now_day + 1, coupon_count) + 10000,
                                    solve(now_day + 3, coupon_count + 1) + 25000,
                                    solve(now_day + 5, coupon_count + 2) + 37000)

    # 쿠폰 갯수가 3개 이상일 경우, 쿠폰을 사용하는 경우도 고려한다.
    if coupon_count >= 3:
        dp[now_day][coupon_count] = min(dp[now_day][coupon_count], solve(now_day + 1, coupon_count - 3))

    return dp[now_day][coupon_count]

# 최종적으로 dp[1][0] 에 정답이 담기게 된다.
print(solve(1, 0))