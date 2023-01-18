# K 개를 하나하나 다 나누었지만, 그럴 필요가 없는 문제이다.

import sys
from collections import defaultdict

input = sys.stdin.readline

N = int(input())

tree = defaultdict(list)

for i in range(1, N + 1):
    u, v = map(int, input().split())
    if not (u == -1 and v == -1):
        tree[i].append(u)
        tree[i].append(v)
    tree[i].append(0)

K = int(input())


def drop(node):
    global answer
    # 리프 노드이면 끝
    if len(tree[node]) == 1:
        answer = node
        return
    # 왼쪽 또는 오른쪽 자식에게 떨굼
    if tree[node][0] == -1:
        tree[tree[node][1]][-1] += 1
        drop(tree[node][1])
    elif tree[node][1] == -1:
        tree[tree[node][0]][-1] += 1
        drop(tree[node][0])
    else:
        # 값 비교 - 왼쪽 서브트리에 담긴 모든 구슬의 수 <= 오른쪽 서브트리에 담긴 모든 구슬의 수일 경우
        if tree[tree[node][0]][-1] <= tree[tree[node][1]][-1]:
            # 왼쪽 자식 노드로 떨어진다.
            tree[tree[node][0]][-1] += 1
            drop(tree[node][0])
        else:
            # 오른쪽 자식 노드로 떨어진다.
            tree[tree[node][1]][-1] += 1
            drop(tree[node][1])


answer = 0
for _ in range(K):
    # 구슬 떨어짐
    drop(1)

print(answer)
