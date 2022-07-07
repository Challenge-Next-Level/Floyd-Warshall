import sys

n, w = map(int, sys.stdin.readline().split())
tree = [[] for _ in range(n+1)]
for _ in range(n-1):
    start, end = map(int, sys.stdin.readline().split())
    tree[start].append(end)
    tree[end].append(start)

leafNode = 0
for i in range(2, n+1): # root node는 절대 leaf node가 될 수 없다. 따라서 2번부터 탐색
    if len(tree[i]) == 1:
        leafNode += 1
print(round(w / leafNode, 10))