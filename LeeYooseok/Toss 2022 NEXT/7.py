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

# dp 활용
def new_solution(money, stocks):
    new_answer = 0

    dp = []

    return new_answer


print(solution(10, [[1, 1], [3, 5], [3, 5], [4, 9]]))
