N = int(input())
board = list(input())

B_idx = []
O_idx = []
J_idx = []

for i in range(N):
    if board[i] == 'B':
        B_idx.append(i)
    elif board[i] == 'O':
        O_idx.append(i)
    elif board[i] == 'J':
        J_idx.append(i)

dp = [-1 for _ in range(N)]
dp[0] = 0

for i in range(1, N):
    dp_val = 1e9
    if board[i] == 'B':
        for j_idx in J_idx:
            if j_idx > i:
                break
            if dp[j_idx] != -1:
                dp_val = min(dp_val, dp[j_idx] + (i - j_idx) ** 2)
    elif board[i] == 'O':
        for b_idx in B_idx:
            if b_idx > i:
                break
            if dp[b_idx] != -1:
                dp_val = min(dp_val, dp[b_idx] + (i - b_idx) ** 2)
    elif board[i] == 'J':
        for o_idx in O_idx:
            if o_idx > i:
                break
            if dp[o_idx] != -1:
                dp_val = min(dp_val, dp[o_idx] + (i - o_idx) ** 2)
    if dp_val != 1e9:
        dp[i] = dp_val

print(dp[N - 1])