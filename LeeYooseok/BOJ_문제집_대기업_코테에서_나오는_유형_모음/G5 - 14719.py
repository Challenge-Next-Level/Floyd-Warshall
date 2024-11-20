H, W = map(int, input().split())
block_list = list(map(int, input().split()))

answer = 0

# 처음과 가장 끝은 물이 채워지지 않는다.
for i in range(1, W - 1):
    left_max = max(block_list[:i])
    right_max = max(block_list[i + 1:])

    if block_list[i] < (min(left_max, right_max)):
        answer += (min(left_max, right_max) - block_list[i])

print(answer)
