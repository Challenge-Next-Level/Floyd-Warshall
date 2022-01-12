# 재귀가 곁들어진 완전탐색 문제... 하 어렵네ㅎ
k = int(input())
oper = input().split()
min_ans, max_ans = "", ""
visit = [0] * 10


def check(a, b, op):
    if op == '<':
        return a < b
    else:
        return a > b


def solve(length, answer):
    if length == k + 1: # 정답의 조건(길이를 만족하면 됨)
        global min_ans, max_ans
        if min_ans == "":
            min_ans = answer
        else:
            max_ans = answer
        return # 이거 안써서 두시간 날림. 리얼임

    for i in range(10): # 0~9 까지의 숫자에 대한 경우의 수 체크
        if visit[i] == 0: # 방문하지 않은 숫자를 본다
            # 1. 첫 번째 숫자는 집어 넣고 본다
            # 2. 그외는 앞에 숫자와 비교 조건을 만족해야 한다
            if length == 0 or check(answer[-1], str(i), oper[length - 1]):
                visit[i] = 1
                solve(length + 1, answer + str(i))
                visit[i] = 0 # 방문 체크 해제도 중요하다


solve(0, "")
print(max_ans)
print(min_ans)