import sys
from collections import deque

n = int(input())
tree = [[] for _ in range(n+1)]
haveParent = [False for _ in range(n+1)]
for _ in range(n):
    num, left, right = map(int, sys.stdin.readline().split())
    tree[num] = [left, right]
    if left != -1:
        haveParent[left] = True
    if right != -1:
        haveParent[right] = True

rootNode = -1
for i in range(1,n+1): # root 노드를 찾는다
    if haveParent[i] is False:
        rootNode = i
        break

column = {} # 각 번호가 몇 번째 열에 저장되는지 확인
idx = 1
row = [[] for _ in range(n+1)] # 각 행에 어떤 번호들이 있는지 확인
row[1].append(rootNode)
visit = [0 for _ in range(n+1)] # bfs 탐색 용도
visit[rootNode] = 1


def search(node): # 중위 순회
    global idx
    if node == -1:
        return
    search(tree[node][0]) # 왼쪽 서브 트리 탐색
    column[node] = idx
    idx += 1
    search(tree[node][1]) # 오른쪽 서브 트리 탐색


def bfs(num): # depth를 인자로 넘겨주며 bfs 탐색
    dq = deque([[num, 1]])
    while dq:
        number, depth = dq.popleft()
        for child in tree[number]:
            if child != -1 and visit[child] == 0:
                visit[child] = 1
                row[depth+1].append(child)
                dq.append([child, depth+1])


search(rootNode) # 열에 대해 계산
bfs(rootNode) # 행에 대해 계산

maxDif = 0
result = []
for i in range(1, n+1): # 각 행에 대해
    if len(row[i]) == 0:
        break
    left, right = column[row[i][0]], column[row[i][0]]
    for j in range(1, len(row[i])): # 열 좌, 우 끝의 차이 확인
        index = column[row[i][j]]
        left = min(left, index)
        right = max(right, index)
    result.append([i, right-left+1])
    maxDif = max(maxDif, right-left+1)

answer = float('inf')
for i in range(len(result)): # 정답 도출
    if result[i][1] == maxDif:
        answer = min(answer, result[i][0])
print(answer, maxDif)