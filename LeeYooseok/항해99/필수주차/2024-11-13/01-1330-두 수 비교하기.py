import sys

input = sys.stdin.readline

A, B = map(int, input().split())

if A < B:
    print("<")
elif A > B:
    print(">")
else:
    print("==")