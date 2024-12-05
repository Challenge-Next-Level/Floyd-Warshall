import sys

input = sys.stdin.readline

S = input().rstrip()
P = input().rstrip()

if P in S:
    print(1)
else:
    print(0)