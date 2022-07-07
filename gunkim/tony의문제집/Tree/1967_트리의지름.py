import sys

n = int(input())
tree = [[] for _ in range(n+1)]
myWeight = [0 for _ in range(n+1)]
for _ in range(n-1):
    parent, child, weight = map(int, sys.stdin.readline().split())
    tree[parent].append([child, weight])
    myWeight[child] = weight

save = [[] for _ in range(n+1)]


def findAndSave(node):
    if len(tree[node]) == 0:
        return myWeight[node]
    elif len(tree[node]) == 1:
        return max(save[tree[node][0]]) + myWeight[tree[node][0]]
    else:
        return max(max(save[tree[node][0]]) + myWeight[tree[node][0]], max(save[tree[node][1]]) + myWeight[tree[node][1]])