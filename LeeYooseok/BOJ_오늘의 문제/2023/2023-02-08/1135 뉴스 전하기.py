N = int(input())
parent_list = list(map(int, input().split()))

tree = [[] for _ in range(N)]

# tree 생성
for idx in range(1, N):
    tree[parent_list[idx]].append(idx)  # idx번째 노드의 부모는 parent_list[i]

# time[v] = v를 root로 하는 subtree에 정보를 모두 전달하는데 걸리는 시간
time = [False] * N


def dp(v):
    child_t = []
    for child in tree[v]:
        # Leaf까지 내려감
        dp(child)
        # 각 child를 root로 하는 subtree에 정보 전달하는데 걸리는 시간 모음
        child_t.append(time[child])
    if not tree[v]:
        # child가 없으면 0
        child_t.append(0)

    child_t.sort(reverse=True)  #시간이 오래 걸리는 순으로 정렬
    # 시간이 오래 걸리는 쪽부터 먼저 전화를 돌리기
    need_time = list()
    for i in range(len(child_t)):
        need_time.append(child_t[i] + i + 1)  # v가 루트 노드일때, i 번째에 전화를 걸고 난 후 시간 : child_t[i] + (i + 1)

    time[v] = max(need_time)  # 그 중에 가장 오래 걸리는 시간을 assign


dp(0)
print(time[0] - 1)  # Root node에 정보 전달하는 시간은 없으니 1빼기
