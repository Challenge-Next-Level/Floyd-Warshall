N = int(input())
tree = list(map(int, input().split()))
del_node = int(input())

result = 0

# 삭제 노드는 -2로 update
def dfs(num, arr):
    arr[num] = -2
    # 현재 부모 노드가 num 인 node 를 재귀를 통해서 삭제
    for i in range(len(arr)):
        if arr[i] == num:
            dfs(i, arr)


dfs(del_node, tree)

# node를 지운 후, tree를 탐색하면서
for node_idx in range(len(tree)):
    # 삭제된 node가 아니고, 부모 노드가 아니면(즉, tree list 에 없으면)
    if tree[node_idx] != -2 and node_idx not in tree:
        result += 1

print(result)
