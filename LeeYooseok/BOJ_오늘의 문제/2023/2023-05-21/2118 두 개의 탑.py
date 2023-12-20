N = int(input())
dists = [int(input()) for _ in range(N)]

# 거리 리스트 두 개를 이어 붙인 리스트의 prefix sum
ps = [0] * (2 * N + 1)
for i in range(2 * N):
    ps[i + 1] = ps[i] + dists[i % N]

ans = 0
total, right = sum(dists), 1
for left in range(2 * N):
    # 시계 방향 거리가 반시계 방향 거리보다 크면 거리를 줄임
    while right < 2 * N + 1 and ps[right] - ps[left] <= total - ps[right] + ps[left]:
        ans = max(ans, ps[right] - ps[left])
        right += 1
print(ans)