# 재귀 깊이 설정 필요
# inorder(중위 순회) 구현은 쉬웠으나 간선 이동 카운트를 어떻게 구해야 할지 의문이었음
# (전체 카운트 - 맨 오른쪽 순회 카운트) 로 해결하는게 방법
import sys
sys.setrecursionlimit(10**8)

n = int(input())
node = [[0,0] for _ in range(n+1)] # 노드의 자식을 저장
parent = {} # 노드의 부모를 저장
for _ in range(n):
    num, a, b = map(int, sys.stdin.readline().split())
    node[num] = [a, b]
    if a != -1:
        parent[a] = num
    if b != -1:
        parent[b] = num

countTotal = 0 # 전체 간선 순회 카운트
countRight = 0 # (종료 노드 -> 루트 노드) 까지 간선 카운트
lastNode = 1


def inorder(nd): # 중위 순회
    global countTotal, lastNode
    if node[nd][0] != -1:
        inorder(node[nd][0])
        countTotal += 1
    lastNode = nd # 마지막 노드 갱신
    countTotal += 1
    if node[nd][1] != -1:
        inorder(node[nd][1])
        countTotal += 1
    return


inorder(1) # root node는 항상 1

while lastNode != 1:
    countRight += 1
    lastNode = parent[lastNode]
print(countTotal-countRight-1)