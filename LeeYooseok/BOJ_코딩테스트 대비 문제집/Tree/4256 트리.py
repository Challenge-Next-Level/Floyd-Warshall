import sys


# 전위, 중위 순회를 입력받아 루트를 찾아 다시 왼쪽, 오른쪽으로 나눈후, 재귀 입력 그 후 루트 출력
def toPostorder(preorder, inorder):
    # 서브 트리의 노드 개수가 1 or 2개 일때는 순서대로 출력
    if len(preorder) == 0:
        return
    elif len(preorder) == 1:
        print(preorder[0], end=' ')
        return
    elif len(preorder) == 2:
        print(preorder[1], preorder[0], end=' ')
        return

    # 전위 순회의 가장 앞 자리가 루트 노드이다.
    # root_idx : 중위 순회 결과에서 루트 노드의 위치
    root_idx = inorder.index(preorder[0])

    # 중위 순회에서 왼쪽 서브트리를 찾는다.
    left_in = inorder[0:root_idx]
    # 전위 순회에서 왼쪽 서브 트리를 찾는다. 
    left_pre = preorder[1:1 + len(left_in)]
    # 재귀 함수
    toPostorder(left_pre, left_in)

    # 중위 순회에서 오른쪽 서브트리를 찾는다.
    right_in = inorder[root_idx + 1:]
    # 전위 순회에서 오른쪽 서브 트리를 찾는다.
    right_pre = preorder[len(left_pre) + 1:]
    # 재귀 함수
    toPostorder(right_pre, right_in)

    # 루트 노드 출력
    print(preorder[0], end=' ')


T = int(sys.stdin.readline().strip())

for t in range(T):
    N = int(sys.stdin.readline().strip())
    preorder = list(map(int, sys.stdin.readline().strip().split()))
    inorder = list(map(int, sys.stdin.readline().strip().split()))

    toPostorder(preorder, inorder)
    print()
