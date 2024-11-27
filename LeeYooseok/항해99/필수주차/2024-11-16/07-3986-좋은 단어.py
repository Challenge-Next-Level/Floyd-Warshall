import sys

input = sys.stdin.readline

N = int(input())
answer = 0

for _ in range(N):
    word = input().rstrip()

    stack = list()

    for char in word:
        if stack and stack[-1] == char:
            stack.pop()
        else:
            stack.append(char)
    if len(stack) == 0:
        answer += 1
print(answer)