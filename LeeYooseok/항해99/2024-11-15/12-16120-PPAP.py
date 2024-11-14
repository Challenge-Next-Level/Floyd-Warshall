import sys

input = sys.stdin.readline

S = input().rstrip()

PPAP = ["P", "P", "A", "P"]

stack = list()

for s in S:
    stack.append(s)

    if len(stack) >= 4 and stack[:-4] == PPAP:
        for _ in range(3):
            PPAP.pop()

if stack[0] == "P":
    print("PPAP")
else:
    print("NP")