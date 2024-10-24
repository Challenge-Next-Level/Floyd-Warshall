H, W, N, M = map(int, input().split())

answer = 0
for _y in range(0, H, N + 1):
    for _x in range(0, W, M + 1):
        answer += 1

print(answer)