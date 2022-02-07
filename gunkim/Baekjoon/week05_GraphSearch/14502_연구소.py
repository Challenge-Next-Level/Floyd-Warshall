import sys

N, M = map(int, sys.stdin.readline().split())
virus = [[] for _ in range(N)]
for i in range(N):
    virus[i] = list(map(int, sys.stdin.readline().split()))

