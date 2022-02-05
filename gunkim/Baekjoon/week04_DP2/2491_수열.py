N = int(input())
nums = list(map(int, input().split()))
up = [1] * N
down = [1] * N
for i in range(1, N): # 오름차순 dp 계산
    if nums[i] >= nums[i - 1]:
        up[i] = up[i - 1] + 1
for i in range(N - 2, -1, -1): # 내림차순 dp 계산
    if nums[i] >= nums[i + 1]:
        down[i] = down[i + 1] + 1
answer = max(max(up), max(down))
print(answer)