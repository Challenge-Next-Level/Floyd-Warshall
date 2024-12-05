import sys

input = sys.stdin.readline

N, M = map(int, input().split())
tree_list = list(map(int, input().split()))

left, right = 0, max(tree_list)
answer = right

while left <= right:
    mid = (left + right) // 2

    now_value = 0
    for tree in tree_list:
        now_value += ((tree - mid) if (tree - mid) >= 0 else 0)

    if now_value >= M:
        left = mid + 1
        answer = mid
    else:
        right = mid - 1

print(answer)