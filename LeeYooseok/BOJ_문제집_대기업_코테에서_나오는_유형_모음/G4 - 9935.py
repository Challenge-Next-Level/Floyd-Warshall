import sys

input = sys.stdin.readline

X = list(input().rstrip())
Y = list(input().rstrip())
len_Y = len(Y)

stack = list()
for i in range(len(X)):
    stack.append(X[i])

    if len(stack) >= len_Y:
        if stack[-len_Y:] == Y:
            for _ in range(len_Y):
                stack.pop()

if stack:
    print("".join(stack))
else:
    print("FRULA")