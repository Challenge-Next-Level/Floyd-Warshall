import sys

n = int(input())
stack = []
answer = 0
for _ in range(n):
    x, h = map(int, sys.stdin.readline().split())
    while len(stack) > 0 and stack[-1] > h: # 틀렸던 부분(한 번에 여러 건물을 찾아낼 수 있다)
        answer += 1
        stack.pop()
    if len(stack) == 0 or stack[-1] != h:
        if h != 0:
            stack.append(h)

print(answer + len(stack))