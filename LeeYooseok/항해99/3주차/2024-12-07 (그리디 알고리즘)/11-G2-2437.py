N = int(input())

weight_list = list(map(int, input().split()))
weight_list.sort()

answer = 1

for weight in weight_list:
    if answer < weight:
        break
    answer += weight

print(answer)