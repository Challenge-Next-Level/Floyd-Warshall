n = int(input())
result = 0
stack = list()
for _ in range(n):
    x, h = map(int, input().split())
    while stack and stack[-1] > h:
        result += 1
        stack.pop()

