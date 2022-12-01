n = int(input())
num_list = list(map(int, input().split()))

prefix_sum = 0
answer = 0

for idx in range(n - 1):
    prefix_sum += num_list[idx]
    answer += prefix_sum * num_list[idx + 1]

print(answer)