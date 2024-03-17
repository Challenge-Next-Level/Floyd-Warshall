import sys

input = sys.stdin.readline

N, K = map(int, input().split())
satisfaction_list = list(map(int, input().split()))

dp = [0] * N  # dp[i]: i번쨰 까지의 최대 탈피 에너지
lmax, ans = 0, 0  # lmax : # 애벌레가 먹기 시작하는 구간에서 지금까지 얻었던 최대 탈피 에너지
tmp = 0  # 현재 만족도
left, right = 0, 0  # 투 포인터
while right <= N:
    # 만족도가 최소를 넘었을 때, 더 이상 먹을 수 없음.
    if tmp >= K:
        if left == 0:
            lmax = 0
        else:
            max(lmax, dp[left - 1])
        # dp 값 갱신 : 최대 탈피 에너지 + (현재 만족도 - 최소 만족도)
        dp[right - 1] = max(dp[right - 1], lmax + tmp - K)

        # 구간 줄이기
        tmp -= satisfaction_list[left]
        left += 1
    # 만족도가 최소를 넘지 못했을 때, -> right 를 늘림.
    else:
        tmp += satisfaction_list[right]
        right += 1

for i in range(N):
    ans = max(ans, dp[i])
print(ans)