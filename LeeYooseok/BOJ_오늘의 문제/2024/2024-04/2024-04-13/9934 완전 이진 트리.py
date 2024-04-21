# 중위 순회의 완전 이진 트리 복구
import sys

input = sys.stdin.readline

K = int(input())

inorder = list(map(int, input().split()))

answer = [[] for _ in range(K)]


def to_tree(left, right, depth):
    mid = (left + right) // 2

    if left > right:
        return
    answer[depth].append(inorder[mid])

    to_tree(left, mid - 1, depth + 1)
    to_tree(mid + 1, right, depth + 1)


to_tree(0, len(inorder) - 1, 0)

for a in answer:
    print(*a)
