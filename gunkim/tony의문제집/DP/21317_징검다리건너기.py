# 왜 틀리는지 이해가 안감
import sys

n = int(input())
stone = [[0,0]]
for _ in range(n-1):
    small, big = map(int, sys.stdin.readline().split())
    stone.append([small, big])
k = int(input())


def minCheck(A, B):
    if A[0] < B[0]: # 최소 비용을 리턴
        return A
    elif A[0] > B[0]: # 최소 비용을 리턴
        return B
    else: # 비용이 같다면 매우 큰 점프를 안한 것으로 리턴
        if A[1] == 0 or B[1] == 0:
            return [A[0], 0]
        else:
            return [A[0], 1]


if n == 1:
    print(0)
elif n == 2:
    print(stone[1][0])
else: # 돌 3개 이상
    dp = [[0,0] for _ in range(n+1)]
    dp[2] = [stone[1][0], 0]
    for i in range(3, n+1):
        one = [dp[i-1][0] + stone[i-1][0], dp[i-1][1]] # 한 칸 전에서 최소 dp
        two = [dp[i-2][0] + stone[i-2][1], dp[i-2][1]] # 두 칸 전에서 최소 dp
        minVal = minCheck(one, two)
        if i > 3 and dp[i-3][1] == 0:
            three = [dp[i-3][0] + k, 1] # 세 칸 전에서 최소 dp
            minVal = minCheck(minVal, three)
        dp[i] = minVal

    print(dp[n][0])