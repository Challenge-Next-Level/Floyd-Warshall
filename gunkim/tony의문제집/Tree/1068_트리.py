# 트리 문제 정말 어색하다. 접근을 너무 잘못하고 어려웠던 문제.
import sys

n = int(input())
node = list(map(int, sys.stdin.readline().split()))
removeNode = int(input())


def deleteAndSearchChildNode(num):
    node[num] = -2 # -2 입력으로 제거 표시
    for i in range(n): # num을 부모로 갖는 자식 노드들을 탐색
        if node[i] == num:
            deleteAndSearchChildNode(i)
    return


deleteAndSearchChildNode(removeNode)
notLeaf = set() # 자식 노드가 있는 노드들
removed = 0 # 제거된 노드의 수
for i in range(n):
    if node[i] != -2:
        if node[i] != -1:
            notLeaf.add(node[i])
    else:
        removed += 1
# 총 노드 - 제거된 노드 - 자식이 있는 노드
print(n - len(notLeaf) - removed)