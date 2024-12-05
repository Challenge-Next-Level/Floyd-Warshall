import sys

input = sys.stdin.readline

N = int(input())

num_list = [int(input().rstrip()) for _ in range(N)]
num_list.sort()

print("\n".join(list(map(str, num_list))))
