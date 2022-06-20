# back tracking (dfs 활용)
import sys

n = int(input())
nums = list(map(int, input().split()))

# +, -, X, %
operator_num = list(map(int, input().split()))

result_min, result_max = sys.maxsize, -1 * sys.maxsize


def dfs(cnt, total, plus, minus, mul, div):
    global result_min, result_max

    if cnt == n:
        result_min = min(total, result_min)
        result_max = max(total, result_max)
        return

    if plus > 0:
        dfs(cnt + 1, total + nums[cnt], plus - 1, minus, mul, div)

    if minus > 0:
        dfs(cnt + 1, total - nums[cnt], plus, minus - 1, mul, div)

    if mul > 0:
        dfs(cnt + 1, total * nums[cnt], plus, minus, mul - 1, div)

    if div > 0:
        dfs(cnt + 1, int(total / nums[cnt]), plus, minus, mul, div - 1)


dfs(1, nums[0], operator_num[0], operator_num[1], operator_num[2], operator_num[3])
print(result_max)
print(result_min)
