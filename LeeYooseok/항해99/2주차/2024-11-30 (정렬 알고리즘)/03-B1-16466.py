N = int(input())
number_list = list(map(int, input().split()))

number_list.insert(0, 0)

number_list.sort()

answer = N + 1
for idx in range(N):
    now_num = number_list[idx]
    next_num = number_list[idx + 1]

    if now_num + 1 != next_num:
        answer = now_num + 1
        break

print(answer)