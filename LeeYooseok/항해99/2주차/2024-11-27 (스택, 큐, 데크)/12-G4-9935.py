import sys

input = sys.stdin.readline

X = list(input().rstrip())
Y = list(input().rstrip())
len_Y = len(Y)
answer = list()

for i in range(len(X)):
    answer.append(X[i])
    if answer[-len_Y:] == Y:
        for _ in range(len_Y):
            answer.pop()

if answer:
    print("".join(answer))
else:
    print("FRULA")