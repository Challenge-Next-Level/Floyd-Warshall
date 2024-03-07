import sys

input = sys.stdin.readline

N = int(input())
A_list = list(map(int, input().split()))

for i in range(1, N):
    A_list[i] += A_list[i - 1]
A_list.insert(0, 0)

M = int(input())
for _ in range(M):
    i, j = map(int, input().split())

    print(A_list[j] - A_list[i - 1])