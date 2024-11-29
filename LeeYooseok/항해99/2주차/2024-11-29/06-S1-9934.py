K = int(input())

answer = [[] for _ in range(K)]

pre_order = list(map(int, input().split()))


def solve(order, k):
    if len(order) == 1:
        answer[k].append(order[0])
        return

    mid = len(order) // 2
    left_children = order[:mid]
    parent = order[mid]
    right_children = order[mid + 1:]

    answer[k].append(parent)

    solve(left_children, k + 1)
    solve(right_children, k + 1)


solve(pre_order, 0)

for a in answer:
    print(*a)
