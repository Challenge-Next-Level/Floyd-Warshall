import sys

N = int(input())
num_list = list(map(int, input().split()))
operator_list = list(map(int, input().split())) # +, -, x, %

min_answer = sys.maxsize
max_answer = -1 * sys.maxsize

def solve(cnt, total, plus, minus, mul, div):
    global min_answer, max_answer

    if cnt == N:
        min_answer = min(total, min_answer)
        max_answer = max(total, max_answer)
        return

    if plus > 0:
        solve(cnt + 1, total + num_list[cnt], plus - 1, minus, mul, div)

    if minus > 0:
        solve(cnt + 1, total - num_list[cnt], plus, minus - 1, mul, div)

    if mul > 0:
        solve(cnt + 1, total * num_list[cnt], plus, minus, mul - 1, div)

    if div > 0:
        solve(cnt + 1, int(total / num_list[cnt]), plus, minus, mul, div - 1)


solve(1, num_list[0], operator_list[0], operator_list[1], operator_list[2], operator_list[3])
print(max_answer)
print(min_answer)