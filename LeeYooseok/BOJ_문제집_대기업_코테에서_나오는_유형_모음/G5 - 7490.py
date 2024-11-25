T = int(input())

operator_list = [" ", "+", "-"]


def solve(idx, expression):
    # 결과 확인
    if idx == N:
        value = eval(expression.replace(" ", ""))
        if value == 0:
            answer_list.append(expression)
    else:
        # 연산자 추가
        for operator in operator_list:
            solve(idx + 1, expression + operator + str(idx + 1))


for _ in range(T):
    N = int(input())
    answer_list = list()
    solve(1, "1")
    for answer in answer_list:
        print(answer)
    print()