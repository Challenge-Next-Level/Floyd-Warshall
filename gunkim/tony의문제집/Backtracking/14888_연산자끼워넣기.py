# 백트래킹의 느낌보다는 일반적인 dfs의 느낌이 강하게 난다.
n = int(input())
numbers = list(map(int, input().split()))
oper = list(map(int, input().split()))

min_value = float('inf')
max_value = -float('inf')


def calculate(index, sign, current_value):
    b = numbers[index+1]
    if sign == 0: # 덧셈
        return current_value + b
    elif sign == 1: # 뺄셈
        return current_value - b
    elif sign == 2: # 곱셉
        return current_value * b
    else: # 나눗셈
        quotient = abs(current_value) // abs(b)
        if current_value < 0:
            quotient *= -1
        if b < 0:
            quotient *= -1
        return quotient


def dfs(op, idx, result):
    if idx + 1 >= n: # 그나마 백트래킹? 그냥 종료 필수 조건이긴 함.
        global min_value, max_value
        min_value = min(min_value, result)
        max_value = max(max_value, result)
        return
    for i in range(4):
        if op[i] <= 0:
            continue
        op[i] -= 1
        dfs(op, idx+1, calculate(idx, i, result))
        op[i] += 1


for i in range(4):
    if oper[i] <= 0:
        continue
    oper[i] -= 1
    dfs(oper, 1, calculate(0, i, numbers[0]))
    oper[i] += 1

print(max_value)
print(min_value)