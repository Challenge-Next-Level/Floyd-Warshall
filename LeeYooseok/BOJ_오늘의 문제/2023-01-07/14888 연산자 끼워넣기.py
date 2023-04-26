import sys

N = int(input())
num_list = list(map(int, input().split()))
operator_list = list(map(int, input().split()))

answer_min, answer_max = sys.maxsize, -1 * sys.maxsize


def dfs(cnt, total, plus, minus, mul, div):
    global answer_min, answer_max
    if cnt == N:
        answer_min = min(answer_min, total)
        answer_max = max(answer_max, total)
        return

    if plus > 0:
        dfs(cnt + 1, total + num_list[cnt], plus - 1, minus, mul, div)

    if minus > 0:
        dfs(cnt + 1, total - num_list[cnt], plus, minus - 1, mul, div)

    if mul > 0:
        dfs(cnt + 1, total * num_list[cnt], plus, minus, mul - 1, div)

    if div > 0:
        dfs(cnt + 1, int(total / num_list[cnt]), plus, minus, mul, div - 1)


dfs(1, num_list[0], operator_list[0], operator_list[1], operator_list[2], operator_list[3])
print(answer_max)
print(answer_min)