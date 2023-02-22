import sys

n = int(input())

ingredients_list = list()

for _ in range(n):
    sin, ssun = map(int, input().split())
    ingredients_list.append([sin, ssun])

answer = sys.maxsize


def dfs(depth, cnt, now_sin, now_ssun):
    global answer

    if cnt != 0:
        answer = min(answer, abs(now_sin - now_ssun))

    if depth == n:
        return

    dfs(depth + 1, cnt + 1, now_sin * ingredients_list[depth][0], now_ssun + ingredients_list[depth][1])
    dfs(depth + 1, cnt, now_sin, now_ssun)


dfs(0, 0, 1, 0)

print(answer)
