import sys

input = sys.stdin.readline

n = int(input())
k = int(input())
num_list = [input().strip() for _ in range(n)]

answer_set = set()
visited = [False for _ in range(n)]


def make_num(num, cnt):
    if cnt == k:
        answer_set.add(num)
        return

    for i in range(n):
        if visited[i]:
            continue

        visited[i] = True
        make_num(num + num_list[i], cnt + 1)
        visited[i] = False


for j in range(n):
    visited[j] = True
    make_num(num_list[j], 1)
    visited[j] = False

print(len(answer_set))
