order_list = input().strip()
board_list = [input().strip() for _ in range(2)]

order_len = len(order_list)
board_len = len(board_list[0])

dp = [[[0] * 2 for _ in range(order_len)] for _ in range(board_len)]
for i in range(board_len):
    for j in range(order_len):
        for k in range(2):
            if board_list[k][i] == order_list[j]:
                if j == 0:
                    dp[i][j][k] = 1
                else:
                    for l in range(i):
                        dp[i][j][k] += dp[l][j - 1][1 - k]

result = 0
for i in range(board_len):
    for j in range(2):
        result += dp[i][-1][j]

print(result)
