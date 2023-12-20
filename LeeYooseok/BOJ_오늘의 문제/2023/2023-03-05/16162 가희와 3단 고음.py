N, A, D = map(int, input().split())
eum_list = list(map(int, input().split()))

n = 0
for i in range(N):
    if eum_list[i] == A + n * D:
        n += 1
print(n)