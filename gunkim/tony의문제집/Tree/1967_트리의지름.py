import sys
sys.setrecursionlimit(10000)

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
        return [0]
    else:
        for i in range(len(tree[node])):
            save[node].append(max(findAndSave(tree[node][i][0])) + tree[node][i][1])
    return save[node]


findAndSave(1)
answer = 0
for i in range(n+1):
    if len(save[i]) > 0:
        save[i].sort(reverse=True)
        answer = max(answer, sum(save[i][:2]))

print(answer)