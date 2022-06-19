import sys

n = int(sys.stdin.readline().split()[0])
case = []
for i in range(n):
    x, r = map(int, sys.stdin.readline().split())
    case.append([x - r, 0, i]) # 원의 맨 왼쪽 좌표
    case.append([x + r, 1, i]) # 원의 맨 오른쪽 좌표
case.sort()
stack = []
for i in range(len(case)):
    spot, leftOrRight, number = case[i]
    if leftOrRight == 1:
        s, lOR, num = stack.pop()
        if not (lOR == 0 and num == number):
            print("NO")
            exit(0)
    else:
        stack.append(case[i])
print("YES")