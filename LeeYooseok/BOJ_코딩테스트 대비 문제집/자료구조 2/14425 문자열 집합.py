N, M = map(int, input().split())

S_set = set()
for _ in range(N):
    S_set.add(input())

result = 0
for _ in range(M):
    s = input()

    if s in S_set:
        result += 1

print(result)

