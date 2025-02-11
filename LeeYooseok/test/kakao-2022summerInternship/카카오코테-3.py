# dp 문제
# problems : [alp_req, cop_req, alp_rwd, cop_rwd, cost]

# 현재 내가 풀 수 있는 문제 목록을 확인
def check(alp, clp, problems):
    temp = list()
    for p in problems:
        if p[0] <= alp and p[1] <= clp:
            temp.append(p)

    return temp

# 가장 높은 난이도의 문제 확인
def getMaxReq(problems):
    max_alp_req = 0
    max_cop_req = 0
    for p in problems:
        max_alp_req = max(max_alp_req, p[0])
        max_cop_req = max(max_cop_req, p[1])
    return max_alp_req, max_cop_req

def solution(alp, cop, problems):
    # 가장 높은 난이도의 문제 확인
    max_alp_req, max_cop_req = getMaxReq(problems)
    dp = []
    for i in range(max_req):
        dp.append(max_req)
    # 현재 내가 풀 수 있는 문제 목록을 확인

    #