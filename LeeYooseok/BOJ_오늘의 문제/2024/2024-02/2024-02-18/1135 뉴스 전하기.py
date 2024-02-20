N = int(input())

t = list(map(int, input().split()))
# tree 만들기
tree = [[] for _ in range(N)]
for idx in range(1, N):
    tree[t[idx]].append(idx)

# sub tree 포함 자식 노드의 개수
child_cnt_list = [0] * N

def dfs(node):
    # 자식이 있으면
    if tree[node]:
        child_node = []
        for child in tree[node]:
            # 자식의 자식 개수를 세고
            dfs(child)
            child_node.append(child_cnt_list[child])

        # 자식의 수가 많은 자식 부터 연락을 돌린다.
        child_node.sort(reverse=True)
        # child_node[i] 에게 연락 돌리는데 걸리는 시간 : child_node[i] 의 자식 수 + i 번째 + 1
        child_node = [child_node[i] + i + 1 for i in range(len(child_node))]
        # node 의 자식들 중 연락 돌리는데 가장 많이 걸리는 시간이 node 가 연락을 돌리는 시간 (?)
        child_cnt_list[node] = max(child_node)
    # Leaf 노드 이면
    else:
        child_cnt_list[node] = 0

dfs(0)

print(child_cnt_list[0])