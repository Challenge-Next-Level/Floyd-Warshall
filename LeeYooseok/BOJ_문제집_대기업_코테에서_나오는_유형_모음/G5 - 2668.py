N = int(input())

board = [0] + [int(input()) for _ in range(N)]

answer_set = set()
for i in range(1, N + 1):
    up_set = set()
    down_set = set()

    up_set.add(i)
    down_set.add(board[i])

    stack = [board[i]]
    while stack:
        now_idx = stack.pop()

        if now_idx in up_set:
            continue

        up_set.add(now_idx)
        down_set.add(board[now_idx])

        stack.append(board[now_idx])

    if up_set == down_set:
        answer_set = answer_set.union(up_set)

print(len(answer_set))
for num in sorted(list(answer_set)):
    print(num)
