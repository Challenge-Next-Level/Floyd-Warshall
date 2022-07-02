import sys

input = sys.stdin.readline


def dfs(left, right, string):
    if len(string) == target:
        answers.add(string)
        return
    if left > 0:
        # left 쪽으로 하나 더 연장
        dfs(left - 1, right, string + N[left - 1:right + 1])
    if right < n:
        # right 쪽으로 하나 더 연장
        dfs(left, right + 1, string + N[left: right + 2])


N = input().rstrip()
n = len(N)

target = n * (n + 1) // 2  # 완성된 문자열의 길이 : 1 ~ n 까지의 합
answers = set()
for i in range(n):
    dfs(i, i, N[i])

print(len(answers))
