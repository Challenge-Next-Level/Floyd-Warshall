N, M = map(int, input().split())

tree_list = list(map(int, input().split()))

answer = 0
start, end = 0, max(tree_list)

while start <= end:
    mid = (start + end) // 2

    get_tree = 0
    for tree in tree_list:
        if tree > mid:
            get_tree += (tree - mid)

    if get_tree >= M:
        answer = max(answer, mid)
        start = mid + 1
    else:
        end = mid - 1

print(answer)