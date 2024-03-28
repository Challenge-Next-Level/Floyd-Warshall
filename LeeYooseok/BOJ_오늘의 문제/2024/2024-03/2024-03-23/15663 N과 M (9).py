import sys

input = sys.stdin.readline

N, M = map(int, input().split())
num_list = list(map(int, input().split()))
num_list.sort()
visited = [False for _ in range(N)]
answer_list = list()


def make_list(number_list, n):
    if n == M:
        print(*number_list)
        return

    prior_num = 0
    for i in range(N):
        if visited[i] or prior_num == num_list[i]:
            continue

        visited[i] = True
        number_list.append(num_list[i])
        prior_num = num_list[i]
        make_list(number_list, n + 1)
        visited[i] = False
        number_list.pop()


make_list([], 0)
