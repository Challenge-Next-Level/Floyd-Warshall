import math, sys

input = sys.stdin.readline
N = int(input())
L = list(map(int, input().split()))
M = int(input())

# leaf node의 개수 = 2**K의 형태로 맞춰주기
# 5 -> 8개
node = math.ceil(math.log2(N))
node = 2 ** node

# tree의 Node 개수 = 2*(node)
tree = [[float('inf'), -1] for _ in range(node * 2)]

# initialize (leaf)
for i in range(N):
    treeNum = i + node # tree[node:] -> leaf node 구역
    tree[treeNum] = [L[i], i]

# initailize (all node)
# 자식 트리 중 더 작은 값으로 부모 트리를 채운다.
for i in range(node - 1, 0, -1):
    # 1의 자식 -> 2, 3 | 2의 자식 -> 4, 5 | 3의 자식 -> 6, 7
    left, right = tree[2 * i], tree[(2 * i) + 1]
    if left[0] <= right[0]:
        tree[i] = [left[0], left[1]]
    else:
        tree[i] = [right[0], right[1]]


def update(idx, value):
    treeNum = idx + node
    tree[treeNum][0] = value # leaf 노드의 값 업데이트

    # 자식 트리 중 더 작은 값으로 부모 트리를 채운다.
    while treeNum != 1:
        treeNum = treeNum // 2 # treeNum = 부모 트리의 idx
        left, right = tree[2 * treeNum], tree[(2 * treeNum) + 1]

        if left[0] <= right[0]:
            tree[treeNum] = [left[0], left[1]]
        else:
            tree[treeNum] = [right[0], right[1]]


# main
for _ in range(M):
    l = input().split()

    # 루트 노드에 저장된 값 = [최솟값, 최솟값의 인덱스]
    if len(l) == 1:
        print(tree[1][1] + 1)

    else:
        _, i, v = l
        i, v = int(i), int(v)

        update(i - 1, v)