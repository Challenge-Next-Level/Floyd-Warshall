import sys
from collections import defaultdict

input = sys.stdin.readline

N = int(input())

tree = defaultdict(list)

for i in range(1, N + 1):
    u, v = map(int, input().split())

    if u != -1:
        tree[i].append(u)

    if v != -1:
        tree[i].append(v)

K = int(input())
now_node = 1
while True:
    if len(tree[now_node]) == 0:
        print(now_node)
        break

    # 자식이 하나뿐이라면
    if len(tree[now_node]) == 1:
        now_node = tree[now_node][0]
        continue

    # 나누어야 할 구슬이 짝수개라면, -> 오른쪽으로 간다.
    if K % 2 == 0:
        K = K // 2
        now_node = tree[now_node][1]
    else:
        K = K // 2
        K += 1
        now_node = tree[now_node][0]
