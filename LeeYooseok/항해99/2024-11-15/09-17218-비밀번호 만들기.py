A = input()
B = input()

dp = [[0 for _ in range(len(B) + 1)] for _ in range(len(A) + 1)]

for i in range(len(A)):
    for j in range(len(B)):
        if A[i] == B[j]:
            dp[i+1][j+1] = dp[i][j] + 1
        else:
            dp[i+1][j+1] = max(dp[i][j+1], dp[i+1][j])

answer = ""
A_idx, B_idx = len(A), len(B)
while dp[A_idx][B_idx] != 0:
    if dp[A_idx][B_idx] == dp[A_idx - 1][B_idx]:
        A_idx -= 1
    elif dp[A_idx][B_idx] == dp[A_idx][B_idx - 1]:
        B_idx -= 1
    else:
        answer += A[A_idx - 1]
        A_idx -= 1
        B_idx -= 1

print(answer[::-1])