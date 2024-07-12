T = int(input())

operator_list = [" ", "+", "-"]


def dfs(idx, expression):
    if idx == N:
        # 결과가 0 인지 확인
        value = eval(expression.replace(" ", ""))
        if value == 0:
            answer_list.append(expression)
    else:
        # 연산자 추가하기
        for operator in operator_list:
            dfs(idx + 1, expression + operator + str(idx + 1))


for _ in range(T):
    N = int(input())
    answer_list = list()
    dfs(1, "1")
    for answer in answer_list:
        print(answer)
    print()
