import sys

input = sys.stdin.readline

N, K = map(int, input().split())
num_list = list(map(int, input().split()))
num_list.sort()
print(num_list[K - 1])