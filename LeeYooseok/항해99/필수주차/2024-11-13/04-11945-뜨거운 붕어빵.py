import sys

input = sys.stdin.readline

N, M = map(int, input().split())
for _ in range(N):
    x_board = input().rstrip()
    print(x_board[::-1])
