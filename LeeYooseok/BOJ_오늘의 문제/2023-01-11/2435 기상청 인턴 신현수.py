N, K = map(int, input().split())
temp_list = list(map(int, input().split()))

answer = -100 * 100

for i in range(N - K + 1):
    answer = max(answer, sum(temp_list[i: i + K]))

print(answer)