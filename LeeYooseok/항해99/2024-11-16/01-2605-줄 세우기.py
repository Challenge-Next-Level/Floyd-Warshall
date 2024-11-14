N = int(input())
number_list = list(map(int, input().split()))

answer = []
for i in range(N):
    answer.insert(i - number_list[i], i + 1)

print(*answer)