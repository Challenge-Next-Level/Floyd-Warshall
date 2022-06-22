import sys

n, m = map(int, sys.stdin.readline().split())
pocketMon = []
pocketMonDict = {}
for i in range(n):
    name = sys.stdin.readline().split()[0]
    pocketMon.append(name)
    pocketMonDict[name] = i

for _ in range(m):
    problem = sys.stdin.readline().split()[0]
    if '0' <= problem[0] <= '9':
        problem = int(problem)
        print(pocketMon[problem - 1])
    else:
        print(pocketMonDict[problem] + 1)