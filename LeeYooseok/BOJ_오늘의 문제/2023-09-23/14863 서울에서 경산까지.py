N, K = map(int, input().split())

road_list = [list(map(int, input().split())) for _ in range(N)]

dp = [[-1 for _ in range(K + 1)] for _ in range(N)]

def check(idx, total):
    # 시간 예외 처리
    if total < 0:
        return -9876543210
    # Base case : 경산까지 도달한 경우
    if idx == N:
        return 0
    # Memoization
    if dp[idx][total] != -1:
        return dp[idx][total]
    # 점화식 max(idx 경우를 도보로 갈 경우, idx 경우를 자전거로 갈 경우)
    dp[idx][total] = max(check(idx + 1, total - road_list[idx][0]) + road_list[idx][1], check(idx + 1, total - road_list[idx][2]) + road_list[idx][3])
    return dp[idx][total]

print(check(0, K))