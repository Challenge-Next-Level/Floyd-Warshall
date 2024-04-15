from collections import deque
import sys

input = sys.stdin.readline

A, B, C = map(int, input().split())

visited = [[[False for _ in range(C + 1)] for _ in range(B + 1)] for _ in range(A + 1)]

visited[0][0][C] = True
queue = deque([[0, 0, C]])

answer_set = set()

while queue:
    a, b, c = queue.popleft()

    if a == 0:
        answer_set.add(c)

    # 물 비우기
    next_list = [[max(0, a - (B - b)), min(B, b + a), c],
                 [max(0, a - (C - c)), b, min(C, c + a)],
                 [min(A, a + b), max(0, b - (A - a)), c],
                 [a, max(0, b - (C - c)), min(C, c + b)],
                 [min(A, a + c), b, max(0, c - (A - a))],
                 [a, min(B, b + c), max(0, c - (B - b))]]

    for next_a, next_b, next_c in next_list:
        if visited[next_a][next_b][next_c]:
            continue
        visited[next_a][next_b][next_c] = True
        queue.append([next_a, next_b, next_c])

print(*sorted(list(answer_set)))