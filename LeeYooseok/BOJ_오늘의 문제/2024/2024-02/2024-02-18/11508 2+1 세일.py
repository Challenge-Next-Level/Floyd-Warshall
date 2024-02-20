N = int(input())
item_list = [int(input()) for _ in range(N)]

item_list.sort(reverse=True)

answer = 0

for idx in range(N):
    if idx % 3 == 2:
        continue

    answer += item_list[idx]

print(answer)