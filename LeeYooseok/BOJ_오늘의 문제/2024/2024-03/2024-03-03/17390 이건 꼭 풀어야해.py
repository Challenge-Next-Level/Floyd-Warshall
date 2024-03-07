import sys

input = sys.stdin.readline

N, Q = map(int, input().split())

A_list = list(map(int, input().split()))
A_list.sort()

prefix_sum_A = [0, A_list[0]]

for i in range(1, N):
    prefix_sum_A.append(prefix_sum_A[-1] + A_list[i])

for _ in range(Q):
    L, R = map(int, input().split())

    if L == 1:
        print(prefix_sum_A[R])
    else:
        print(prefix_sum_A[R] - prefix_sum_A[L - 1])
