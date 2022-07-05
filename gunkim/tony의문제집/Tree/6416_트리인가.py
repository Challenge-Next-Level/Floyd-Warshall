import sys
from collections import deque

tree = []
test = 1


def bfs(node, visited, treeNode):
    visited[node] = True
    stack = deque([node])
    while stack:
        start = stack.popleft()
        for tn in treeNode[start]:
            if not visited[tn]:
                visited[tn] = True
                stack.append(tn)


while True:
    case = list(map(int, sys.stdin.readline().split()))
    if case and case[0] == -1: # 테스트 종료
        break
    elif len(case) == 0: # 새로운 테스트 시작
        tree = []
        continue
    else:
        for i in range(0, len(case), 2):
            if case[i] == 0 and case[i+1] == 0: # 트리인지 판별
                flag = 0
                makeTree = {}
                haveParent = {}
                visit = {}
                for j in range(len(tree)):
                    parent, child = tree[j]
                    if child in haveParent: # 부모가 여러개라면 not tree
                        print("Case", test, "is not a tree.")
                        flag = 1
                        break
                    haveParent[child] = True
                    if parent not in makeTree: # 쌍방 연결관계로 만들기
                        makeTree[parent] = []
                        visit[parent] = False
                    if child not in makeTree:
                        makeTree[child] = []
                        visit[child] = False
                    makeTree[parent].append(child)
                    makeTree[child].append(parent)
                if len(tree) == 0:
                    print("Case", test, "is a tree.")
                    flag = 1
                if flag == 0: # dfs 탐색으로 연결이 모두 되었는지 확인
                    bfs(tree[0][0], visit, makeTree)
                    for key in visit.keys():
                        if not visit[key]: # 방문하지 않은 노드는 not tree
                            print("Case", test, "is not a tree.")
                            flag = 1
                            break
                    if flag == 0:
                        print("Case", test, "is a tree.") # 모두 방문했다면 is a tree
                test += 1
            else: # 연결 관계 저장하기
                tree.append([case[i], case[i+1]])