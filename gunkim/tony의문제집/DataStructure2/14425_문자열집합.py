import sys

n, m = map(int, sys.stdin.readline().split())
stringDict = {}
for _ in range(n):
    name = sys.stdin.readline().split()[0]
    stringDict[name] = True
answer = 0
for _ in range(m):
    question = sys.stdin.readline().split()[0]
    if question in stringDict:
        answer += 1
print(answer)