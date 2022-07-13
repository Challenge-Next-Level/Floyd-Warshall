# 재귀 제한 넉넉히 하니까 '시간초과' 해결됨.
# 반례)루트 노드에서 바로 여러 가지로 나뉠 수 있음. 즉 루트 노드가 기가 노드가 될 수 있음.
import sys

sys.setrecursionlimit(1000000)
n, r = map(int, sys.stdin.readline().split())
tree = [[] for _ in range(n + 1)]
for _ in range(n-1):
    start, end, length = map(int, sys.stdin.readline().split())
    tree[start].append([end, length])
    tree[end].append([start, length])

nodeNumber = [0 for _ in range(n+1)]


def find(node):
    global r
    if node == r and len(tree[node]) >= 2: # 루트노드가 기가노드일 수 있음(반례 처리)
        nodeNumber[node] = 1
        return node
    if len(tree[node]) > 2:
        nodeNumber[node] = 1
        return node
    for num, dist in tree[node]:
        if nodeNumber[num] == 0:
            if node == r:
                nodeNumber[node] = 2
            nodeNumber[num] = 2
            return find(num)


def dfs(start, isBranch, totalLen): # isBranch: 0 - 가지, 2 - 기둥
    if len(tree[start]) == 1 and totalLen != 0:
        global answer1, answer2
        if isBranch == 2:
            answer1 = max(answer1, totalLen)
        else:
            answer2 = max(answer2, totalLen)
        return
    for number, distance in tree[start]:
        if visit[number] == 0 and nodeNumber[number] == isBranch:
            visit[number] = 1
            dfs(number, isBranch, totalLen + distance)
    return


gigaNode = find(r) # 기가 노드를 찾는다
visit = [0 for _ in range(n+1)]
answer1, answer2 = 0, 0

if gigaNode is not None: # 가지가 있을 때
    visit[gigaNode] = 1
    dfs(gigaNode, 2, 0)
    dfs(gigaNode, 0, 0)
else: # 기둥만 있을 때
    visit[r] = 1
    dfs(r, 2, 0)

print(answer1, answer2)