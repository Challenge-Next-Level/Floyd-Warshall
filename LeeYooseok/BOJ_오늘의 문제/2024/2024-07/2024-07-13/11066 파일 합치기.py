# 파일의 위치가 바뀔 수 없다
# 1 ~ K 까지의 합치는 비용의 최소 -> 1 <= j <= K 인 j 에 대하여 -> (1 ~ j 까지 합치는 비용의 최소 + (j + 1) ~ K 까지 합치는 비용의 최소) 들의 최소값 이다.
import sys

# dp 초기화
# i ~ i + 1 까지 합치는 비용의 최소 -> i 번째 크기 + (i + 1) 번째 크기

input = sys.stdin.readline

T = int(input())
for _ in range(T):
    K = int(input())
    size_list = list(map(int, input().split()))

    # 부분합
    prefix_sum = size_list[:]
    for k in range(1, K):
        prefix_sum[k] += prefix_sum[k - 1]
    prefix_sum = [0] + prefix_sum

    # dp[i][j] = (i + 1) 번째 파일부터, (j + 1) 번째 파일까지 합치는 비용의 최소 -> dp[0][K - 1] 이 정답
    dp = [[0] * K for _ in range(K)]

    # dp 초기화
    for i in range(K - 1):
        dp[i][i + 1] = sum(size_list[i: i + 2])

    # 맨 뒤 파일부터 합치는 범위를 늘려나간다.
    for j in range(K, -1, -1):
        for l in range(j + 1, K):
            if dp[j][l] == 0:  # -> (j + 1) 부터 (l + 1) 번째 파일 까지 합치는 비용의 최소
                new_value = 1e9
                sum_j_l = prefix_sum[l + 1] - prefix_sum[j]  # j ~ l 번째 파일들의 비용 합
                for m in range(j, l):
                    new_value = min(new_value, dp[j][m] + dp[m + 1][l])
                dp[j][l] = new_value + sum_j_l
    print(dp[0][K - 1])