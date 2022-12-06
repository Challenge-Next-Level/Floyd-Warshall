import sys

input = sys.stdin.readline

N = int(input())
nan_list = list(map(int, input().split()))

prefix_sum_list = [0, 0]
for idx in range(N - 1):
    if nan_list[idx] > nan_list[idx + 1]:
        prefix_sum_list.append(prefix_sum_list[-1] + 1)
    else:
        prefix_sum_list.append(prefix_sum_list[-1])

Q = int(input())
for _ in range(Q):
    x, y = map(int, input().split())
    print(prefix_sum_list[y] - prefix_sum_list[x])

