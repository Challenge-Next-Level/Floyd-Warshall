n, w = map(int, input().split())

coin = [int(input()) for _ in range(n)]

for i in range(n - 1):
    if coin[i] < coin[i + 1]:
        w += ((coin[i + 1] - coin[i]) * (w // coin[i]))

print(w)