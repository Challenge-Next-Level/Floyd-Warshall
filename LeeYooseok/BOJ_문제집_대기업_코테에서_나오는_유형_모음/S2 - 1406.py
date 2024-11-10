import sys

input = sys.stdin.readline

left = list(input().rstrip())
right = list()
N = len(left)
M = int(input())

cursor = N
for _ in range(M):
    operator_list = list(input().split())

    operator = operator_list[0]

    if operator == "L" and left:
        right.append(left.pop())
    elif operator == "D" and right:
        left.append(right.pop())
    elif operator == "B" and left:
        left.pop()
    elif operator == "P":
        left.append(operator_list[1])

answer = left + right[::-1]
print(''.join(answer))