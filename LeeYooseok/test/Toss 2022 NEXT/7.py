# 통과 못함 - 시간 초과
# money : 갖고있는 돈, stocks : [[가치, 비용]]
# 이익을 가장 크게하는 경우
def s(m, profit, visited, stocks):
    global answer
    chk = False
    for idx in range(len(stocks)):
        if not visited[idx]:
            _s = stocks[idx]
            if _s[1] <= m:
                visited[idx] = True
                s(m - _s[1], profit + _s[0], visited, stocks)
                visited[idx] = False
                chk = True
    if not chk:
        answer = max(answer, profit)
        return


def solution(money, stocks):
    global answer
    answer = 0
    s(money, 0, [False for _ in range(len(stocks))], stocks)

    return answer


print(solution(10, [[1, 1], [3, 5], [3, 5], [4, 9]]))


# dp 활용
def new_solution(money, stocks):
    n = len(stocks)

    # 행에는 주식의 종류, 열에는 현재 갖고있는 돈 으로 dp 배열을 만들어 줍니다.
    dp = [[0 for _ in range(money + 1)] for _ in range(n)]

    # 각각의 주식을 선택할 때마다 가능한 금액으로 얻을 수 있는 최고의 가치를 구할 수 있도록 해준다.
    for i in range(n):
        for j in range(1, money + 1):
            value = stocks[i][0]
            price = stocks[i][1]

            # 현재 가능한 돈의 액수 보다, 주식의 비용이 더 크면
            if j < price:
                # 해당 주식은 선택할 수 없다.
                # 즉 같은 비용, 이전 주식 단계의 동일 금액의 최대 가치를 그대로 가져온다.
                dp[i][j] = dp[i - 1][j]
            # 해당 주식을 선택할 수 있다면
            else:
                # (같은 비용, 이전 주식 단계의 최대 가치) 와 ((이전 주식, 같은 비용 - 현재 주식의 비용) + 현재 주식의 가치) 을 비교하여 최대 가치를 수정해준다.
                dp[i][j] = max(dp[i - 1][j], dp[i - 1][j - price] + value)

    # 갖고있는 금액으로 모든 주식의 선택 여부를 다 결정했을때의 최대 가치를 출력한다.
    new_answer = dp[n - 1][money]
    return new_answer


print(new_solution(10, [[1, 1], [3, 5], [3, 5], [4, 9]]))

